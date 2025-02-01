<template>
<!--
    表格中每一行都是一個 Todo 項目
    使用 v-for 來迴圈渲染每個 Todo 項目
    使用 key 來指定每個 Todo 項目的唯一key
    使得 Vue 能夠正確地追蹤每個 Todo 項目的變化
-->
<table>
    <tr v-for="todo in todos" :key="todo.id">
        <TodoItem
            :todo="todo"
            @update-todo="updateTodo"
            @delete-todo="deleteTodo"
        />
    </tr>
</table>
</template>

<script>
import TodoItem from './TodoItem.vue';

export default {
    components: { TodoItem },
    props: {
        todos: Array,
    },
    emits: ['update-todo', 'delete-todo'],
    methods: {
        updateTodo(todo) {
            this.$emit('update-todo', todo);
        },
        deleteTodo(id) {
            this.$emit('delete-todo', id);
        },
    },
};
</script>

<style scoped>
table{
    width: 100%;
    margin-top: 2%;
    text-align: center;
}
</style>