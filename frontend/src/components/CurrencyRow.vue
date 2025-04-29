<script setup>
    import { ref } from 'vue';

    const props = defineProps({
        currency:Object
    })
</script>

<template>
    <tr>
        <td>{{ currency.ref_currency_id }}</td>
        <td>{{ currency.name }}</td>
        <td>{{ currency.short_name }}</td>
        <td>{{ currency.user_inserted }}</td>
        <td>{{ currency.created_at }}</td>
        <td>{{ currency.user_updated }}</td>
        <td>{{ currency.updated_at }}</td>
    </tr>
</template>

<style scoped>
    td{
        padding-left: 5px;
    }
    td, input {
        width: 100%;
        box-sizing: border-box;
    }
    tr:not(.izabran):hover{
        background-color: #d4d4d4;
    }
</style>