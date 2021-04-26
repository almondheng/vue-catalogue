<template>
  <div
    id="popupModal"
    class="modal fade"
    data-bs-backdrop="static"
    data-bs-keyboard="false"
    tabindex="-1"
    aria-labelledby="popupLabel"
    aria-hidden="true"
  >
    <div class="modal-dialog modal-dialog-centered">
      <div class="modal-content">
        <div class="modal-header">
          <h5
            id="popupLabel"
            class="modal-title"
          >
            {{ title }}
          </h5>
          <button
            type="button"
            class="btn-close"
            data-bs-dismiss="modal"
            aria-label="Close"
          />
        </div>
        <div class="modal-body">
          <p>{{ message }} {{ selected.name }}</p>
        </div>
        <div class="modal-footer">
          <button
            type="button"
            class="btn btn-secondary"
            data-bs-dismiss="modal"
          >
            Cancel
          </button>
          <button
            type="button"
            class="btn btn-primary"
            @click="onClickConfirm"
          >
            Confirm
          </button>
        </div>
      </div>
    </div>
  </div>
</template>

<script>

export default {
  props: {
    title: {
      type: String,
      default: 'Popup'
    },
    message: {
      type: String,
      default: 'Are you sure?'
    },
    selected: {
      type: Object,
      required: true
    },
  },
  emits: ['confirm'],
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
