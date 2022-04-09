<template>
  <div>
    <div>
        <h3>投票ページへようこそ</h3>

        <div class="img_frame">
          <img v-bind:src="Image1Path" v-bind:title="Image1Name" />
          <p>{{ Image1Name }}</p>
          <p>現在の投票数: xxx</p>
          <div class="box-vote">
            <button v-on:click="user1VoteClick">投票する</button>
            <div v-show="bUser1Vote">
              <span class="circle-icon"></span>
            </div>
          </div>
        </div>

        <div class="img_frame">
          <img v-bind:src="Image2Path" v-bind:title="Image2Name" />
          <p>{{ Image2Name }}</p>
          <p>現在の投票数: xxx</p>
          <div class="box-vote">
            <button v-on:click="user2VoteClick">投票する</button>
            <div v-show="bUser2Vote">
              <span class="circle-icon"></span>
            </div>
          </div>
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
        bUser1Vote: false,
        bUser2Vote: false,
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
    methods: {
        user1VoteClick () {
            if(!this.bUser1Vote)
            {
              // User1に投票されていない場合
              this.bUser1Vote = true
              this.bUser2Vote = false
              console.log("User1 Vote")
            }
        },
        user2VoteClick () {
            if(!this.bUser2Vote)
            {
              // User2に投票されていない場合
              this.bUser2Vote = true
              this.bUser1Vote = false
              console.log("User2 Vote")
            }
        },
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

.box-vote{
  height: 30px;
  display: flex;
  justify-content: center;
  gap: 15px;
}

.circle-icon{
  display: inline-block;
  width: 30px;
  height: 30px;
  border-radius: 50%;
  background: #f14040;
}

</style>
