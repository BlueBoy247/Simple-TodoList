<template>
<!--
    顯示 Todo 項目的完成狀態
    使用 v-model 來雙向綁定 todo.completed 的值
    使輸入框中的值與 todo.completed 的值保持同步
    使用 @change 來觸發 updateTodo 函數
-->
<td class="complete">
    <input
        type="checkbox"
        v-model="localTodo.completed"
        @change="updateTodo"
    />
</td>

<!--
    顯示 Todo 項目的創建時間
-->
<td class="time">
    {{ formatDate(localTodo.id) }}
</td>

<!--
    顯示 Todo 項目的標題
    使用 :style 來設定標題的樣式
    使標題的樣式與 todo.completed 的值保持同步
-->
<td class="title">
    <span
        :style="{
            textDecoration:
                localTodo.completed
                ? 'line-through'
                : 'none'
            }
        "
    >
        {{ localTodo.title }}
    </span>
</td>

<!--
    刪除 Todo 項目
    使用 @click 來觸發 deleteTodo 函數
-->
<td class="delete">
    <a @click="deleteTodo">刪除</a>
</td>
</template>

<script>
export default {
    props: {
        todo: Object,
    },
    data(){
        return {
            localTodo: this.todo
        }
    },
    methods: {
        updateTodo() {
            this.$emit('update-todo', this.localTodo);
        },
        deleteTodo() {
            this.$emit('delete-todo', this.localTodo.id);
        },
        formatDate(timestamp) {
            const date = new Date(timestamp);
            return date.toLocaleString();
        },
    },
};
</script>

<style scoped>
td{
    list-style: none;
    padding: 3px;
    overflow-wrap: break-word;
    word-wrap: break-word;
    white-space: normal;
}
.complete{
    width: 15px;
}
.time{
    width: 175px;
}
.title{
    width: calc(70vw - 250px);
    text-align: left;
    overflow-wrap: break-word;
    word-wrap: break-word;
    white-space: normal;
}
.delete{
    width: 40px;
}
.delete a{
    cursor: pointer;
    color: #cc0000;
    text-decoration: underline;
    word-wrap: normal;
    white-space: nowrap;
}
</style>