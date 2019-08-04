<template>
  <section class="postcard" @click="flipBackside()">
    <img @load="checkPortrait($event)" v-if="img && !backside" v-bind:src="img" alt="postcard" :class="{forcelandscape: isPortrait}">
    <p v-if="backside">{{ postcard }}</p>
  </section>
</template>

<script>
export default {
	name: 'PostcardPreview',
    props: ['postcard'],
    data() {
        return {
            img: null,
            isPortrait: false,
            backside: false
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
        },
        flipBackside() {
            this.backside = !this.backside;
        }
    }
    
}
</script>

<style>
section.postcard {
    width: 500px;
    height: 354.75px;
}
img {
    width:500px;
}

img.forcelandscape {
    transform: rotate(-90deg);
    height:500px;
    width: unset;
    position: relative;
    top: 354.75px;
    top: -72.625px; /* (500-354.75)/2 */
}
</style>
