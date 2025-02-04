import { createRouter, createWebHistory } from 'vue-router'
import App from './App.vue'

const routes = [
    {
        name: 'Simple TodoList',
        path: '/',
        meta: {
            title: 'Simple TodoList'
        },
        component: App
    }
]

const router = createRouter({
    history: createWebHistory(process.env.BASE_URL),
    routes
})

router.beforeEach((to) => {
    document.title = to.meta.title || 'Simple TodoList'
})

export default router