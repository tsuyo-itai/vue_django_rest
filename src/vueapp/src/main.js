import { createApp } from "vue";
import App from "./App.vue";
import router from "./router";
import axios from "axios";
import VueAxios from "vue-axios";

const app = createApp(App);

// axios設定
axios.defaults.baseURL = "http://" + location.hostname + ":8000";
axios.defaults.headers.post["Content-Type"] = "application/json;charset=utf-8";
// axios.defaults.headers.post['Access-Control-Allow-Origin'] = '*';
// axios.defaults.headers.post['Access-Control-Allow-Methods'] = "PUT, GET, POST, DELETE, OPTION";

app.use(router);
app.use(VueAxios, axios);

app.mount("#app");
