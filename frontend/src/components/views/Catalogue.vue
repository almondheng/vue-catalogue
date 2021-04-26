<template>
  <div class="container">
    <div class="d-flex justify-content-between align-items-center">
      <h1 class="my-4 my-md-5">
        Catalogue
      </h1>
      <div class="p-2">
        <button
          v-if="global.state.isStaff"
          type="button"
          class="btn btn-outline-success"
          data-bs-toggle="modal"
          data-bs-target="#productModal"
          @click="getSelected()"
        >
          Add Product
        </button>
      </div>
    </div>

    <!-- Modal -->
    <product
      ref="product"
      :selected="selected"
      @save="onSave"
    />
    <popup
      ref="popup"
      title="Are you sure?"
      message="This action will delete"
      :selected="selected"
      @confirm="onDelete"
    />

    <div class="table-responsive">
      <table class="table table-dark table-striped">
        <thead>
          <tr>
            <th scope="col">
              #
            </th>
            <th scope="col">
              Product
            </th>
            <th scope="col">
              Price
            </th>
            <th
              v-if="global.state.isStaff"
              scope="col"
              class="text-center"
            >
              Action
            </th>
          </tr>
        </thead>
        <tbody>
          <tr
            v-for="(product, index) in products.results"
            :key="product.id"
          >
            <th scope="row">
              {{ (page-1)*10+index+1 }}
            </th>
            <td>{{ product.name }}</td>
            <td>$ {{ product.price }}</td>
            <td
              v-if="global.state.isStaff"
              class="text-center"
            >
              <svg
                role="button"
                data-bs-toggle="modal"
                data-bs-target="#productModal"
                xmlns="http://www.w3.org/2000/svg"
                width="16"
                height="16"
                fill="currentColor"
                class="bi bi-pencil-square"
                viewBox="0 0 16 16"
                @click="getSelected(product)"
              >
                <path d="M15.502 1.94a.5.5 0 0 1 0 .706L14.459 3.69l-2-2L13.502.646a.5.5 0 0 1 .707 0l1.293 1.293zm-1.75 2.456-2-2L4.939 9.21a.5.5 0 0 0-.121.196l-.805 2.414a.25.25 0 0 0 .316.316l2.414-.805a.5.5 0 0 0 .196-.12l6.813-6.814z" />
                <path
                  fill-rule="evenodd"
                  d="M1 13.5A1.5 1.5 0 0 0 2.5 15h11a1.5 1.5 0 0 0 1.5-1.5v-6a.5.5 0 0 0-1 0v6a.5.5 0 0 1-.5.5h-11a.5.5 0 0 1-.5-.5v-11a.5.5 0 0 1 .5-.5H9a.5.5 0 0 0 0-1H2.5A1.5 1.5 0 0 0 1 2.5v11z"
                />
              </svg>
              <svg
                role="button"
                data-bs-toggle="modal"
                data-bs-target="#popupModal"
                xmlns="http://www.w3.org/2000/svg"
                width="16"
                height="16"
                fill="currentColor"
                class="bi bi-trash"
                viewBox="0 0 16 16"
                @click="getSelected(product)"
              >
                <path d="M5.5 5.5A.5.5 0 0 1 6 6v6a.5.5 0 0 1-1 0V6a.5.5 0 0 1 .5-.5zm2.5 0a.5.5 0 0 1 .5.5v6a.5.5 0 0 1-1 0V6a.5.5 0 0 1 .5-.5zm3 .5a.5.5 0 0 0-1 0v6a.5.5 0 0 0 1 0V6z" />
                <path
                  fill-rule="evenodd"
                  d="M14.5 3a1 1 0 0 1-1 1H13v9a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V4h-.5a1 1 0 0 1-1-1V2a1 1 0 0 1 1-1H6a1 1 0 0 1 1-1h2a1 1 0 0 1 1 1h3.5a1 1 0 0 1 1 1v1zM4.118 4 4 4.059V13a1 1 0 0 0 1 1h6a1 1 0 0 0 1-1V4.059L11.882 4H4.118zM2.5 3V2h11v1h-11z"
                />
              </svg>
            </td>
          </tr>
        </tbody>
      </table>
    </div>
    <nav class="d-flex justify-content-end">
      <pagination
        v-model="page"
        :records="products.count"
        :per-page="10"
      />
    </nav>
  </div>
</template>

<script>
import { ref, inject, watch } from 'vue'
import { Modal } from 'bootstrap'
import Pagination from 'v-pagination-3';

import Product from '@/components/modal/Product.vue'
import Popup from '@/components/modal/Popup.vue'
import api from '@/api'

export default {
  components: { Product, Popup, Pagination },
  setup (props) {
    const products = ref({count: NaN})
    const selected = ref({})
    const page = ref(1)
    const global = inject('global')

    const getProducts = async () => {
      const params = {
        page: page.value
      }
      const token = await global.inspectToken()
      try {
        const res = await api.listProduct(params, token)
        products.value = res.data
      } catch (error) {
        console.log(error)
      }
    }

    const getSelected = product => {
      selected.value = product || {name: '', price: 0}
    }

    watch(page, getProducts)
    
    getProducts()

    return {
      products,
      selected,
      page,
      global,
      getProducts,
      getSelected
    }
  },
  methods: {
    async onSave (product) {
      const {id, ...input} = product
      const payload = input
      const token = await this.global.inspectToken()
      try {
        if (id) await api.updateProduct(id, payload, token)
        else await api.addProduct(payload, token)
      } catch (error) {
        console.log(error)
      }
      await this.getProducts()
      var modal = Modal.getInstance(document.getElementById('productModal'))
      modal.toggle()
    },
    async onDelete () {
      const token = await this.global.inspectToken()
      try {
        await api.deleteProduct(this.selected.id, token)
      } catch (error) {
        console.log(error)
      }
      await this.getProducts()
      var modal = Modal.getInstance(document.getElementById('popupModal'))
      modal.toggle()
    }
  }
}
</script>
