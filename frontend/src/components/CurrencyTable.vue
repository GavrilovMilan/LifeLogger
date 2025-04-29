<script setup>
    import {ref, onMounted} from 'vue';
    import CurrencyRow from './CurrencyRow.vue';
    import axios from 'axios';

    let currencies = ref([])

    onMounted(() => {
        getCurrencies()
    })

    let getCurrencies = () => {
        axios.get("/api/currencies")
        .then(resp => {
            currencies.value = resp.data;
        })
        .catch(err => {
            // console.error('API Error:' err.resp?.data || err.message);
            alert(err);
        })
    }
</script>

<template>
    <table>
        <caption>Currency list</caption>
        <thead>
            <th>ID</th>
            <th>Name</th>
            <th>Short name</th>
            <th>User inserted</th>
            <th>Created at</th>
            <th>User updated</th>
            <th>Updated at</th>
        </thead>
        <tbody>
            <CurrencyRow
                v-for="(curr, id) in currencies"
                :key="curr.ref_currency_id"
                :currency="curr"
            ></CurrencyRow>
        </tbody>
    </table>
</template>

<style scoped>
    table {
        border: 2px solid black;
        border-collapse: collapse;
        margin: auto;
        width: 100%;
        table-layout: fixed;
    }
    th, td {
        border: 2px solid black;
        padding: 8px;
        text-align: left;
    }
</style>