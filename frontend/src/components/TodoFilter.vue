<template>
<!--
    篩選 TodoList 的項目
    使用 v-model 來雙向綁定 currentFilter 的值
    使選擇框中的值與 currentFilter 的值保持同步
-->
<div>
    <span>篩選：</span>
    <label>
        <input
            type="radio"
            value="all"
            v-model="currentFilter"
        />
        全部
    </label>
    <label>
        <input
            type="radio"
            value="active"
            v-model="currentFilter"
        />
        未完成
    </label>
    <label>
        <input
            type="radio"
            value="completed"
            v-model="currentFilter"
        />
        已完成
    </label>
</div>
</template>

<script>
export default {
    props: {
        filter: String,
    },
    emits: ['updateFilter'],
    /**
     *  - currentFilter {String}:目前的篩選類型
     *      使得 v-model 連結到父組件的 filter 屬性
     *      並在數據改變時，emit updateFilter 事件
     */
    data() {
        return {
            currentFilter: this.filter,
        };
    },
    watch: {
        /**
         * 監控 currentFilter 的變化並觸發 updateFilter 事件
         *
         * @param {String} newValue
         *      新的篩選類型，可能的值為 "all", "active", "completed"
         * 
         * @emits updateFilter
         *      當 currentFilter 發生變化時，將新的篩選類型傳遞給父組件
         */
        currentFilter(newValue) {
            this.$emit('updateFilter', newValue);
        },
    },
};
</script>
