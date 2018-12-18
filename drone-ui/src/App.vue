<template>
  <div id="app">
    <router-view/>
     <b-link to="/">Drones</b-link> | <b-link to="helloworld">User Mangement</b-link> 
  </div>
</template>

<script>
export default {
  name: 'App',
};
</script>

<style>
#app {
  margin-top: 60px;
}
</style>
