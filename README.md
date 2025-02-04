# Simple-TodoList
繁體中文 | [English](./README-en.md)

基於 Vue.js 和 FastAPI 的簡易 Todo List 應用。

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
- **Python 3.10+**
- **Node.js 14+ / npm**

## 啟動應用
### 本地端
#### frontend
1. 進入 frontend 目錄
```bash
cd frontend
```
2. 安裝依賴
```bash
npm install  # 安裝 Vue.js 和相關依賴
```
3. 複製 .env 檔案
```bash
cp .env.template .env
```
4. 啟動應用
```bash
npm run serve
```
前端啟動後可在 http://localhost:8080 瀏覽應用。

#### backend
1. 進入 backend 目錄
```bash
cd backend
```
2. 安裝依賴
```bash
pip install -r requirements.txt  # 安裝 FastAPI 和相關依賴
```
3. 啟動應用
```bash
uvicorn main:app --reload
```
後端啟動後，API 服務將運行於 http://localhost:8000，並可透過 http://localhost:8000/docs 查看 Swagger UI 文件。

### Docker
啟動 Docker Compose 容器。
```bash
docker compose up -d --build
```
> 說明：
> - `-d`：以背景模式執行容器
> - `--build`：強制重新建置映像檔（無論容器是否已存在）

應用啟動後：
- 前端應用應可透過 http://localhost:8080 瀏覽。
- 後端 API 服務應運行於 http://127.0.0.1:8000，並可透過 http://127.0.0.1:8000/docs 查看 Swagger UI 文件。

## 環境變數
在 `.env` 檔案中設定以下環境變數：
- `VUE_APP_BACKEND_URL`: 指定前端應用應該連接的後端 API 服務 URL（預設 `http://127.0.0.1:8000`）
