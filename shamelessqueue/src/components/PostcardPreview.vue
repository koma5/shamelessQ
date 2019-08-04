<template>
  <div class="postcard">
    <img @load="checkPortrait($event)" v-if="img" v-bind:src="img" alt="postcard" :class="{forcelandscape: isPortrait}">
    {{ postcard }}
  </div>
</template>

<script>
export default {
	name: 'PostcardPreview',
    props: ['postcard'],
    data() {
        return {
            img: null,
            isPortrait: false
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
        },
        checkPortrait(event) {
            var image = event.target
            this.isPortrait = image.naturalWidth < image.naturalHeight
        }
    }
    
}
</script>

<style scoped>
img {
    width:500px;
}
img.forcelandscape {
    transform: rotate(90deg);
    height:500px;
    width: unset;
}
</style>
