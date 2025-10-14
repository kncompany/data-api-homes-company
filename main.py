# main.py
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from controllers import homes_company_building, homes_company_land, homes_company_realdeal

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 라우터 직접 등록 (간결화)
app.include_router(homes_company_building.router)
app.include_router(homes_company_land.router)
app.include_router(homes_company_realdeal.router)
@app.get("/openapi.json")
async def get_openapi():
    return {"status": "ok", "openapi": app.openapi()}

@app.get("/")
async def root():
    return {"status": "ok", "message": "[빅밸류] 홈즈 컴퍼니 API 서비스 호출"}

@app.get("/health")
async def health():
    return {"status": "ok", "message": "HEALTH CHECK OK"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8014)
