<template>
<!--
    使用 @submit.prevent 來阻止 form 的預設送出行為
    並在送出時執行 submitTodo 函數
-->
<form @submit.prevent="submitTodo">
    <input
        type="text"
        v-model="newTodoInput"
        placeholder="想做什麼?"
        minlength="1"
        maxlength="100"
        required
    />
    <button type="submit">新增</button>
</form>
</template>

<script>
export default{
    // 表單元件的 props
    props: {
        //  - newTodo {String}: 用於綁定輸入框的值
        newTodo: String,
    },

    // 使用 emits 宣告組件發出的事件
    emits: [
        // - 'addTodo': 當使用者提交表單時發出該事件，將新的 TodoObject 傳遞給父組件
        'addTodo'
    ],

    /**
     * 提供表單數據
     * 
     * @returns {Object}
     *   返回一個物件，包含：
     *   - newTodoInput {String}：用於綁定輸入框的值
     */
    data() {
        return {
            newTodoInput: this.newTodo,
        };
    },

    methods: {
        /**
         * 提交 TodoForm
         * 
         * @description
         *   當表單提交時，將輸入框的值 emit 給父組件
         *   並將輸入框的值清空
         */
        submitTodo() {
            this.$emit('addTodo', this.newTodoInput);
            this.newTodoInput = '';
        },
    },
};
</script>

<style scoped>
form{
    text-align: center;
    margin-bottom: 10px;
}
input[type="text"]{
    padding: 8px;
    width: 90%;
    margin-right: 10px;
}
button{
    padding: 8px 12px;
}
</style>