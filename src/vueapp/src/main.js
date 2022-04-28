import { createApp } from "vue";
import App from "./App.vue";
import router from "./router";
import axios from "axios";
import VueAxios from "vue-axios";

const app = createApp(App);

// [vue_port, django_port] のport紐づけ用配列を用意
const portlinkArray = [
  ["8080", "8000"],
  ["9080", "9000"],
];

let django_port = "";
portlinkArray.forEach(function (portlink) {
  if (portlink[0] === location.port) {
    django_port = portlink[1];
  }
});

// axios設定
axios.defaults.baseURL = "http://" + location.hostname + ":" + django_port;
axios.defaults.headers.post["Content-Type"] = "application/json;charset=utf-8";
// axios.defaults.headers.post['Access-Control-Allow-Origin'] = '*';
// axios.defaults.headers.post['Access-Control-Allow-Methods'] = "PUT, GET, POST, DELETE, OPTION";

app.use(router);
app.use(VueAxios, axios);

app.mount("#app");
