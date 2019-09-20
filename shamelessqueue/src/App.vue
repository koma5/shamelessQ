<template>
  <div id="app">
    <button @click="syncForm = true" v-if="!syncForm">sync</button>
    <button v-if="updateExists" @click="refreshApp">
        New version avaiiliable! Click to update
    </button>
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
            syncForm: false,
            refreshing: false,
            registration: null,
            updateExists: false
        }
    },
    components: {
        Queue, Sync
    },
    created() {

        document.addEventListener(
            'swUpdated', this.showRefreshUI, { once: true }
        );
        navigator.serviceWorker.addEventListener(
            'controllerchange', () => {
                if (this.refreshing) return;
                this.refreshing = true;
                window.location.reload();
            }
        );

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
        },
        showRefreshUI(e) {
            this.registration = e.detail;
            this.updateExists = true;
        },
        refreshApp() {
            this.updateExists = false;  if (!this.registration || !this.registration.waiting) { return; }
            this.registration.waiting.postMessage('skipWaiting');
        },
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
    text-align:center;
}
button {
    height: 40px;
    background-color: lightgray;
    border:none;
    margin-right: 10px;
    font-size: 1.2em;
}
</style>
