import { createRouter, createWebHistory } from "vue-router";
import CurrencyTable from "../components/CurrencyTable.vue";
import Dashboard from '../views/Dashboard.vue';

const routes = [
    { path: '/', component: Dashboard },
    { path: '/currencies', component: CurrencyTable }
]

const router = createRouter({
    history: createWebHistory(),
    routes
})

export default router