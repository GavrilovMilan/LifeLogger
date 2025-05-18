<template>
    <div class="sidebar">
        <div class="logo">Logo here</div>
        <nav>
            <router-link to="/" class="menu-item">
                <span class="text">Dashboard</span>
            </router-link>
            <router-link to="/currencies" class="menu-item">
                <span class="text">Currencies</span>
            </router-link>
        </nav>
    </div>
</template>
<style scoped>
.sidebar {
  width: 150px;
  height: 100vh;
  background: #2c3e50;
  color: white;
  position: fixed;
  left: 0;
  top: 0;
  padding: 20px;
}
.logo {
  font-size: 1.5rem;
  font-weight: bold;
  margin-bottom: 30px;
  padding: 10px;
  border-bottom: 1px solid rgba(255, 255, 255, 0.2);
}
.menu-item {
  display: flex;
  align-items: center;
  padding: 12px 15px;
  margin: 5px 0;
  border-radius: 5px;
  color: white;
  text-decoration: none;
  transition: all 0.3s;
}
.menu-item:hover {
  background: #34495e;
}
.menu-item.router-link-exact-active {
  background: #42b983;
}
.icon {
  margin-right: 10px;
  font-size: 1.2rem;
}
.text {
  font-size: 1rem;
}
</style>