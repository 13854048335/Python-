from datetime import datetime
from contextlib import asynccontextmanager

from click import echo
from fastapi import FastAPI,Depends
from sqlalchemy import DateTime, String, Float,func,select
from sqlalchemy.ext.asyncio import create_async_engine,async_sessionmaker,AsyncSession
from sqlalchemy.orm import DeclarativeBase, mapped_column, Mapped

# ============ 数据库配置 ============
ASYNC_DATABASE_URL = "mysql+aiomysql://root:123456@localhost:3307/ormdemo?charset=utf8"
async_engine = create_async_engine(
    ASYNC_DATABASE_URL,
    echo = True,
    pool_size = 10,
    max_overflow = 20
)
# ============ 定义模型类 ============
class Base(DeclarativeBase):
    create_time: Mapped[datetime] = mapped_column(
        DateTime,
        insert_default=func.now(),
        default=func.now,
        comment="创建时间"
    )
    update_time: Mapped[datetime] = mapped_column(
        DateTime,
        insert_default=func.now(),
        default=func.now,
        onupdate=func.now(),
        comment="更新时间"
    )
class Book(Base):
    __tablename__ = "book"
    id: Mapped[int] = mapped_column(primary_key=True, comment="书籍id")
    bookname: Mapped[str] = mapped_column(String(255), comment="书名")
    author: Mapped[str] = mapped_column(String(255), comment="作者")
    price: Mapped[float] = mapped_column(Float, comment="价格")
    publisher: Mapped[str] = mapped_column(String(255), comment="出版社")

# ============ 建表函数 ============
async def create_table():
    async with async_engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

# ============ 定义 lifespan 上下文管理器 ============
@asynccontextmanager
async def lifespan(app: FastAPI):
    await create_table()
    yield
    await async_engine.dispose()
app = FastAPI(lifespan = lifespan)
@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}
# 定义一个查询功能的接口  - 依赖注入，先创建依赖项获取数据库会话,Depends注入路由处理函数
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
@app.get("/books")
async def get_book(database: AsyncSession = Depends(get_database)):
   result = await database.execute(select(Book))
   book = result.scalars().all()
   return book


