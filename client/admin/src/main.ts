import { createApp } from 'vue'
import "@/style.css";
import "@/reset.css";
import "@/assets/css/themes/theme.scss"
import 'element-plus/dist/index.css'
import App from './App.vue'
import router from '@/router/index';

let app = createApp(App)

app.use(router).mount('#app')

