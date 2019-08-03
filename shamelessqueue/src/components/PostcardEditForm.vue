<template>
  <div class="postcard">
    <form v-on:submit.prevent="">
        recipient
        <label>first name<input v-model="p.recipient.firstname" type="text"></label>
        <label>last name <input v-model="p.recipient.lastname" type="text"></label>
        <label>street<input v-model="p.recipient.address" type="text"></label>
        <label>city<input v-model="p.recipient.city" type="text"></label>
        <label>postcode<input v-model="p.recipient.postcode" type="text"> </label>

        sender
        <label>first name <input v-model="p.sender.firstname" type="text"></label>
        <label>last name <input v-model="p.sender.lastname" type="text"></label>
        <label>address <input v-model="p.sender.address" type="text"></label>
        <label>city <input v-model="p.sender.city" type="text"></label>
        <label>postcode <input v-model="p.sender.postcode" type="text"></label>

        <label>message <input v-model="p.message" type="text"></label>
        
        <button @click="save">save</button><button @click="cancel">cancel</button>
    </form>
  </div>
</template>

<script>
export default {
	name: 'PostcardEditForm',
    props: ['postcard'],
    data() {
        return {
            p: this.postcard
        }
    },
    methods: {
        save() {
            this.$pouch.put(this.p).then(() => {});

            this.$emit("editDone")
        },
        cancel() {
            this.$emit("editDone")
        },
    }
}
</script>

<style scoped>
    form label {
        display: block;
    }
</style>
