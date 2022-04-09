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
    this.axios.get("/api/v1/get_test_information/").then((response) => {
      this.Datas = response.data;
      console.log(response.data);
    });
  },
};
</script>
