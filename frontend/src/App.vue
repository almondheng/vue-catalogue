<template>
  <app-header />
  <router-view />
  <app-footer />
</template>

<script setup>
import { useRouter } from 'vue-router'
import AppHeader from '@/components/layouts/AppHeader.vue'
import AppFooter from '@/components/layouts/AppFooter.vue'
import global from './global'

const router = useRouter()
global.inspectToken().then(res => res ? router.push('/catalogue') : router.push('/'))

// This starter template is using Vue 3 experimental <script setup> SFCs
// Check out https://github.com/vuejs/rfcs/blob/script-setup-2/active-rfcs/0000-script-setup.md
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  color: #2c3e50;
  margin-bottom: 150px;
}
</style>
