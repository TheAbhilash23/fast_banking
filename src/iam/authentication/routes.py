from fastapi import APIRouter

router = APIRouter()

@router.get("/authenticate")
async def post_authenticate():
    """
    Post authentication request here to get refresh and access token for the requested user
    """
    return {"message": "List of users"}
