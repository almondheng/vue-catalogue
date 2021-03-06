import { reactive, readonly } from "vue";
import jwt_decode from "jwt-decode";
import api from '@/api'

const state = reactive({
  jwt: JSON.parse(localStorage.getItem('t')),
  isLogin: 0,
  isStaff: false
});

const updateToken = function (tokens) {
  localStorage.setItem('t', JSON.stringify(tokens))
  state.jwt = tokens
}

const removeToken = function () {
  localStorage.removeItem('t');
  state.jwt = null;
}

const inspectToken = async function () {
  const tokens = state.jwt
  if (tokens) {
    const {exp, is_staff} = jwt_decode(tokens.access)
    const {refresh_exp} = jwt_decode(tokens.refresh)
    if (exp > Date.now()/1000) {
      state.isStaff = is_staff
      state.isLogin = 1
      return tokens.access
    } else if (refresh_exp > Date.now()/1000) {
      try {
        const payload = {refresh: tokens.refresh}
        const response = await api.authRefresh(payload)
        tokens.access = response.data.newAccess
        updateToken(tokens)
        return tokens.access
      } catch (error) {
        console.log(error)
        return false
      }
    } else {
      return false
    }
  } else {
    return false
  }
}

const login = function (tokens) {
  updateToken(tokens)
  return inspectToken()
}

const logout = function () {
  removeToken()
  state.isLogin = 0;
}

export default { state: readonly(state), inspectToken, login, logout };