<template>
  <div class="hello">
    <ul>
        <li v-for="postcard in postcards" v-bind:key="postcard._id">
            <PostcardPreview v-bind:postcard="postcard"/>
        </li>
        <li>
            <PostcardEditForm v-if="currentEdit" v-bind:postcard="currentEdit" />
            <button @click="newPostcard">new</button>
        </li>
    </ul>
  </div>
</template>

<script>
import PostcardPreview from './PostcardPreview.vue'
import PostcardEditForm from './PostcardEditForm.vue'
import uniqid from 'uniqid'

export default {
	name: 'Queue',
    data() {
        return {
            currentEdit: false,
        }
    },
    pouch: {
        postcards: {}
    },
    created() {
        this.$pouch.sync('http://127.0.0.1:5984/postcards')
    }, 
    components: {
        PostcardPreview,
        PostcardEditForm
    },
    methods: {
        newPostcard() {
            var newPostcard = {"_id": uniqid(), sender: {}, recipient: {}}
            this.$pouch.put(newPostcard)
            this.currentEdit = newPostcard;
        }
    }
}
</script>

<style scoped>
</style>
