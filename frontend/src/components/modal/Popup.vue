<template>
  <div class="modal fade" id="popupModal" data-bs-backdrop="static" data-bs-keyboard="false" tabindex="-1" aria-labelledby="popupLabel" aria-hidden="true">
    <div class="modal-dialog modal-dialog-centered">
      <div class="modal-content">
        <div class="modal-header">
          <h5 class="modal-title" id="popupLabel">{{title}}</h5>
          <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
        </div>
        <div class="modal-body">
          <p>{{message}} {{selected.name}}</p>
        </div>
        <div class="modal-footer">
          <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Cancel</button>
          <button type="button" @click="onClickConfirm" class="btn btn-primary">Confirm</button>
        </div>
      </div>
    </div>
  </div>
</template>

<script>

export default {
  props: {
    title: String,
    message: String,
    selected: Object
  },
  methods: {
    onClickConfirm (e) {
      if (this.selected) {
        this.$emit('confirm')
      }
      e.preventDefault()
    }
  }
}
</script>
