<template>
  <div id="app">
    <button @click="loginForm = true" v-if="!loginForm">login</button>
    <Login @editDone="editDone" v-if="loginForm" />
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
            syncHandle: null,
            loginForm: false
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

            this.$pouch.connect(database_auth.username, database_auth.password, database_auth.couchdburl)
            this.syncHandle = this.$pouch.sync(database_auth.couchdburl)

        },
        editDone() {
            this.loginForm = !this.loginForm
            this.sync()
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
