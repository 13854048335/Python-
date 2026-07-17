from fastapi import APIRouter, Depends, Query
from sqlalchemy.ext.asyncio import AsyncSession
from starlette import status

from config.db_config import get_database
from crud.history import add_history_list, get_history_list, delete_history, clear_all_history
from models.users import User
from schemas.history import HistoryAddRequest, HistoryListResponse
from utils.auth import get_current_user
from utils.response import success_response

router = APIRouter(prefix="/api/history", tags=["history"])

# 添加浏览历史
@router.post("/add")
async def history_add(
        history: HistoryAddRequest,
        db: AsyncSession = Depends(get_database),
        user: User = Depends(get_current_user)):
    data = await add_history_list(db, user.id, history.news_id)
    return success_response(message = "添加浏览历史成功", data=data)
# 获取浏览历史列表
@router.get("/list")
async def history_list(
        db: AsyncSession = Depends(get_database),
            user: User = Depends(get_current_user),
            page: int = Query(1, ge=1),
            page_size: int = Query(10, ge=1, le=100, alias="pageSize"),
):
    rows, total = await get_history_list(db, user.id, page, page_size)
    history_list = [
        {**news.__dict__, "viewTime": view_time, "historyId": history_id}
        for news, view_time, history_id in rows
    ]
    has_more = total > page * page_size
    data = HistoryListResponse(list=history_list, total=total, hasMore=has_more)
    return success_response(message = "获取浏览历史列表成功", data=data)
# 删除单条浏览历史
@router.delete("/delete/{history_id}")
async def history_delete(
        history_id: int,
        db: AsyncSession = Depends(get_database),
        user: User = Depends(get_current_user)):
    result = await delete_history(db, user.id, history_id)
    if not result:
        from fastapi import HTTPException
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="历史记录不存在")
    return success_response(message = "删除浏览历史成功")
@router.delete("/clear")
async def clear_history(
        db: AsyncSession = Depends(get_database),
        user: User = Depends(get_current_user)):
    await clear_all_history(db, user.id)
    return success_response(message="清空成功")