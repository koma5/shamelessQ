<template>
  <section class="postcard" @click="flipBackside()">
    <img @load="checkPortrait($event)" v-show="img && !backside" v-bind:src="img" alt="postcard" :class="{forcelandscape: isPortrait}">

    <section class="backside" v-show="backside">
        <p class="message">{{ postcard.message }}</p>

        <address class="sender">
            {{postcard.sender.company}} {{ postcard.sender.firstname }} {{ postcard.sender.lastname }},
            {{ postcard.sender.address }},
            {{ postcard.sender.postcode }} {{ postcard.sender.city }}
        </address>

        <address class="recipient">
            {{ postcard.recipient.company }} <br>
            {{ postcard.recipient.company_addition }} <br>
            {{ postcard.recipient.salutation }} {{ postcard.recipient.firstname }} {{ postcard.recipient.lastname }} <br>
            {{ postcard.recipient.address }} <br>
            {{ postcard.recipient.postcode }} {{ postcard.recipient.city }} <br>
        </address>

        <div class="buttons">
            <button @click.stop="sendRemove()" v-show="deletePresses == 0">delete</button>
            <button @click="sendRemove()" v-show="deletePresses > 0" class="confirmDelete">really delete?</button>
            <button @click="sendEdit()">edit</button>
        </div>


    </section>

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
            backside: false,
            deletePresses: 0
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
            this.deletePresses = 0;
        },
        sendEdit() {
            this.$emit('edit');
        },
        sendRemove() {
            if (this.deletePresses > 0) {
                this.$emit('remove');
            }
            else {
                this.deletePresses++;
            }
        },
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
section.postcard address, p.message {
    font-style: normal;
    text-align: left;
}

p.message {
    word-break: break-all;
}

address.sender {
    grid-area: sender;
    font-size: 0.75em;
    align-items: flex-end;
}

address.recipient {
    grid-area: recipient;
}

div.buttons {
    grid-area: buttons;
}

button.confirmDelete {
    background-color: #f55a42;
    color: white;
}

section.backside {
    width: 460px;
    height: 314.75px;
    border: 0.25px lightgray solid;
    padding: 20px;
    display: grid;
    grid-template-columns: 3fr 4fr;
    grid-template-rows: 0.9fr 0.2fr 1.9fr;
    grid-gap: 10px;
    grid-template-areas: "message buttons"
                         "message sender"
                         "message recipient";
}
</style>
