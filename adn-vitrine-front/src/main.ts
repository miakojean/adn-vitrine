import { createApp } from 'vue'
import './style.css'
import App from './App.vue'
import router from './router'
import 'remixicon/fonts/remixicon.css'
import '@fortawesome/vue-fontawesome'

const app = createApp(App)
app.use(router)
app.mount('#app')