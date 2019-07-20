<template>
  <div class="hello">
    <ul v-for="postcard in postcards">
        <li>
            <PostcardPreview v-bind:postcard="postcard"/>
        </li>
    </ul>
  </div>
</template>

<script>
import PostcardPreview from './PostcardPreview.vue'

export default {
	name: 'Queue',
    data() {
        return {
            newPostcard: false
        }
    },
    pouch: {
        postcards: {}
    },
    created() {
        this.$pouch.sync('postcards', 'http://127.0.0.1:5984/postcards')
    }, 
    components: {
        PostcardPreview
    }
}
</script>

<style scoped>
</style>
