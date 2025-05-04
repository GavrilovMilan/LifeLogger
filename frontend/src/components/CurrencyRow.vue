<script setup>
    import { ref } from 'vue';
    import axios from 'axios';

    const props = defineProps({
        currency:Object
    })

    const emit = defineEmits(['refreshCurrencies'])

    let fChange = ref(false)
    let tmpCurrency = ref({...props.currency})

    let saveChange = () => {
        axios.put(`api/currencies/${tmpCurrency.value.ref_currency_id}/`, tmpCurrency.value)
        .then(response => {
            emit('refreshCurrencies')
            fChange.value = false
            alert('Updated currency!')
        })
        .catch(error => {
            console.error('Error:', error.response?.data || error.message)
            alert('Failed to update currency')
        })
    }
</script>

<template>
    <tr v-if="!fChange">
        <td>{{ currency.ref_currency_id }}</td>
        <td>{{ currency.name }}</td>
        <td>{{ currency.short_name }}</td>
        <td>{{ currency.user_inserted }}</td>
        <td>{{ currency.created_at }}</td>
        <td>{{ currency.user_updated }}</td>
        <td>{{ currency.updated_at }}</td>
        <td>
            <button @click="fChange = true">Change</button>
        </td>
    </tr>
    <tr v-else>
        <td>{{ currency.ref_currency_id }}</td>
        <td><input type="text" v-model="tmpCurrency.name"></td>
        <td><input type="text" v-model="tmpCurrency.short_name"></td>
        <td>{{ currency.user_inserted }}</td>
        <td>{{ currency.created_at }}</td>
        <td>{{ currency.user_updated }}</td>
        <td>{{ currency.updated_at }}</td>
        <td>
            <button @click="saveChange">Save</button>
        </td>
    </tr>
</template>

<style scoped>
    td{
        padding: 5px;
    }
    td, input {
        width: 100%;
        box-sizing: border-box;
    }
    tr:not(.chosen):hover{
        background-color: #d4d4d4;
    }
</style>