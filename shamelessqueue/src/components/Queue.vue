<template>
  <div class="hello">
    <ul>
        <li v-for="postcard in postcards" v-bind:key="postcard._id">
            <PostcardPreview v-bind:postcard="postcard" v-if="currentEdit !== postcard"/>
            <PostcardEditForm v-bind:postcard="currentEdit" v-if="currentEdit == postcard" @editDone="toggleEdit"/>

            <button @click="remove(postcard)" v-if="currentEdit !== postcard">delete</button>
            <button @click="toggleEdit(postcard)" v-if="currentEdit !== postcard">edit</button>
        </li>
        <li>
            <PostcardNewForm @editDone="toggleNewPostcard" v-if="newPostcard" />
            <button @click="toggleNewPostcard">new</button>
        </li>
    </ul>
  </div>
</template>

<script>
import PostcardPreview from './PostcardPreview.vue'
import PostcardEditForm from './PostcardEditForm.vue'
import PostcardNewForm from './PostcardNewForm.vue'

export default {
	name: 'Queue',
    data() {
        return {
            newPostcard: false,
            currentEdit: null
        }
    },
    pouch: {
        postcards: { posted: false }
    },
    components: {
        PostcardPreview,
        PostcardEditForm,
        PostcardNewForm
    },
    methods: {
        toggleNewPostcard() {
            this.newPostcard = !this.newPostcard;
        },
        remove(postcard) {
            this.$pouch.remove(postcard);
        },
        toggleEdit(postcard) {
            if(postcard) {
                this.currentEdit = postcard
            }
            else {
                this.currentEdit = null
            }
        }
    }
}
</script>

<style scoped>
</style>
