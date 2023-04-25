from fastapi import APIRouter, Depends
from bson.objectid import ObjectId
from serializers.userSerializers import userResponseEntity

from database import User
import schemas
import user_auth.oauth2 as oauth2

router = APIRouter()


@router.get('/me', response_model=schemas.UserResponse)
def get_me(user_id: str = Depends(oauth2.require_user)):
    user = userResponseEntity(User.find_one({'_id': ObjectId(str(user_id))}))
    return {"status": "success", "user": user}

