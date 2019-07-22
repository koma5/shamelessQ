<template>
  <div class="hello">
    <ul>
        <li v-for="postcard in postcards" v-bind:key="postcard._id">
            <PostcardPreview v-bind:postcard="postcard"/>
        </li>
        <li>
            <PostcardEditForm @editDone="toggleEdit" v-if="newPostcard" />
            <button @click="toggleEdit">new</button>
        </li>
    </ul>
  </div>
</template>

<script>
import PostcardPreview from './PostcardPreview.vue'
import PostcardEditForm from './PostcardEditForm.vue'

export default {
	name: 'Queue',
    data() {
        return {
            newPostcard: false,
            database_auth: JSON.parse(window.localStorage.getItem('database_auth'))
        }
    },
    pouch: {
        postcards: { posted: false }
    },
    created() {
        this.$pouch.sync('http://' + this.database_auth.username + ':' + this.database_auth.password + '@127.0.0.1:5984/postcards')
    }, 
    components: {
        PostcardPreview,
        PostcardEditForm
    },
    methods: {
        toggleEdit() {
            this.newPostcard = !this.newPostcard;
        },
    }
}
</script>

<style scoped>
</style>
