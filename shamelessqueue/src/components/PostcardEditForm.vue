<template>
  <div class="postcard">
    <form v-on:submit.prevent="">
        recipient
        <label>company <input v-model="p.recipient.company" type="text"></label>
        <label>company addition<input v-model="p.recipient.company_addition" type="text"></label>
        <label>salutation<input v-model="p.recipient.salutation" type="text"></label>
        <label>first name<input v-model="p.recipient.firstname" type="text"></label>
        <label>last name <input v-model="p.recipient.lastname" type="text"></label>
        <label>street<input v-model="p.recipient.address" type="text"></label>
        <label>postcode<input v-model="p.recipient.postcode" type="text"> </label>
        <label>city<input v-model="p.recipient.city" type="text"></label>

        sender
        <label>company <input v-model="p.sender.company" type="text"></label>
        <label>first name <input v-model="p.sender.firstname" type="text"></label>
        <label>last name <input v-model="p.sender.lastname" type="text"></label>
        <label>address <input v-model="p.sender.address" type="text"></label>
        <label>postcode <input v-model="p.sender.postcode" type="text"></label>
        <label>city <input v-model="p.sender.city" type="text"></label>

        <label>message <input v-model="p.message" type="text"></label>

        <button @click="saveNew" v-if="!postcard">save</button>
        <button @click="saveExisting" v-if="postcard">save</button>

        <button @click="cancel">cancel</button>

        <croppa v-if="!postcard" v-model="postcardCroppa" v-bind:width="postcardCroppa.width" v-bind:height="postcardCroppa.height" :quality="4" :prevent-white-space="true"></croppa>
        <button v-if="!postcard" @click="rotate">rotate</button>
    </form>
  </div>
</template>

<script>
import uniqid from 'uniqid'
import mudder from 'mudder'

export default {
	name: 'PostcardNewForm',
    props: ['postcard', 'lastPostcardOrder'],
    data() {
        var mydata = {
            postcardCroppa: {
                width: 455,
                height: 328
            },
            p: {
                _id: uniqid(),
                recipient: {},
                sender: {},
                message: '',
                posted: false,
                order: mudder.alphabet.mudder(this.lastPostcardOrder, 'z', 100)[0]
            }
        }
        if (this.postcard) {
           Object.assign(mydata.p, this.postcard) 
        }
        return mydata
    },
    methods: {
        saveNew() {

            this.$pouch.put({
                _id: this.p._id,
                posted: this.p.posted,
                sender: this.p.sender,
                recipient: this.p.recipient,
                message: this.p.message,
                order: this.p.order
            }).then((response) => {

                this.postcardCroppa.generateBlob(blob => {
                    this.$pouch.putAttachment(
                        this.p._id,
                        response.rev,
                        {id: 'postcard.jpeg', data: blob, type: 'image/jpeg'}).catch(() => {});
                }, 'image/jpeg',0.8);

            });

            this.$emit("editDone")
        },
        saveExisting() {
            this.$pouch.put(this.p).then(() => {});

            this.$emit("editDone")
        },
        cancel() {
            this.$emit("editDone")
        },
        rotate() {
            var width = this.postcardCroppa.width
            var height = this.postcardCroppa.height
            this.postcardCroppa.width = height
            this.postcardCroppa.height = width
        }
    }
}
</script>

<style scoped>
    form label {
        display: block;
    }
</style>
