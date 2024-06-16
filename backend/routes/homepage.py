from fastapi import APIRouter

router = APIRouter()


@router.get("/")
async def homepage():
    return {"Hello": "World"}
