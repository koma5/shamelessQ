<template>
  <div class="postcard">
    <img v-bind:src="getImgUrl()" alt="">
    {{ postcard }}
  </div>
</template>

<script>
export default {
	name: 'PostcardPreview',
    props: ['postcard'],
    mounted() {
    },
    methods: {
        /*getAttachment() {
            this.$pouch.getAttachment(this.postcard._id, '922-536x354.jpg').then((response) => { this.postcard.img = response })
        }*/
        getImgUrl() {
            if (this.postcard._attachments) {
                return 'http://127.0.0.1:5984/postcards/' + this.postcard._id + '/' + Object.keys(this.postcard._attachments)[0]
            }
            else {
                return null
            }
        }
    }
}
</script>

<style scoped>
</style>
