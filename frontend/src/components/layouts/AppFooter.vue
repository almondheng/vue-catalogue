<template>
  <footer>
    <div class="container text-center">
      <a class="link-primary" href="https://github.com/almondheng/vue-catalogue">Github Repo</a>
      <span>by Almond Heng</span>
    </div>
  </footer>
</template>

<script>
export default {
  name: 'AppFooter'
}
</script>

<style scoped>
footer {
  display: block;
  position: absolute;
  bottom: 0;
  width: 100%;
  height: 60px;
  line-height: 60px;
  background-color: #f5f5f5;
  font-size: 0.8rem;
}
</style>
