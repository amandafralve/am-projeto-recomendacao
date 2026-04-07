from fastapi import FastAPI
from src.api.v1.router import api_router

app = FastAPI(title="API de recomendação")
app.include_router(api_router, prefix="/api/v1")


if __name__ == "__main__":
    main()
