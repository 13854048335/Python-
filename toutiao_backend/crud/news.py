from fastapi.encoders import jsonable_encoder
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import update
from cache.news_cache import get_cache_categories, set_cache_categories, get_cache_news_list, set_cache_news_list
from models.news import Category, News
from sqlalchemy import select, func
from schemas.base import NewsItemBase


# 获取新闻分类
async def get_category(db: AsyncSession,skip: int = 0, limit: int = 10):
    # 尝试从缓存中获取数据
    cached_categories = await get_cache_categories()
    if cached_categories:
        return cached_categories
    result = await db.execute(select(Category).offset(skip).limit(limit))
    categories =  result.scalars().all() # ORM结果
    if categories:
        categories = jsonable_encoder(categories)
        await set_cache_categories(categories)
    return categories

# 获取新闻列表（查询指定分类下的所有新闻）
async def get_news_list(db: AsyncSession, category_id: int, skip: int = 0, limit: int = 10 ):
   #从缓存中获取新闻列表
   page = skip // limit + 1
   cached_news_list = await get_cache_news_list(category_id, page, limit)
   if cached_news_list:
       return [News(**item) for item in cached_news_list]
   stmt = select(News).where(News.category_id == category_id).offset(skip).limit(limit)
   result = await db.execute(stmt)
   news_list = result.scalars().all()
   #写入缓存
   if news_list:
        # 先把 ORM 数据 转换 字典才能写入缓存
        # ORM 转成 Pydantic，再转为 字典
        # by_alias=False 不适用别名，保存 Python 风格，因为 Redis 数据是给后端用的
        news_data = [NewsItemBase.model_validate(item).model_dump(mode="json", by_alias=False) for item in news_list]
        await set_cache_news_list(category_id, page, limit, news_data)
   return news_list
# 计算数量
async def get_news_count(db: AsyncSession, category_id: int):
   stmt = select(func.count(News.id)).where(News.category_id == category_id)
   result = await db.execute(stmt)
   return result.scalar_one() #只能有一个结果

# 按id查询新闻
async def get_news_detail(db: AsyncSession, id: int):
    stmt = select(News).where(News.id == id)
    result = await db.execute(stmt)
    return result.scalar_one_or_none()

# 增加浏览量
async def increase_news_view(db: AsyncSession, id: int):
    update_stmt = update(News).where(News.id == id).values(views=News.views + 1)
    result = await db.execute(update_stmt)
    await db.commit()
    # 检查数据库是否真的命中了数据
    return result.rowcount > 0

# 获取同类的推荐新闻
async def get_related_news(db: AsyncSession, category_id: int, news_id: int, limit: int = 5):
    stmt = select(News).where(
        News.id != news_id,
        News.category_id == category_id
    ).order_by(
        News.views.desc(),
        News.publish_time.desc()
    ).limit(limit)
    result = await db.execute(stmt)
    related_news = result.scalars().all()
    #用列表推导式来推导出需要的核心数据
    return [{
            "id": news.id,
            "title": news.title,
            "content": news.content,
            "image": news.image,
            "author": news.author,
            "publishTime": news.publish_time,
            "categoryId": news.category_id,
            "views": news.views,
    }
            for news in related_news]

