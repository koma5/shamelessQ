<template>
  <div class="postcard">
    <img v-bind:src="getImgUrl()" alt="">
    <p> {{  }}</p>
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
            return 'http://127.0.0.1:5984/postcards/' + this.postcard._id + '/' + Object.keys(this.postcard._attachments)[0]
        }
    }
}
</script>

<style scoped>
</style>
