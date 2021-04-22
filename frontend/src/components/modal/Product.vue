<template>
  <div class="modal fade" id="productModal" data-bs-backdrop="static" data-bs-keyboard="false" tabindex="-1" aria-labelledby="productLabel" aria-hidden="true">
    <div class="modal-dialog modal-dialog-centered">
      <div class="modal-content">
        <div class="modal-header">
          <h5 class="modal-title" id="productLabel">Product</h5>
          <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
        </div>
        <div class="modal-body">
          <form>
            <div class="mb-3">
              <label for="inputName" class="form-label">Name</label>
              <input type="text" v-model="product.name" class="form-control" id="inputName">
            </div>
            <div class="mb-3">
              <label for="inputPrice" class="form-label">Price</label>
              <input type="number" min="0" step="0.01" required v-model="product.price" class="form-control" id="inputPrice">
            </div>
          </form>
        </div>
        <div class="modal-footer">
          <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Cancel</button>
          <button type="button" @click="onClickSave" class="btn btn-primary">Save</button>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { ref, toRef, onMounted, watch } from 'vue'

export default {
  props: {
    selected: Object
  },
  setup (props) {
    const product = ref({})
    const selectedRef = toRef(props, 'selected')

    const getProduct = () => {
      product.value = selectedRef.value
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
        const {id, ...input} = this.product
        this.$emit('save', id ? this.product : input) // omit id if not exist
      }
      
      e.preventDefault()
    }
  }
}
</script>
