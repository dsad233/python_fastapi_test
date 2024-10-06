from fastapi import FastAPI
import uvicorn
from src.models import models
from src.utils.DB.database import engine
from src.routers.auth import auth
from src.routers.users import users
from src.routers.posts import posts

SWAGGER_HEADERS = {
    "title": "SWAGGER UI 변경 테스트",
    "version": "100.100.100",
    "description": "## SWAGGER 문서 변경 \n - swagger 문서를 변경해보는 테스트입니다. \n - 테스트 1234 \n - 테스트 5678",
    "contact": {
        "name": "CHAECHAE",
        "url": "https://chaechae.life",
        "email": "chaechae.couple@gmail.com",
        "license_info": {
            "name": "MIT",
            "url": "https://opensource.org/licenses/MIT",
        },
    },
}

app = FastAPI(
    swagger_ui_parameters={
        "deepLinking": True,
        "displayRequestDuration": True,
        "docExpansion": "none",
        "operationsSorter": "method",
        "filter": True,
        "tagsSorter": "alpha",
        "syntaxHighlight.theme": "tomorrow-night",
    },
    **SWAGGER_HEADERS
)

models.Base.metadata.create_all(bind=engine)

app.include_router(auth.router, prefix="/auth", tags=["Auth"])
app.include_router(users.router, prefix="/users", tags=["Users"])
app.include_router(posts.router, prefix="/posts", tags=["Posts"])


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0")
    print("서버가 열렸습니다.")