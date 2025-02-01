# Simple-TodoList
使用Vue.js與FastAPI做的簡單本地端Todo List。

## 功能
- 新增、查看、更新、刪除 (CRUD) Todo 項目
- 前後端分離架構，提升開發效率
- 支援 CORS，方便本地開發測試

## 架構
```
Simple-TodoList/
├── backend/
│   ├── main.py
│   └── requirements.txt
├── frontend/
│   ├── public/
│   │   ├── favicon.ico
│   │   └── index.html
│   ├── src/
│   │   ├── assets/
│   │   │   └── logo.png
│   │   ├── components/
│   │   │   ├── AppHeader.vue
│   │   │   ├── TodoBoard.vue
│   │   │   ├── TodoFilter.vue
│   │   │   ├── TodoForm.vue
│   │   │   └── TodoItem.vue
│   │   ├── App.vue
│   │   └── main.js
│   ├── babel.config.js
│   ├── jsconfig.json
│   ├── package-lock.json
│   ├── package.json
│   ├── README.md
│   └── vue.config.js
├── .gitattributes
├── LICENSE
└── README.md
```

## 環境需求
- **Python 3.8+**
- **Node.js 14+ / npm**
- **FastAPI**
- **Vue.js**

## 環境安裝
前端(Vue.js)依賴：
``` bash
npm install -g @vue/cli   # 安裝 Vue CLI
npm install axios         # 安裝 axios
```

後端(FastAPI)依賴：
``` bash
pip install fastapi uvicorn pydantic fastapi[all]  # 安裝 FastAPI 和相關依賴
```

## 執行指令
### 啟動 Vue.js 前端
```bash
cd frontend
npm run serve
```
前端啟動後可在 http://localhost:8080 瀏覽應用。

### 啟動 FastAPI 後端
```bash
cd backend
uvicorn main:app --reload
```
後端啟動後可透過 http://127.0.0.1:8000/docs 查看 API 文件。