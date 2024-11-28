from fastapi import APIRouter

router = APIRouter(tags=['Search by keyword'])
@router.get('/get/key')
def search_by_key():
    