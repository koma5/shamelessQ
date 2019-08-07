<template>
  <div>
    <ul id="queue">
        <draggable v-model="postcards" group="postcards" @start="drag=true" @end="drag=false" @change="orderChange($event)">
            <li v-for="postcard in postcards" v-bind:key="postcard._id">
                <PostcardPreview v-bind:postcard="postcard" v-if="currentEdit !== postcard"/>
                <PostcardEditForm v-bind:postcard="currentEdit" v-if="currentEdit == postcard" @editDone="toggleEdit"/>

                <button @click="remove(postcard)" v-if="currentEdit !== postcard">delete</button>
                <button @click="toggleEdit(postcard)" v-if="currentEdit !== postcard">edit</button>
            </li>
        </draggable>
        <li>
            <PostcardEditForm @editDone="toggleNewPostcard" v-if="newPostcard" :lastPostcardOrder="lastPostcardOrder"/>
            <button @click="toggleNewPostcard">new</button>
        </li>
    </ul>
  </div>
</template>

<script>
import PostcardPreview from './PostcardPreview.vue'
import PostcardEditForm from './PostcardEditForm.vue'
import draggable from 'vuedraggable'
import mudder from 'mudder'

export default {
	name: 'Queue',
    data() {
        return {
            newPostcard: false,
            currentEdit: null
        }
    },
    pouch: {
        postcards() {
            return {
                selector: { posted: false },
                sort: [{"order": "asc"}]
            }
        }
    },
    components: {
        PostcardPreview,
        PostcardEditForm,
        draggable,
    },
    computed: {
        lastPostcardOrder: {
            get: function() {
                if (this.postcards.length > 0) {
                    return this.postcards[this.postcards.length -1].order
                }
                else {
                    return 'a'
                }
            }
        }
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
        },
        orderChange(event) {
            if(event.moved) {
                var element = event.moved.element
                var newIndex = event.moved.newIndex
                var postcardOrderBefore = (this.postcards[newIndex-1]) ? this.postcards[newIndex-1].order : 'a'
                var postcardOrderAfter =  (this.postcards[newIndex+1]) ? this.postcards[newIndex+1].order : 'z'
                var newOrder = mudder.alphabet.mudder(postcardOrderBefore, postcardOrderAfter, 1)
                element.order = newOrder[0]
                this.$pouch.put(element)
            }
        }
    }
}
</script>

<style>
ul#queue {
    list-style-type: none;
}

</style>
