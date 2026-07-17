from sqlalchemy.ext.asyncio import create_async_engine,async_sessionmaker,AsyncSession

# ============ 数据库配置 ============
ASYNC_DATABASE_URL = "mysql+aiomysql://root:123456@localhost:3307/news_app?charset=utf8"
async_engine = create_async_engine(
    ASYNC_DATABASE_URL,
    echo = True,
    pool_size = 10,
    max_overflow = 20
)
#创建会话工厂
AsyncSessionLocal = async_sessionmaker(
    bind=async_engine,#绑定数据库引擎
    class_=AsyncSession,#指定会话类
    expire_on_commit=False,#禁用会话提交后过期
)
#依赖项
async def get_database():
    async with AsyncSessionLocal() as session:
        try:
            yield session # 返回数据库会话给路由处理函数
            await session.commit() # 提交事务
        except Exception:
            await session.rollback()  # 异常回滚
            raise
        finally:
            await session.close()
