<template>
  <div>
    <div v-for="(data, key) in Datas" :key="key">
      <p>{{ data.name }}</p>
      <p>{{ data.telnum }}</p>
      <p>{{ data.comment }}</p>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      Datas: [],
    };
  },
  mounted() {
    this.axios
      .get("http://127.0.0.1:8000/api/v1/get_test_information/")
      .then((response) => {
        this.Datas = response.data;
      });
  },
};
</script>