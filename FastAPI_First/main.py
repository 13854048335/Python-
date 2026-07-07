from fastapi import FastAPI,Path,Query,HTTPException
from pydantic import BaseModel,Field
from fastapi.responses import HTMLResponse,FileResponse

# 创建一个 FastAPI 应用实例
app = FastAPI()

@app.get("/")
async def root():
    return {"message": "6666"}

#访问 /hello,响应结果msg：你好，FastAPI
@app.get("/user{id}")

async def get_user(id: int = Path(..., gt = 0, lt = 101, description="取值范围1-100之间")):
    return {"id": id, "title": f"普通用户{id}"}

#需求：查找书籍的作者，路径参数name，长度2-10
@app.get("/author/{name}")
async def get_name(name: str = Path(..., min_length=2, max_length=10, description="长度在2-10之间")):
    return {"msg",f"这是{name}的信息"}

#需求：查询新闻，分页，skip：跳过的记录数，limit：返回的记录数
@app.get("/books/book_list")
async def get_book_list(
        category: str = Query("Python", min_length=5, max_length=255),
        price: float = Query(gt=5, lt=101)
):
    return {"图书分类": category, "价格": price}
# 新增图书
class Book(BaseModel):
    name: str = Field(..., min_length=2, max_length=20)
    author: str = Field(min_length=2, max_length=20)
    price : float = Field(...,gt=0)
    publisher: str = Field(default="黑马出版社")
@app.post("/books/add")
async def add_book(book: Book):
    return book

# 响应HTML代码
@app.get("/html",response_class=HTMLResponse)
async def get_html():
    return "<h1>这是一级标题</h1>"
# 返回文件内容
@app.get("/image")
async def get_image():
    path = "./files/1.jpeg"
    return FileResponse(path)
# 自定义返回参数
# 定义一个返回新闻的接口
class News(BaseModel):
    id: int
    title: str
    content: str
@app.get("/news/{id}",response_model=News)
async def get_news(id: int):
    return {
        "id":id,
        "title":f"新闻{id}的标题",
        "content":f"新闻{id}的内容"
    }
# 异常处理
@app.get("/cars/{id}")
async def get_car(id:int):
    id_list = [1,2,3,4,5,6]
    if not id in id_list:
       raise HTTPException(status_code=404,detail="您查找的信息不存在")
    return {"id":id,"msg":"查询成功"}








