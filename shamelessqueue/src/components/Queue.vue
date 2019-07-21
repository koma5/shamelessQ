<template>
  <div class="hello">
    <ul>
        <li v-for="postcard in postcards" v-bind:key="postcard._id">
            <PostcardPreview v-bind:postcard="postcard"/>
        </li>
        <li>
            <PostcardEditForm v-if="newPostcard" />
            <button @click="createNewPostcard">new</button>
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
        createNewPostcard() {
            //this.newPostcard = {"_id": uniqid(), sender: {}, recipient: {}}
            this.newPostcard = true;

            /*this.$pouch.put(newPostcard).then(() => {
                this.currentEdit = this.postcards.find(p => p._id === newPostcard._id )
            })*/
        }
    }
}
</script>

<style scoped>
</style>
