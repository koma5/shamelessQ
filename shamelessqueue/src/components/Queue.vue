<template>
  <div class="hello">
    <ul>
        <li v-for="postcard in postcards" v-bind:key="postcard._id">
            <PostcardPreview v-bind:postcard="postcard"/>
            <button @click="remove(postcard)">delete</button>
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
        }
    },
    pouch: {
        postcards: { posted: false }
    },
    components: {
        PostcardPreview,
        PostcardEditForm
    },
    methods: {
        toggleEdit() {
            this.newPostcard = !this.newPostcard;
        },
        remove(postcard) {
            this.$pouch.remove(postcard);
        }
    }
}
</script>

<style scoped>
</style>
