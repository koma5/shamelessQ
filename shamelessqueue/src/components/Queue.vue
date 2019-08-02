<template>
  <div class="hello">
    <ul>
        <li v-for="postcard in postcards" v-bind:key="postcard._id">
            <PostcardPreview v-bind:postcard="postcard" v-if="currentEdit !== postcard" />
            <button @click="remove(postcard)">delete</button>
            <button @click="edit(postcard)">edit</button>
        </li>
        <li>
            <PostcardEditForm @editDone="toggleEditForm" v-if="editForm" postcard="currentEdit"/>
            <button @click="toggleEditForm">new</button>
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
            editForm: false,
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
        toggleEditForm() {
            this.editForm = !this.editForm;
        },
        remove(postcard) {
            this.$pouch.remove(postcard);
        },
        edit(postcard) {
            this.currentEdit = postcard;
            this.toggleEditForm();
        }
    }
}
</script>

<style scoped>
</style>
