from fastapi import APIRouter, Depends,HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from starlette import status
from config.db_config import get_database
from crud.users import get_user_by_username, create_user, create_token, authenticate_user, update_user, change_pwd
from models.users import User
from schemas.user import UserRequest, UserAuthResponse, UserInfoResponse, UserUpdateRequest, UserChangePasswordRequest
from utils.auth import get_current_user
from utils.response import success_response
router = APIRouter(prefix="/api/user", tags=["user"])

# 注册接口
@router.post("/register")
async def register(user_data: UserRequest, db: AsyncSession = Depends(get_database)):
    existing_user = await get_user_by_username(db, user_data.username)
    if existing_user:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="用户名已存在")
    user = await create_user(db, user_data)
    token = await create_token(db, user.id)
    # return {
    #     "code": 200,
    #     "message": "注册成功",
    #     "data":{
    #         "token": token,
    #         "userInfo":{
    #             "id": user.id,
    #             "username": user.username,
    #             "bio": user.bio,
    #             "avatar": user.avatar
    #         }
    #     }
    # }
    response_data = UserAuthResponse(token=token, user_info=UserInfoResponse.model_validate(user))
    return success_response(message="注册成功", data=response_data)
# 登录接口
@router.post("/login")
async def login(user_data: UserRequest, db: AsyncSession = Depends(get_database)):
    user = await authenticate_user(db, user_data.username, user_data.password)
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="用户名或密码错误")
    token = await create_token(db, user.id)
    response_data = UserAuthResponse(token=token, user_info=UserInfoResponse.model_validate(user))
    return success_response(message="登录成功", data=response_data)
# 获取用户信息
@router.get("/info")
async def get_user_info(user: User = Depends(get_current_user)):
    return success_response(message="获取用户信息成功", data=UserInfoResponse.model_validate(user))
# 修改用户信息
@router.put("/update")
async def update_user_info(user_data: UserUpdateRequest, user: User = Depends(get_current_user),
                           db: AsyncSession = Depends(get_database)):
    user = await update_user(db, user.username, user_data)
    return success_response(message="修改用户信息成功", data=UserInfoResponse.model_validate(user))
    return success_response(message="修改用户信息成功")
# 修改用户密码
@router.put("/password")
async def change_password(
        password_data: UserChangePasswordRequest,
        user: User = Depends(get_current_user),
        db: AsyncSession = Depends(get_database)):
    res_chang_pwd= await change_pwd(db, user, password_data.old_password, password_data.new_password)
    if not res_chang_pwd:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="修改密码失败")
    return success_response(message="密码修改成功")

