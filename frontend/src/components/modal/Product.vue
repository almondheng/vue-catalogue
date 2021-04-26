<template>
  <div
    id="productModal"
    class="modal fade"
    data-bs-backdrop="static"
    data-bs-keyboard="false"
    tabindex="-1"
    aria-labelledby="productLabel"
    aria-hidden="true"
  >
    <div class="modal-dialog modal-dialog-centered">
      <div class="modal-content">
        <div class="modal-header">
          <h5
            id="productLabel"
            class="modal-title"
          >
            Product
          </h5>
          <button
            type="button"
            class="btn-close"
            data-bs-dismiss="modal"
            aria-label="Close"
          />
        </div>
        <div class="modal-body">
          <form>
            <div class="mb-3">
              <label
                for="inputName"
                class="form-label"
              >Name</label>
              <input
                id="inputName"
                v-model="product.name"
                type="text"
                class="form-control"
              >
            </div>
            <div class="mb-3">
              <label
                for="inputPrice"
                class="form-label"
              >Price</label>
              <input
                id="inputPrice"
                v-model="product.price"
                type="number"
                min="0"
                step="0.01"
                required
                class="form-control"
              >
            </div>
          </form>
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
            @click="onClickSave"
          >
            Save
          </button>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { ref, toRef, onMounted, watch } from 'vue'

export default {
  props: {
    selected: {
      type: Object,
      required: true
    }
  },
  emits: ['save'],
  setup (props) {
    const product = ref({})
    const selectedRef = toRef(props, 'selected')

    const getProduct = () => {
      product.value = {...selectedRef.value}
    }

    onMounted(getProduct)

    watch(selectedRef, getProduct)

    return {
      product,
      getProduct
    }
  },
  methods: {
    onClickSave (e) {
      if (this.product.name && this.product.price >= 0) {
        this.$emit('save', this.product) 
      }
      
      e.preventDefault()
    }
  }
}
</script>
