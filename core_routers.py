from fastapi import APIRouter

core_router = APIRouter(prefix="/core",tags=["Rotas centrais"])

@core_router.get("/")
async def core():
    return {"Mensagem":"Acessando Endpoints."}