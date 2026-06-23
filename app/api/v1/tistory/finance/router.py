from fastapi import APIRouter


router = APIRouter(prefix="/finance")

@router.get('/')
def index():
    return {"message": "Tistory Finance API is working!"}