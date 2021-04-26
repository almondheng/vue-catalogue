<template>
  <div class="container">
    <h1 class="display-4 my-4 my-md-5 text-center text-primary">
      Welcome to Vue Catalogue
    </h1>

    <div class="card mx-auto p-2 login">
      <div class="card-body">
        <h4 class="card-title mb-3">
          Login
        </h4>

        <form @submit="checkForm">
          <div class="mb-3">
            <label
              for="inputUsername"
              class="form-label"
            >Username</label>
            <input
              id="inputUsername"
              v-model="username"
              type="text"
              class="form-control"
            >
          </div>

          <div class="mb-3">
            <label
              for="inputPassword"
              class="form-label"
            >Password</label>
            <input
              id="inputPassword"
              v-model="password"
              type="password"
              class="form-control"
            >
          </div>

          <div
            v-if="errors.length"
            class="alert alert-warning alert-dismissible fade show"
            role="alert"
          >
            <b>Please correct the following error(s):</b>
            <ul>
              <li
                v-for="error in errors"
                :key="error"
              >
                {{ error }}
              </li>
            </ul>
            <button
              type="button"
              class="btn-close"
              data-bs-dismiss="alert"
              aria-label="Close"
              @click="errors = []"
            />
          </div>

          <button
            type="submit"
            class="btn btn-primary"
          >
            Submit
          </button>
        </form>
      </div>
    </div>
  </div>
</template>

<script>
import api from '@/api'

export default {
  inject: ['global'],
  data () {
    return {
      username: '',
      password: '',
      errors: []
    }
  },
  methods: {
    checkForm (e) {
      this.errors = []

      if (!this.username) {
        this.errors.push('Username required.')
      }
      if (!this.password) {
        this.errors.push('Password required.')
      }

      if (this.username && this.password) {
        const payload = {
          username: this.username,
          password: this.password
        }
        api.auth(payload)
          .then(res => {
            this.global.login(res.data)
            this.$router.push('/catalogue')
          })
          .catch(err => {
            this.errors.push('Login failed.')
            console.log(err)
          })
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
