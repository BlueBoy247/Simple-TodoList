<template>
    <header>
        <h1>Simple TodoList</h1>
        <p>Copyright &copy; 2024 BlueBoy247</p>
    </header>

    <main>
        <!--
            使用 @submit.prevent 來阻止 form 的預設送出行為
            並在送出時執行 addTodo 函數
        -->
        <form @submit.prevent="addTodo">
            <!--
                使用 v-model 來雙向綁定 newTodo 的值
                使輸入框中的值與 newTodo 的值保持同步
            -->
            <input type="text" v-model="newTodo" placeholder="新增 Todo" minlength="1" maxlength="100" />
            <button type="submit">新增</button>
        </form>

        <br />
        <!--
           篩選 TodoList 的項目
            使用 v-model 來雙向綁定 filter 的值
            使選擇框中的值與 filter 的值保持同步
        -->
        <span>篩選：</span>
        <label for="all">
            <input id="all" type="radio" name="filter" value="all" v-model="filter" checked />
            全部
        </label>
        <label for="active">
            <input id="active" type="radio" name="filter" value="active" v-model="filter" />
            未完成
        </label>
        <label for="completed">
            <input id="completed" type="radio" name="filter" value="completed" v-model="filter" />
            已完成
        </label>
        
        <table>
            <!--
                表格中每一行都是一個 Todo 項目
                使用 v-for 來迴圈渲染每個 Todo 項目
                使用 key 來指定每個 Todo 項目的唯一key
                使得 Vue 能夠正確地追蹤每個 Todo 項目的變化
            -->
            <tr v-for="todo in filteredTodos" :key="todo.id">
                <!--
                    顯示 Todo 項目的完成狀態
                    使用 v-model 來雙向綁定 todo.completed 的值
                    使輸入框中的值與 todo.completed 的值保持同步
                    使用 @change 來觸發 updateTodo 函數
                -->
                <td id="complete">
                    <input type="checkbox" v-model="todo.completed" @change="updateTodo(todo)" />
                </td>
                <!--
                    顯示 Todo 項目的創建時間
                -->
                <td id="time">
                    <span>{{ formatDate(todo.id) }}</span>
                </td>
                <!--
                    顯示 Todo 項目的標題
                    使用 :style 來設定標題的樣式
                    使標題的樣式與 todo.completed 的值保持同步
                -->
                <td id="title">
                    <span :style="{ textDecoration: todo.completed ? 'line-through' : 'none' }">
                        {{ todo.title }}
                    </span>
                </td>
                <!--
                    刪除 Todo 項目
                    使用 @click 來觸發 deleteTodo 函數
                -->
                <td id="delete">
                    <a @click="deleteTodo(todo.id)">刪除</a>
                </td>
            </tr>
        </table>            
    </main>
</template>

<script>
    // 引入 axios 用來發送 HTTP 請求
    import axios from 'axios';

    // 前端 Todo 項目資料物件
    export default{
        /**
         * TodoList 的資料
         * 
         * @property {Array<Object>} todos  
         *      Todo 項目的清單，每個項目為一個物件，內容為 `{ id: number, title: string, completed: boolean }`
         * @property {string} newTodo  
         *      使用者輸入的新 Todo 項目的標題
         * @property {string} filter  
         *     篩選的類型，可能的值為 `"all"`, `"active"`, `"completed"`
         */
        data(){
            return{
                todos: [],
                newTodo: '',
                filter: 'all',
            };
        },

        // 計算屬性
        computed: {
            /**
             * 根據 filter 的值，回傳已篩選的 Todo 項目清單
             * 
             * @returns {Array<TodoItem>}
             */
            filteredTodos(){
                switch (this.filter){
                    case 'active':
                    return this.todos.filter((todo) => !todo.completed);
                    case 'completed':
                    return this.todos.filter((todo) => todo.completed);
                    default:
                    return this.todos;
                }
            }
        },

        // 方法
        methods:{
            /**
             * 取得 TodoList 的資料
             * 
             * @returns {Promise<void>}
             */
            async fetchTodos(){
                const response = await axios.get('http://127.0.0.1:8000/todos');
                this.todos = response.data;
            },
            
            /**
             * 新增 Todo 項目
             * 
             * @description
             *   如果使用者輸入的內容不為空白，則將其轉換為 TodoItem 物件
             *   並將其 POST 到後端 API，然後清空輸入框
             *   並重新 fetch TodoList 的資料
             * 
             * @returns {Promise<void>}
             */
            async addTodo(){
                if (this.newTodo.trim() === '') return;
                const newItem = {
                    id: Date.now(),
                    title: this.newTodo,
                    completed: false,
                };
                await axios.post('http://127.0.0.1:8000/todos', newItem);
                this.newTodo = '';
                this.fetchTodos();
            },

            
            /**
             * 更新 Todo 項目
             * 
             * @param {Object} todo
             *      要更新的 Todo 項目物件，包含 id、title 和 completed 狀態
             * 
             * @returns {Promise<void>}
             */
            async updateTodo(todo) {
                await axios.put(`http://127.0.0.1:8000/todos/${todo.id}`, todo);
                this.fetchTodos();
            },

            
            /**
             * 刪除 Todo 項目
             * 
             * @param {number} id
             *      要刪除的 Todo 項目的 ID
             * 
             * @returns {Promise<void>}
             */
            async deleteTodo(id) {
                await axios.delete(`http://127.0.0.1:8000/todos/${id}`);
                this.fetchTodos();
            },

            /**
             * 將 Unix Timestamp 轉換為易讀的日期字串
             * 
             * @param {number} timestamp
             *      Unix Timestamp
             * 
             * @returns {string}
             *      易讀的日期字串
             */
            formatDate(timestamp) {
                const date = new Date(timestamp);
                return date.toLocaleString();
            },
        },
        
        
        /**
         * 當組件加載完成後，自動調用 fetchTodos 方法
         * 
         * @description
         *   這個方法在組件掛載到 DOM 後自動執行，用於初始化並取得 TodoList 的資料
         */
        mounted() {
            this.fetchTodos();
        },
    };
</script>

<style>
    body{
        background-color: aquamarine;
    }
    #app{
        max-width: 70vw;
        overflow: auto;
        margin: 20px auto;
    }
    header{
        text-align: center;
    }
    main{
        min-height: 70vh;
    }
    form{
        text-align: center;
    }
    input[type="text"]{
        padding: 8px;
        width: 90%;
        margin-right: 10px;
    }
    button{
        padding: 8px 12px;
    }
    table{
        width: 100%;
        margin-top: 3%;
        text-align: center;
    }
    td{
        list-style: none;
        padding: 3px;
        overflow-wrap: break-word;
        word-wrap: break-word;
        white-space: normal;
    }
    #complete{
        width: 15px;
    }
    #time{
        width: 175px;
    }
    #title{
        width: calc(70vw - 250px);
        text-align: left;
        overflow-wrap: break-word;
        word-wrap: break-word;
        white-space: normal;
    }
    #delete{
        width: 40px;
    }
    #delete a{
        cursor: pointer;
        color: #cc0000;
        text-decoration: underline;
        word-wrap: normal;
        white-space: nowrap;
    }
</style>
