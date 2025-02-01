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

# Todo資料模型
class TodoItem(BaseModel):
    """
    Todo 項目資料模型

    屬性:
        id (int): Todo 項目的唯一 ID，以 Unix Timestamp 生成
        title (str): Todo 項目的標題
        completed (bool): Todo 項目的完成狀態，預設為 False
    """
    id: int
    title: str
    completed: bool = False

# 模擬資料庫
todo_list: List[TodoItem] = []

# APP alive
@app.get("/", include_in_schema=False)
async def root():
    """
    APP 是否在線

    Returns:
        dict: {"alive": True}
    """
    return {"alive": True, "docs": "/docs"}

# 獲取所有 Todo 項目
@app.get("/todos", response_model=List[TodoItem])
def get_todos():
    """
    獲取所有 Todo 項目

    Returns:
        List[TodoItem]: Todo 項目的列表
    """
    return todo_list

# 新增 Todo 項目
@app.post("/todos", response_model=TodoItem)
def create_todo(todo: TodoItem):
    """
    新增 Todo 項目

    Args:
        todo (TodoItem): 要新增的 Todo 項目

    Returns:
        TodoItem: 新增的 Todo 項目
    """
    todo_list.append(todo)
    return todo

# 更新 Todo 項目
@app.put("/todos/{todo_id}", response_model=TodoItem)
def update_todo(todo_id: int, updated_todo: TodoItem):
    """
    更新 Todo 項目

    Args:
        todo_id (int): Todo 項目的 ID
        updated_todo (TodoItem): 更新後的 Todo 項目資料

    Returns:
        TodoItem: 更新後的 Todo 項目

    Raises:
        HTTPException: 當指定的 Todo ID 不存在時，拋出 404 錯誤
    """
    for index, todo in enumerate(todo_list):
        if todo.id == todo_id:
            todo_list[index] = updated_todo
            return updated_todo
    raise HTTPException(status_code=404, detail="Todo not found")

# 刪除 Todo 項目
@app.delete("/todos/{todo_id}")
def delete_todo(todo_id: int):
    """
    刪除 Todo 項目

    Args:
        todo_id (int): Todo 項目的 ID

    Returns:
        dict: {"detail": "Todo deleted"}

    Raises:
        HTTPException: 當指定的 Todo ID 不存在時，拋出 404 錯誤
    """
    for index, todo in enumerate(todo_list):
        if todo.id == todo_id:
            todo_list.pop(index)
            return {"detail": "Todo deleted"}
    raise HTTPException(status_code=404, detail="Todo not found")
