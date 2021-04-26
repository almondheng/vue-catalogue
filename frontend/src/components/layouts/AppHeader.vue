<template>
  <nav class="navbar navbar-expand-lg navbar-light bg-dark py-3">
    <div class="container-fluid">
      <span class="navbar-brand mb-0 h1 text-white">Product Catalogue</span>
      <div
        v-if="global.state.isLogin"
        class="d-flex"
      >
        <span class="align-self-center text-white px-3">{{ global.state.isStaff ? 'Admin' : 'User' }}</span>
        <button
          class="btn btn-outline-light"
          @click="onClickLogout"
        >
          Logout
        </button>
      </div>
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
