"""
引入必要的模組

模組包括:
    List: 用於類型註解以表示列表
    FastAPI, HTTPException: 提供 FastAPI 框架功能和 HTTP 錯誤處理
    CORSMiddleware: 用於處理跨來源資源共用
    BaseModel: 提供 Pydantic 的數據驗證功能
"""
from typing import List
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

# FastAPI 初始化
app = FastAPI()

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class TodoObject(BaseModel):
    """
    待辦事項物件模型

    屬性:
        id (int): 待辦事項的唯一 ID, 以 Unix Timestamp 生成
        title (str): 待辦事項的標題
        completed (bool): 待辦事項的完成狀態，預設為 False
    """
    id: int
    title: str
    completed: bool = False

# 模擬資料庫
todo_list: List[TodoObject] = []

@app.get("/", include_in_schema=False)
async def root():
    """
    APP 是否在線

    Returns:
        dict: {"alive": True}
    """
    return {"alive": True, "docs": "/docs"}

@app.get("/todos", response_model=List[TodoObject])
def get_todos():
    """
    獲取所有 TodoObject

    Returns:
        List[TodoObject]: TodoObject 的列表
    """
    return todo_list

@app.post("/todos", response_model=TodoObject)
def create_todo(todo: TodoObject):
    """
    新增 TodoObject

    Args:
        todo (TodoObject): 要新增的 TodoObject

    Returns:
        TodoObject: 新增的 TodoObject
    """
    todo_list.append(todo)
    return todo

@app.put("/todos/{todo_id}", response_model=TodoObject)
def update_todo(todo_id: int, updated_todo: TodoObject):
    """
    更新 TodoObject

    Args:
        todo_id (int): TodoObject 的 ID
        updated_todo (TodoObject): 更新後的 TodoObject 資料

    Returns:
        TodoObject: 更新後的 TodoObject

    Raises:
        HTTPException: 當指定的 TodoObject ID 不存在時，拋出 404 錯誤
    """
    for index, todo in enumerate(todo_list):
        if todo.id == todo_id:
            todo_list[index] = updated_todo
            return updated_todo
    raise HTTPException(status_code=404, detail="Todo not found")

@app.delete("/todos/{todo_id}")
def delete_todo(todo_id: int):
    """
    刪除 TodoObject

    Args:
        todo_id (int): TodoObject 的 ID

    Returns:
        dict: {"detail": "Todo deleted"}

    Raises:
        HTTPException: 當指定的 TodoObject ID 不存在時，拋出 404 錯誤
    """
    for index, todo in enumerate(todo_list):
        if todo.id == todo_id:
            todo_list.pop(index)
            return {"detail": "Todo deleted"}
    raise HTTPException(status_code=404, detail="Todo not found")
