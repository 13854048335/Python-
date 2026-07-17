from fastapi import APIRouter, Depends, Query
from sqlalchemy.ext.asyncio import AsyncSession
from config.db_config import get_database
from crud.favorite import is_new_favorite, add_new_favorite, remove_news_favorite, get_favorite_list, \
    clear_favorite_list
from models.users import User
from schemas.favorite import FavoriteCheckResponse, FavoriteAddRequest, FavoriteListResponse
from utils.auth import get_current_user
from utils.response import success_response

router = APIRouter(prefix="/api/favorite", tags=["favorite"])

# 检查收藏状态
@router.get("/check")
async def state_check(db: AsyncSession = Depends(get_database),
        user: User = Depends(get_current_user),
        news_id: int = Query(..., alias="newsId")):
    is_favorite = await is_new_favorite(db, news_id, user.id)
    return success_response(message="检查收藏状态成功", data=FavoriteCheckResponse(isFavorite=is_favorite))

# 添加收藏
@router.post("/add")
async def favorite_add(
        favorite_data: FavoriteAddRequest,
        db: AsyncSession = Depends(get_database),
        user: User = Depends(get_current_user)):
    result = await add_new_favorite(db, favorite_data.news_id, user.id)
    return success_response(message="添加收藏成功", data=result)

# 取消收藏
@router.delete("/remove")
async def favorite_remove(
        news_id: int = Query(..., alias="newsId"),
        db: AsyncSession = Depends(get_database),
        user: User = Depends(get_current_user)):
    result = await remove_news_favorite(db, user.id, news_id)
    if not result:
        from fastapi import HTTPException
        from starlette import status
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="收藏记录不存在")
    return success_response(message="取消收藏成功")

# 获取收藏列表
@router.get("list")
async def favorite_list(
        page: int = Query(1, gt = 1),
        page_size: int = Query(10, gt = 0, le = 100, alias="pageSize"),
        db: AsyncSession = Depends(get_database),
        user: User = Depends(get_current_user)):
    rows, total = await get_favorite_list(db, user.id, page, page_size)
    favorite_list = [
        {**news.__dict__, "favoriteTime": favorite_time, "favoriteId": favorite_id} for news, favorite_time, favorite_id in rows
    ]
    has_more = total > page * page_size
    data = FavoriteListResponse(list=favorite_list, total = total, hasMore=has_more)
    return success_response(message="获取收藏列表成功", data=data)

# 清空收藏列表
@router.delete("/clear")
async def favorite_clear(
        db: AsyncSession = Depends(get_database),
        user: User = Depends(get_current_user)):
    count = await clear_favorite_list(db, user.id)
    return success_response(message=f"清空了{count}条收藏")

