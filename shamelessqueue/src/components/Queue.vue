<template>
  <div class="hello">
    <ul v-for="postcard in postcards">
        <li>{{ postcard }}ii</li>
    </ul>
  </div>
</template>

<script>
export default {
	name: 'Queue',
    pouch: {
        postcards: {}
    },
    created() {
        this.$pouch.sync('postcards', 'http://127.0.0.1:5984/postcards')
    }, 
}
</script>

<style scoped>
</style>
