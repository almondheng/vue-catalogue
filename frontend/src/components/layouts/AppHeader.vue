<template>
  <nav class="navbar navbar-expand-lg navbar-light bg-dark py-3">
    <div class="container-fluid">
      <span class="navbar-brand mb-0 h1 text-white">Product Catalogue</span>
      <button v-if="global.state.isLogin" class="btn btn-outline-light d-flex" @click="onClickLogout">Logout</button>
    </div>
  </nav>
</template>

<script>
export default {
  name: 'AppHeader',
  inject: ['global'],
  methods: {
    onClickLogout(e) {
      e.preventDefault()
      this.global.logout()
      this.$router.push('/')
    }
  }
}
</script>
