<template>
    <div>log the fuck in.
        <form v-on:submit.prevent="">
            <label>username:<input v-model="username" type="text"></label>
            <label>password:<input v-model="password" type="password"></label>
            <label>couchdb URL:<input v-model="couchdburl"></label>
            <button @click="save">save</button>
            <button @click="cancel">cancel</button>
        </form>
    </div>
</template>

<script>

export default {
	name: 'Sync',
    data() {
        var database_auth = {
            username: null,
            password: null,
            couchdburl: null
        }

        Object.assign(database_auth, JSON.parse(window.localStorage.getItem('database_auth')))

        return database_auth

    },
    methods: {
        save() {
            window.localStorage.setItem('database_auth', JSON.stringify({
                "username": this.username,
                "password": this.password,
                "couchdburl": this.couchdburl
            }))
            this.$emit("editDone", this.database_auth)
        },
        cancel() {
            this.$emit("editDone")
        }
    }
}
</script>

<style scoped>
    form label {
        display: block;
    }
</style>
