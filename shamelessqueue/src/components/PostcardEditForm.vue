<template>
  <div class="postcard">
    <form v-on:submit.prevent="save">
        <label>first name<input v-model="recipient.firstname" type="text"></label>
        <label>last name <input v-model="recipient.lastname" type="text"></label>
        <label>street<input v-model="recipient.address" type="text"></label>
        <label>city<input v-model="recipient.city" type="text"></label>
        <label>postcode<input v-model="recipient.postcode" type="text"> </label>

        <label>first name
            <input v-model="sender.firstname" type="text"></label>
        <label>last name
            <input v-model="sender.lastname" type="text"></label>
        <label>address name
            <input v-model="sender.address" type="text"></label>
        <label>city name
            <input v-model="sender.city" type="text"></label>
        <label>postcode name
            <input v-model="sender.postcode" type="text"></label>

        <label>message
            <input v-model="message" type="text"></label>
        
        <label>picture
            <input @change="fileSelected($event)" type="file"></label>

        <button>save</button>
        <croppa v-model="postcardCroppa"></croppa>
    </form>
  </div>
</template>

<script>
import uniqid from 'uniqid'

export default {
	name: 'PostcardEditForm',
    props: ['postcard'],
    data() {
        return {
            //if porp unpack
            //"_id": uniqid(),
            postcardCroppa: {},
            id: uniqid(),
            recipient: {},
            sender: {},
            message: null,
        }
    },
    methods: {
        fileSelected(event) {
            var file = event.target.files[0]


        },
        save() {

            this.$pouch.put({
                _id: this.id,
                sender: this.sender,
                recipient: this.recipient,
                message: this.message,
            }).then((response) => {

                this.postcardCroppa.generateBlob(blob => {
                    this.$pouch.putAttachment(
                        this.id,
                        response.rev,
                        {id: 'postcard.jpeg', data: blob, type: 'image/jpeg'}).catch(function (err) {});
                }, 'image/jpeg',0.8);

            });
            

           //put doc
            //put attachment 
            //emit done

            /* //!!pulled my hair out for this: this.$pouch.putAttachment(
                'jyctrxn2',
                '3-ef6e708a1a12569de9985c30c5ab26be',
                {id: file.name, data: file, type: file.type}).catch(function (err) {});
            */

        }
    }
}
</script>

<style scoped>
    form label {
        display: block;
    }
</style>
