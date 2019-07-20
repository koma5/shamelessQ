<template>
  <div class="postcard">
    <form>
        <label>first name<input v-model="postcard.recipient.firstname" type="text"></label>
        <label>last name <input v-model="postcard.recipient.lastname" type="text"></label>
        <label>street<input v-model="postcard.recipient.address" type="text"></label>
        <label>city<input v-model="postcard.recipient.city" type="text"></label>
        <label>postcode<input v-model="postcard.recipient.postcode" type="text"> </label>

        <label>first name
            <input v-model="postcard.sender.firstname" type="text"></label>
        <label>last name
            <input v-model="postcard.sender.lastname" type="text"></label>
        <label>address name
            <input v-model="postcard.sender.address" type="text"></label>
        <label>city name
            <input v-model="postcard.sender.city" type="text"></label>
        <label>postcode name
            <input v-model="postcard.sender.postcode" type="text"></label>

        <label>message
            <input v-model="postcard.message" type="text"></label>

    </form>
  </div>
</template>

<script>
export default {
	name: 'PostcardEditForm',
    props: ['postcard'],
    mounted() {
    },
    methods: {
    }
}
</script>

<style scoped>
    form label {
        display: block;
    }
</style>
