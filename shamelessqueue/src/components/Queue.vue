<template>
  <div class="hello">
    <ul>
        <li v-for="postcard in postcards" v-bind:key="postcard._id">
            <PostcardPreview v-bind:postcard="postcard" v-if="currentEdit !== postcard" />
            <PostcardEditForm @editDone="editDone" v-if="currentEdit == postcard" :postcard="currentEdit"/>
            <button @click="remove(postcard)">delete</button>
            <button @click="edit(postcard)">edit</button>
        </li>
        <li>

            <PostcardEditForm @editDone="toggleNewPostcardForm" v-if="newPostcardForm" />
            <button @click="toggleNewPostcardForm">new</button>
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
            newPostcardForm: false,
            currentEdit: null
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
        toggleNewPostcardForm() {
            this.newPostcardForm = !this.newPostcardForm;
        },
        remove(postcard) {
            this.$pouch.remove(postcard);
        },
        edit(postcard) {
            this.currentEdit = postcard;
            this.newPostcardForm = false;
        },
        editDone() {
            this.currentEdit = null;
        }
    }
}
</script>

<style scoped>
</style>
