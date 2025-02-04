<template>
    <AppHeader title="Simple TodoList" author="BlueBoy247" year="2025" />
    <main>
        <TodoForm :newTodo="newTodo" @addTodo="addTodo" />
        <TodoFilter :filter="filter" @updateFilter="updateFilter" />
        <TodoBoard :todos="filteredTodos" @update-todo="updateTodo" @delete-todo="deleteTodo" />
    </main>       
</template>

<script>
// 引入 axios 用來發送 HTTP 請求
import axios from 'axios';

// 引入 components
import AppHeader from '@/components/AppHeader.vue';
import TodoForm from '@/components/TodoForm.vue';
import TodoFilter from '@/components/TodoFilter.vue';
import TodoBoard from './components/TodoBoard.vue';

// 前端 Todo 項目資料物件
export default{
    
    /** TodoList 的主組件
     *
     * @property {String} name  
     *      組件的名稱
     * @property {Object} components  
     *      組件的清單，key 為組件的名稱，value 為組件的定義（省略）
     */
    name: 'App',
    components: {
        AppHeader,
        TodoForm,
        TodoFilter,
        TodoBoard
    },

    /**
     * TodoList 的資料
     * 
     * @property {Array<Object>} todos  
     *      Todo 項目的清單，每個項目為一個物件，內容為 `{ id: number, title: string, completed: boolean }`
     * @property {string} newTodo  
     *      使用者輸入的新 Todo 項目的標題
     * @property {string} filter  
     *      篩選的類型，可能的值為 `"all"`, `"active"`, `"completed"`
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
        backendUrl(){
            return process.env.VUE_APP_BACKEND_URL;
        },
        updateFilter(val){
            this.filter = val;
        },
        /**
         * 取得 TodoList 的資料
         * 
         * @returns {Promise<void>}
         */
        async fetchTodos(){
            const response = await axios.get(`${ this.backendUrl() }/todos`);
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
        async addTodo(val){
            this.newTodo = val;
            if (this.newTodo.trim() === '') return;
            const newItem = {
                id: Date.now(),
                title: this.newTodo,
                completed: false,
            };
            await axios.post(`${ this.backendUrl() }/todos`, newItem);
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
            await axios.put(`${ this.backendUrl() }/todos/${todo.id}`, todo);
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
            await axios.delete(`${ this.backendUrl() }/todos/${id}`);
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
</style>
