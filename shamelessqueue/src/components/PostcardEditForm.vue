<template>
  <div class="postcard">
    <form v-on:submit.prevent="">
        recipient
        <label>first name<input v-model="recipient.firstname" type="text"></label>
        <label>last name <input v-model="recipient.lastname" type="text"></label>
        <label>street<input v-model="recipient.address" type="text"></label>
        <label>postcode<input v-model="recipient.postcode" type="text"> </label>
        <label>city<input v-model="recipient.city" type="text"></label>

        sender
        <label>first name <input v-model="sender.firstname" type="text"></label>
        <label>last name  <input v-model="sender.lastname" type="text"></label>
        <label>address <input v-model="sender.address" type="text"></label>
        <label>postcode <input v-model="sender.postcode" type="text"></label>
        <label>city <input v-model="sender.city" type="text"></label>

        <label>message
            <input v-model="message" type="text"></label>
        
        <button @click="save">save</button><button @click="cancel">cancel</button>
        <croppa v-model="postcardCroppa" :width="420" :height="298" :quality="4" :prevent-white-space="true"></croppa>
        <button @click="rotate">rotate</button>
    </form>
  </div>
</template>

<script>
import uniqid from 'uniqid'

export default {
	name: 'PostcardEditForm',
    props: ['postcard'],
    data() {
        var mydata = {
            postcardCroppa: {},
            id: uniqid(),
            recipient: {},
            posted: false,
            sender: {},
            message: null,
        }
        if (this.postcard) {
            Object.assign(mydata, this.postcard)
        }
        return mydata
    },
    methods: {
        saveNew() {

            this.$pouch.put({
                _id: this.id,
                sender: this.sender,
                recipient: this.recipient,
                message: this.message,
                posted: this.posted
            }).then((response) => {

                this.postcardCroppa.generateBlob(blob => {
                    this.$pouch.putAttachment(
                        this.id,
                        response.rev,
                        {id: 'postcard.jpeg', data: blob, type: 'image/jpeg'}).catch(() => {});
                }, 'image/jpeg',0.8);

            });
            

            this.$emit("editDone")
        },
        saveExisting {
            this.$pouch.put()
        },
        cancel() {
            this.$emit("editDone")
        },
        rotate() {
            var width = this.postcardCroppa.width
            var height = this.postcardCroppa.height
            this.postcardCroppa.width = height
            this.postcardCroppa.height = width

            //this.portrait = !this.portrait
        }
    }
}
</script>

<style scoped>
    form label {
        display: block;
    }
</style>
