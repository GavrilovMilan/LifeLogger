<script setup>
    import {ref, computed, onMounted} from 'vue';
    import CurrencyRow from './CurrencyRow.vue';
    import axios from 'axios';
    import { onBeforeRouteUpdate } from 'vue-router';

    let currencies = ref([])
    let currencyFilter = ref('')
    let chosenId = ref(null)

    onMounted(() => {
        getCurrencies()
    })

    onBeforeRouteUpdate(() => {
        getCurrencies()
    })

    let getCurrencies = () => {
        axios.get('/api/currencies')
        .then(response => {
            currencies.value = response.data;
        })
        .catch(error => {
            console.error('API Error:', error.response?.data || error.message);
            alert(error);
        })
    }

    const filteredCurrencies = computed(() => {
        return currencies.value.filter(currency => {
            return (
                currency.name.toLowerCase().includes(currencyFilter.value.toLowerCase()) ||
                currency.short_name.toLowerCase().includes(currencyFilter.value.toLowerCase()) ||
                currency.user_inserted.toLowerCase().includes(currencyFilter.value.toLowerCase()) ||
                currency.user_updated.toLowerCase().includes(currencyFilter.value.toLowerCase())
            )
        })
    })

    const chosenCurr = (id) => {
        chosenId.value = id
    }

    const form = ref({
        name: '',
        short_name: '',
        user_inserted: 'mgavrilov',
        user_updated: 'mgavrilov'
    })

    const submitCurrency = async () => {
        axios.post('/api/currencies/', form.value)
        .then(response => {
            currencies.value.push(response.data);
            alert('Currency created!')
            form.value = {name: '', short_name: ''}
        })
        .catch(error => {
            console.error('Error:', error.response?.data || error.message);
            alert(error);
        })
    }
</script>
<template>
    <div>
        <input type="text" v-model="currencyFilter" placeholder="Search">
        <br>
        Add new
        <form @submit.prevent="submitCurrency">
            <input v-model="form.name" placeholder="Currency name" required>
            <input v-model="form.short_name" placeholder="Short code (USD)" maxlength="3" required>
            <button type="submit">Add</button>
        </form>
    </div>
    <table>
        <caption>Currency list</caption>
        <thead>
            <tr>
                <th>ID</th>
                <th>Name</th>
                <th>Short name</th>
                <th>User inserted</th>
                <th>Created at</th>
                <th>User updated</th>
                <th>Updated at</th>
                <th></th>
            </tr>
        </thead>
        <tbody>
            <CurrencyRow
                v-for="(curr, id) in filteredCurrencies"
                :key="curr.ref_currency_id"
                :currency="curr"
                :class="{ chosen: chosenId === id }"
                @click="$emit('chosenCurr', curr), chosenCurr(id)"
				@refreshCurrencies="getCurrencies"
            ></CurrencyRow>
        </tbody>
    </table>
</template>
<style scoped>
table{
    border: 2px solid black;
    border-collapse: collapse;
    margin: auto;
    width: 100%;
    table-layout: fixed;
}
th{
    border: 2px solid black;
    padding: 8px;
    text-align: left;
}
.chosen{
    background-color: #aeaeae;
}
</style>