from fastapi import APIRouter

from app.api.api_v1.endpoints.wildlife import wildlife
from app.api.api_v1.endpoints.auth import auth
from app.api.api_v1.endpoints.users import users

api_router = APIRouter()
api_router.include_router(wildlife, prefix="/wildlife", tags=["wildlife"])
api_router.include_router(auth, prefix="/auth", tags=["auth"])
api_router.include_router(users, prefix="/users", tags=["users"])