import axios from 'axios'
import global from '@/global'

const baseURL = 'http://127.0.0.1:8000/api'

const auth = async payload => {
  return await axios.post(baseURL + '/token/', payload)
}

const authRefresh = async payload => {
  return await axios.post(baseURL + '/token/refresh/', payload)
}

const listProduct = async token => {
  return await axios.get(baseURL + '/products/', {headers: {'Authorization': 'Bearer ' + token}})
}

const addProduct = async (payload, token) => {
  return await axios.post(baseURL + '/products/', payload, {headers: {'Authorization': 'Bearer ' + token}})
}

const updateProduct = async (id, payload, token) => {
  return await axios.patch(`${baseURL}/products/${id}/`, payload, {headers: {'Authorization': 'Bearer ' + token}})
}

const deleteProduct = async (id, token) => {
  return await axios.delete(`${baseURL}/products/${id}/`, {headers: {'Authorization': 'Bearer ' + token}})
}

export default { auth, authRefresh, listProduct, addProduct, updateProduct, deleteProduct }
