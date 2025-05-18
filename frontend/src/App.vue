<script setup>
	import CurrencyTable from './components/CurrencyTable.vue';
	import Sidebar from './components/Sidebar.vue';
</script>
<template>
	<div class="app-container">
		<Sidebar />
		<div class="main-content">
			<router-view />
		</div>
	</div>
	<!-- <div class="container">
		<div class="section">
			<CurrencyTable>
			</CurrencyTable>
		</div>
	</div> -->
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
.section:last-child {
	margin-right: 0;
} 

.app-container {
  display: flex;
  min-height: 100vh;
}
.main-content {
  flex: 1;
  margin-left: 170px; /* Same as sidebar width */
  padding: 20px;
}
body {
  margin: 0;
}
</style>
