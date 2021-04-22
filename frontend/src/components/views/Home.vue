<template>
  <div class="container">
    <h1 class="display-4 my-4 my-md-5 text-center text-primary">Welcome to Vue Catalogue</h1>

    <div class="card mx-auto p-2 login">
      <div class="card-body">
        <h4 class="card-title mb-3">Login</h4>

        <form @submit="checkForm">
          <div class="mb-3">
            <label for="inputEmail" class="form-label">Email address</label>
            <input type="email" class="form-control" id="inputEmail" aria-describedby="emailHelp" v-model="email">
            <div id="emailHelp" class="form-text">We'll never share your email with anyone else.</div>
          </div>

          <div class="mb-3">
            <label for="inputPassword" class="form-label">Password</label>
            <input type="password" class="form-control" id="inputPassword" v-model="password">
          </div>

          <div class="alert alert-warning alert-dismissible fade show" role="alert" v-if="errors.length">
            <b>Please correct the following error(s):</b>
            <ul>
              <li v-for="error in errors" :key="error">{{ error }}</li>
            </ul>
            <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close" @click="errors = []"></button>
          </div>

          <button type="submit" class="btn btn-primary">Submit</button>
        </form>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  data () {
    return {
      email: '',
      password: '',
      errors: []
    }
  },
  methods: {
    checkForm (e) {
      this.$router.push('/catalogue')
      if (this.email && this.password) {
        return true
      }

      this.errors = []

      if (!this.email) {
        this.errors.push('Email required.')
      }
      if (!this.password) {
        this.errors.push('Password required.')
      }

      e.preventDefault()
    }
  }
}
</script>

<style scoped>
@media only screen and (min-width: 768px) {
  .login {
    max-width: 50%;
    padding: 1.5rem !important;
  }
}
</style>
