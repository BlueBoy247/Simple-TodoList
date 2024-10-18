from typing import List
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Todo資料模型
class TodoItem(BaseModel):
    id: int
    title: str
    completed: bool = False

# 模擬資料庫
todo_list: List[TodoItem] = []

# 獲取所有 Todo 項目
@app.get("/todos", response_model=List[TodoItem])
def get_todos():
    return todo_list

# 新增 Todo 項目
@app.post("/todos", response_model=TodoItem)
def create_todo(todo: TodoItem):
    todo_list.append(todo)
    return todo

# 更新 Todo 項目
@app.put("/todos/{todo_id}", response_model=TodoItem)
def update_todo(todo_id: int, updated_todo: TodoItem):
    for index, todo in enumerate(todo_list):
        if todo.id == todo_id:
            todo_list[index] = updated_todo
            return updated_todo
    raise HTTPException(status_code=404, detail="Todo not found")

# 刪除 Todo 項目
@app.delete("/todos/{todo_id}")
def delete_todo(todo_id: int):
    global todo_list
    todo_list = [todo for todo in todo_list if todo.id != todo_id]
    return {"detail": "Todo deleted"}
