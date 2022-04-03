<template>
  <div>
    <div>
        <h3>投票ページへようこそ</h3>

        <div class="img_frame">
          <img v-bind:src="Image1Path" v-bind:title="Image1Name" />
          <p>{{ Image1Name }}</p>
        </div>

        <div class="img_frame">
          <img v-bind:src="Image2Path" v-bind:title="Image2Name" />
          <p>{{ Image2Name }}</p>
        </div>

      
    </div>

  </div>
</template>

<script>

export default {
    data() {
      return {
        RoomToken: this.$route.params.room_token,
        Datas: [],
        Image1Name: "",
        Image1Path: "",
        Image2Name: "",
        Image2Path: "",
      };
    },
    mounted() {
      console.log(this.RoomToken)
      this.axios
        .get("/api/v1/room/information/" + this.RoomToken)
        .then((response) => {
          this.Datas = response.data
          this.Image1Name = this.Datas.image1_name
          this.Image2Name = this.Datas.image2_name
          this.Image1Path = this.Datas.image1_path
          this.Image2Path = this.Datas.image2_path
        });
    },

};
</script>

<style scoped>
img {
    width: 500px;
}

.img_frame {
  display: inline-block;
  text-align: center;
}

</style>
