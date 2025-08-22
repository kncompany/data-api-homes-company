import json
import gzip
from fastapi import FastAPI, Request
from starlette.responses import StreamingResponse
from starlette.middleware.base import BaseHTTPMiddleware

from config.logging_config import logger
from datetime import datetime
from zoneinfo import ZoneInfo

MAX_REQUEST_BODY_LENGTH = 1 * 1024
MAX_RESPONSE_BODY_LENGTH = 1 * 1024
KST = ZoneInfo("Asia/Seoul")  # 한국 시간대 설정


class LoggingMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        start_time = datetime.now(KST)
        client_ip = request.headers.get("X-Forwarded-For", request.client.host)

        # 요청 본문 처리
        try:
            request_body = await request.body()
            if len(request_body) > MAX_REQUEST_BODY_LENGTH:
                request_body = request_body[:MAX_REQUEST_BODY_LENGTH] + b"...(truncated)"
            request_body_text = request_body.decode("utf-8", errors="ignore")
        except Exception as e:
            request_body_text = f"Error reading request body: {str(e)}"

        # 요청 로깅
        logger.info("Request received", extra={
            "event": "request",
            "timestamp": start_time.isoformat(),
            "method": request.method,
            "url": str(request.url),
            "client_ip": client_ip,
            "headers": json.dumps(dict(request.headers), ensure_ascii=False),
            "query_params": json.dumps(dict(request.query_params), ensure_ascii=False),
            "request_body": request_body_text,
        })

        # 다음 미들웨어 호출
        response = await call_next(request)

        # 응답 본문 버퍼링
        response_body = b"".join([chunk async for chunk in response.body_iterator])

        # gzip 압축 해제
        if "gzip" in response.headers.get("Content-Encoding", "").lower():
            try:
                response_body_text = gzip.decompress(response_body).decode("utf-8", errors="ignore")
            except Exception as e:
                response_body_text = f"Error decompressing gzip response body: {str(e)}"
        else:
            response_body_text = response_body.decode("utf-8", errors="ignore")

        # 응답 본문 길이 제한
        if len(response_body_text) > MAX_RESPONSE_BODY_LENGTH:
            response_body_text = response_body_text[:MAX_RESPONSE_BODY_LENGTH] + "...(truncated)"

        # 응답 시간 계산
        end_time = datetime.now(KST)
        request_time = round((end_time - start_time).total_seconds() * 1000, 2)

        # 로깅 레벨 설정
        if response.status_code >= 500:
            log_method = logger.error
        elif response.status_code >= 400:
            log_method = logger.warning
        else:
            log_method = logger.info

        # 응답 로깅
        log_method("Response sent", extra={
            "event": "response",
            "timestamp": end_time.isoformat(),
            "method": request.method,
            "url": str(request.url),
            "client_ip": client_ip,
            "headers": json.dumps(dict(response.headers), ensure_ascii=False),
            "status_code": response.status_code,
            "query_params": json.dumps(dict(request.query_params), ensure_ascii=False),
            "request_body": request_body_text,
            "response_body": response_body_text,
            "request_time": request_time,
        })

        # Content-Length를 깨뜨리지 않기 위해 StreamingResponse로 응답 반환
        async def response_generator():
            yield response_body

        return StreamingResponse(response_generator(), status_code=response.status_code, headers=dict(response.headers),
                                 media_type=response.media_type)


def add(app: FastAPI):
    app.add_middleware(
        LoggingMiddleware
    )
