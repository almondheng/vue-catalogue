import axios from 'axios'

const ENDPOINT = 'http://127.0.0.1:8000/api'

const auth = async payload => {
  return await axios.post(ENDPOINT + '/token/', payload)
}

const authRefresh = async payload => {
  return await axios.post(ENDPOINT + '/token/refresh/', payload)
}

export default { auth, authRefresh }
