<template>
  <div class="hello">
    <ul>
        <li v-for="postcard in postcards">
            <PostcardPreview v-bind:postcard="postcard"/>
        </li>
        <li>
            <PostcardEditForm v-bind:postcard="newPostcard" />
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
            newPostcard: {
                recipient: {},
                sender: {},
            },
        }
    },
    pouch: {
        postcards: {}
    },
    created() {
        this.$pouch.sync('postcards', 'http://127.0.0.1:5984/postcards')
    }, 
    components: {
        PostcardPreview,
        PostcardEditForm
    }
}
</script>

<style scoped>
</style>
