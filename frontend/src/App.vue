<script setup>
	import CurrencyTable from './components/CurrencyTable.vue';
</script>
<template>
	<div class="container">
		<div class="section">
			<CurrencyTable>
			</CurrencyTable>
		</div>
	</div>
</template>
<style scoped>
.container {
	display: flex;
	justify-content: space-between;
}
.section {
	border: 3px solid black;
	padding: 10px;
	flex: 1;
	margin-right: 10px;
}
/* .section:first-child {
	flex: 0 0 35%;
}*/
.section:last-child {
	margin-right: 0;
} 
</style>
