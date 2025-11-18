# uvicorn main:app --reload
#github = https://github.com/waldenilson/simpleFastAPI.git
from fastapi import FastAPI
app = FastAPI()

from auth_routers import auth_router
from core_routers import core_router

app.include_router(auth_router)
app.include_router(core_router)
