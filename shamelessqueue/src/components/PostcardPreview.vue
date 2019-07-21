<template>
  <div class="postcard">
    <img v-if="img" v-bind:src="img" alt="">
    {{ postcard }}
  </div>
</template>

<script>
export default {
	name: 'PostcardPreview',
    props: ['postcard'],
    data() {
        return {
            img: null
        }
    },
    mounted() {
        this.getAttachment()
    },
    updated() {
        this.getAttachment()
    },
    methods: {
        getAttachment() {
            if(this.postcard._attachments && this.img == null) {
                this.$pouch.getAttachment(
                    this.postcard._id,
                    Object.keys(this.postcard._attachments)[0])
                    .then((blob) => {
                        this.img = URL.createObjectURL(blob)
                    })
            }
        }
    }
    
}
</script>

<style scoped>
img {
    width:500px;
}
</style>
