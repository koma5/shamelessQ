<template>
  <div id="app">
    <Login @editDone="sync" />
    <Queue />
  </div>
</template>

<script>
import Queue from './components/Queue.vue'
import Login from './components/Login.vue'

export default {
    name: 'app',
    data() {
        return {
            syncHandle: null
        }
    },
    components: {
        Queue, Login
    },
    created() {
        this.sync()
    },
    methods: {
        sync() {
            if(this.syncHandle) this.syncHandle.cancel()
            var database_auth = JSON.parse(window.localStorage.getItem('database_auth'))
            this.syncHandle = this.$pouch.sync('http://' + database_auth.username + ':' + database_auth.password + '@' + database_auth.couchdburl.replace('http://', ''))
        }
    }
}
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
