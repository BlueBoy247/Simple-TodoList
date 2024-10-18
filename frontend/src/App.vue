<template>
  <div id="app">
    <h1>Todo List</h1>

    <form @submit.prevent="addTodo">
      <input type="text" v-model="newTodo" placeholder="新增 Todo" />
      <button type="submit">新增</button>
    </form>

    <br />
    <span>篩選：</span>
    <input type="radio" id="all" name="filter" value="all" v-model="filter" @change="filterTodos" checked/>
    <label for="all">全部</label>
    <input type="radio" id="active" name="filter" value="active" v-model="filter" @change="filterTodos" />
    <label for="active">未完成</label>
    <input type="radio" id="completed" name="filter" value="completed" v-model="filter" @change="filterTodos" />
    <label for="completed">已完成</label>
    
    <table>
      <tr v-for="todo in filteredTodos" :key="todo.id">
        <td><input type="checkbox" v-model="todo.completed" @change="updateTodo(todo)" /></td>
        <td id="title">
          <span :style="{ textDecoration: todo.completed ? 'line-through' : 'none' }">
            {{ todo.title }}
          </span>
        </td>
        <td><a @click="deleteTodo(todo.id)">刪除</a></td>
      </tr>
    </table>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      todos: [],
      newTodo: '',
      filter: 'all',
    };
  },
  computed: {
    filteredTodos() {
      switch (this.filter) {
        case 'active':
          return this.todos.filter((todo) => !todo.completed);
        case 'completed':
          return this.todos.filter((todo) => todo.completed);
        default:
          return this.todos;
      }
    }
  },
  methods: {
    async fetchTodos() {
      const response = await axios.get('http://127.0.0.1:8000/todos');
      this.todos = response.data;
    },
    async addTodo() {
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
    async updateTodo(todo) {
      await axios.put(`http://127.0.0.1:8000/todos/${todo.id}`, todo);
      this.fetchTodos();
    },
    async deleteTodo(id) {
      await axios.delete(`http://127.0.0.1:8000/todos/${id}`);
      this.fetchTodos();
    },
  },
  mounted() {
    this.fetchTodos();
  },
  
};
</script>

<style>
body{
  background-color: aquamarine;
}
#app {
  max-width: 60vw;
  overflow: auto;
  margin: 50px auto;
}
h1{
  text-align: center;
}
form {
  text-align: center;
}
input[type="text"] {
  padding: 8px;
  width: 80%;
  margin-right: 10px;
}
button {
  padding: 8px 12px;
}
table{
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
td span{
  margin-left: 10px;
  margin-right: 10px;
}
td a{
  cursor: pointer;
  color: #cc0000;
  text-decoration: underline;
  word-wrap: normal;
  white-space: nowrap;
}
#title{
  max-width: calc(60vw - 100px);
  text-align: left;
  overflow-wrap: break-word;
  word-wrap: break-word;
  white-space: normal;
}

</style>
