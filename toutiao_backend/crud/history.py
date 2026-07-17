from datetime import datetime
from sqlalchemy import select, func, delete
from sqlalchemy.ext.asyncio import AsyncSession
from models.history import History
from models.news import News


# 添加浏览历史
async def add_history_list(db: AsyncSession, user_id: int, news_id: int):
    query = select(History).where(History.news_id == news_id, History.user_id == user_id)
    result = await db.execute(query)
    existing_history = result.scalar_one_or_none()
    if existing_history:
        existing_history.view_time = datetime.now()
        await db.commit()
        await db.refresh(existing_history)
        return existing_history
    else:
        history = History(news_id=news_id, user_id=user_id)
        db.add(history)
        await db.commit()
        await db.refresh(history)
        return history
# 获取浏览历史列表
async def get_history_list(db: AsyncSession, user_id: int, page: int = 1, page_size: int = 10):
    offset = (page - 1) * page_size
    count_query = select(func.count(History.id)).where(History.user_id == user_id)
    count_result = await db.execute(count_query)
    total = count_result.scalar_one()

    query = (select(News, History.view_time.label("view_time"), History.id.label("history_id"))
             .join(History, History.news_id == News.id)
             .where(History.user_id == user_id)
             .order_by(History.view_time.desc())
             .offset(offset).limit(page_size))

    result = await db.execute(query)
    rows = result.all()
    return rows, total

# 删除单条浏览历史
async def delete_history(db: AsyncSession, user_id: int, history_id: int):
    """
    删除单条历史记录
    """
    query = delete(History).where(History.user_id == user_id, History.id == history_id)
    result = await db.execute(query)
    await db.commit()
    return result.rowcount > 0

# 清空历史浏览记录
async def clear_all_history(db: AsyncSession, user_id: int):
    """
    清空历史浏览记录
    """
    query = delete(History).where(History.user_id == user_id)
    result = await db.execute(query)
    await db.commit()
    return result.rowcount > 0
