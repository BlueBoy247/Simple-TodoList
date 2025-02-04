<template>
<!--
    表格中每一行都是一個 TodoObject
    使用 v-for 來迴圈渲染每個 TodoObject
    使用 key 來指定每個 TodoObject 的唯一key
    使得 Vue 能夠正確地追蹤每個 TodoObject 的變化
-->
<table>
    <caption>待辦事項</caption>
    <thead>
        <tr>
            <th> </th>
            <th>創建時間</th>
            <th>標題</th>
            <th>刪除</th>
        </tr>
    </thead>
    <tbody>
        <tr v-for="todo in todos" :key="todo.id">
            <TodoItem
                :todo="todo"
                @update-todo="updateTodo"
                @delete-todo="deleteTodo"
            />
        </tr>
    </tbody>
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
table caption{
    display: none;
}
table thead{
    display: none;
}
</style>