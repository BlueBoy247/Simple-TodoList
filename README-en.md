# Simple-TodoList
[繁體中文](./README.md) | English

A simple Todo List application built with Vue.js and FastAPI.

## Features
- Add, view, update, and delete Todo items (CRUD)
- Frontend and backend separation to improve development efficiency
- Support CORS for easier local development and testing

## Architecture
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

## Requirements
- **Python 3.10+**
- **Node.js 14+ / npm**

## How to Run
### Local
#### frontend
1. Enter the `frontend` directory
```bash
cd frontend
```
2. Install dependencies
```bash
npm install  # Install Vue.js and related dependencies
```
3. Copy the .env file
```bash
cp .env.template .env
```
4. Run the application
```bash
npm run serve
```
Once the frontend is running, you can view the application at http://localhost:8080.

#### backend
1. Enter the `backend` directory
```bash
cd backend
```
2. Install dependencies
```bash
pip install -r requirements.txt  # Install FastAPI and related dependencies
```
3. Run the application
```bash
uvicorn main:app --reload
```
After the backend is running, the API service will run on http://127.0.0.1:8000, and you can access it through http://127.0.0.1:8000/docs to view the Swagger UI documentation.

### Docker
Start Docker Compose containers.
```bash
docker compose up -d --build
```
> Note:
> - `-d`: Run containers in the background
> - `--build`: Force rebuild the image even if the container already exists

After the containers are running, you can view the frontend application at http://localhost:8080. Besides, the backend API service will run on http://localhost:8000, and you can access it through http://localhost:8000/docs to view the Swagger UI documentation.

## Environment Variables
In the `.env` file, set the following environment variables:
- `VUE_APP_BACKEND_URL`: Specify the URL of the backend API service that the frontend should connect to (default: `http://127.0.0.1:8000`)
