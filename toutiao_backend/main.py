from fastapi import FastAPI
from routers import news,user,favorite,history
from fastapi.middleware.cors import CORSMiddleware
from utils.exception_handlers import register_exception_handlers
app = FastAPI()

# 注册异常处理
register_exception_handlers(app)
#跨域中间件
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], # 允许所有来源的请求，也可以指定某个来源，例如："http://www.example.com"
    allow_credentials=True,# 允许发送Cookie
    allow_methods=["*"],# 允许所有HTTP方法
    allow_headers=["*"],# 允许所有HTTP头
)

@app.get("/")
async def root():
    return {"message": "Hello World"}
# 挂载路由
app.include_router(news.router)
app.include_router(user.router)
app.include_router(favorite.router)
app.include_router(history.router)
