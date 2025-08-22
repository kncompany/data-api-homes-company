import pytz
import logging
from fluent.handler import FluentHandler, FluentRecordFormatter
from config.config import config

class CustomLogFilter(logging.Filter):
    def filter(self, record):
        attributes = ['method', 'url', 'client_ip', 'headers', 'query_params', 'request_body', 'status_code', 'response_body', 'request_time']
        for attr in attributes:
            if not hasattr(record, attr):
                setattr(record, attr, None)
        return True

KST = pytz.timezone('Asia/Seoul')

format = {
    'application': '%(name)s',
    'timestamp': '%(asctime)s',
    'level': '%(levelname)s',
    'message': '%(message)s',
    'method': '%(method)s',
    'url': '%(url)s',
    'client_ip': '%(client_ip)s',
    'headers': '%(headers)s',
    'query_params': '%(query_params)s',
    'request_body': '%(request_body)s',
    'status_code': '%(status_code)s',
    'response_body': '%(response_body)s',
    'request_time': '%(request_time)s',
    'file': '%(filename)s',
    'line': '%(lineno)d',
}

# Fluent Bit에 연결하기 위한 핸들러 설정
fluent_handler = FluentHandler(config.fluentbit_app_name + ".log", host=config.fluentbit_host, port=config.fluentbit_port)
formatter = FluentRecordFormatter(format)
fluent_handler.setFormatter(formatter)

# 콘솔 핸들러 설정
console_handler = logging.StreamHandler()
console_format = logging.Formatter(
    '[%(asctime)s] [%(levelname)s] [%(name)s] [%(filename)s:%(lineno)d] - %(message)s'
)
console_handler.setFormatter(console_format)

# 로거 설정
logger = logging.getLogger(config.fluentbit_app_name)
logger.setLevel(logging.DEBUG)
# logger.addHandler(fluent_handler)
logger.addHandler(console_handler)
logger.addFilter(CustomLogFilter())
