<template>
  <div id="app">
    <button @click="syncForm = true" v-if="!syncForm">sync</button>
    <Sync @editDone="editDone" v-if="syncForm" />
    <Queue />
  </div>
</template>

<script>
import Queue from './components/Queue.vue'
import Sync from './components/Sync.vue'

export default {
    name: 'app',
    data() {
        return {
            syncHandle: null,
            syncForm: false
        }
    },
    components: {
        Queue, Sync
    },
    created() {
        this.sync()
    },
    methods: {
        sync() {
            if(this.syncHandle) this.syncHandle.cancel()
            var database_auth = JSON.parse(window.localStorage.getItem('database_auth'))

            this.$pouch.connect(database_auth.username, database_auth.password, database_auth.couchdburl)
            this.syncHandle = this.$pouch.sync(database_auth.couchdburl).on('error', this.handleSyncError)

        },
        handleSyncError(event) {
            if(event && event.error == 'unauthorized') {
                this.sync()
            }
        },
        editDone() {
            this.syncForm = !this.syncForm
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
  color: #2c3e50;
  margin-top: 60px;
}
</style>
