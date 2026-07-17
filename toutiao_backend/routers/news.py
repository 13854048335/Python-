from fastapi import APIRouter, Depends, HTTPException
from fastapi.params import Query
from config.db_config import get_database
from crud.news import get_category, get_news_list, get_news_count, get_news_detail, increase_news_view, get_related_news
from sqlalchemy.ext.asyncio import AsyncSession

# 创建APIRouter实例
router = APIRouter(prefix="/api/news", tags=["news"])

@router.get("/categories")
async def get_news_categories(skip: int = 0, limit: int = 10, db: AsyncSession = Depends(get_database)):
    # 获取数据库里面的新闻分类
    categories = await get_category(db, skip, limit)
    return {
        "code": 200,
        "message": "success",
        "data": categories
    }

# 获取新闻列表
@router.get("/list")
async def get_new_list(
        category_id: int = Query(...,alias="categoryId"),
        page: int = Query(default=1, alias="page", ge=1),
        page_size: int = Query(default= 10,alias="pageSize",le=100),
        db: AsyncSession = Depends(get_database)
):
    offset = (page - 1) * page_size
    news_list = await get_news_list(db, category_id, offset, page_size)
    total = await get_news_count(db, category_id)
    # 跳过的 + 当前列表里的数量 < 总数量
    has_more = offset + len(news_list) < total
    return {
        "code": 200,
        "message": "success",
        "data": {
            "list": news_list,
            "total": total,
            "hasMore": has_more

        }
    }
# 获取新闻详细
@router.get("/detail")
async def get_new_detail(id: int = Query(..., alias="id"), db: AsyncSession = Depends(get_database)):
    news_detail = await get_news_detail(db, id)
    if not news_detail:
        raise HTTPException(status_code=404, detail="News not found")
    views_res = await increase_news_view(db, news_detail.id)
    if not views_res:
        raise HTTPException(status_code=404, detail="更新浏览量失败")
    related_news = await get_related_news(db, news_detail.category_id, news_detail.id)
    return {
        "code": 200,
        "message": "success",
        "data": {
            "id": news_detail.id,
            "title": news_detail.title,
            "content": news_detail.content,
            "image": news_detail.image,
            "author": news_detail.author,
            "publishTime": news_detail.publish_time,
            "categoryId": news_detail.category_id,
            "views": news_detail.views,
            "relatedNews": related_news
        }
  }


