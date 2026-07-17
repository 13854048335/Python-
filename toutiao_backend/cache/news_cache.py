from typing import Any, List, Dict, Optional

from _testcapi import awaitType

from config.cache_config import get_json_cache, set_cache

# 新闻相关的缓存方法 (新闻分类的读取和写入)
CATEGORIES_KEY = "news:categories"
NEWS_LIST_PREFIX = "news_list:"
NEWS_DETAIL_PREFIX = "news:detail:"

# 获取新闻分类缓存
async def get_cache_categories():
    return await get_json_cache(CATEGORIES_KEY)
# 写入新闻分类缓存
async def set_cache_categories(data: List[Dict[str,Any]], expire: int = 7200):
    return await set_cache(CATEGORIES_KEY, data, expire)
# 获取新闻列表缓存
async def get_cache_news_list(category_id: Optional[int], page: int, size: int):
    category_part = category_id if category_id is not None else "all"
    key = f"{NEWS_LIST_PREFIX}{category_part}:{page}:{size}"
    return await get_json_cache(key)

# 写入新闻列表缓存
async def set_cache_news_list(category_id: Optional[int], page: int,
                              size: int, news_list: List[Dict[str, Any]],
                              expire = 3600 ):
    # 调用封装redis的方法，存入新闻列表缓存
    category_part = category_id if category_id is not None else "all"
    key = f"{NEWS_LIST_PREFIX}{category_part}:{page}:{size}"
    return await set_cache(key, news_list, expire)

# 获取新闻详情缓存
async def get_cache_news_detail(news_id: int) -> Optional[List[Dict[str, Any]]]:
    key = f"{NEWS_DETAIL_PREFIX}{news_id}"
    return await get_json_cache(key)

# 写入新闻详情缓存
async def set_cache_news_detail(news_id: int, news_detail: Dict[str, Any], expire: int = 86400):
    key = f"{NEWS_DETAIL_PREFIX}{news_id}"
    return await set_cache(key, news_detail, expire)
