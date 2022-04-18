<template>
  <div>
    <div>
      <h3>投票ページへようこそ</h3>

      <div class="img_frame">
        <img v-bind:src="Image1Path" v-bind:title="Image1Name" />
        <p>{{ Image1Name }}</p>
        <p>現在の投票数: {{ Image1VoteNum }}</p>
        <div class="box-vote">
          <button id="vote-button1" class="btn-solid" v-on:click="user1VoteClick">投票する</button>
        </div>
      </div>

      <div class="img_frame">
        <img v-bind:src="Image2Path" v-bind:title="Image2Name" />
        <p>{{ Image2Name }}</p>
        <p>現在の投票数: {{ Image2VoteNum }}</p>
        <div class="box-vote">
          <button id="vote-button2" class="btn-solid" v-on:click="user2VoteClick">投票する</button>
        </div>
      </div>
    </div>
    <div class="container">
      <button v-on:click="VoteResultSend">送信</button>
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
      Image1VoteNum: 0,
      Image2VoteNum: 0,
      bUser1Vote: false,
      bUser2Vote: false,
      nUser1VoteCnt: 0,
      nUser2VoteCnt: 0,
    };
  },
  mounted() {
    console.log(this.RoomToken);
    this.axios
      .get("/api/v1/room/information/" + this.RoomToken)
      .then((response) => {
        this.Datas = response.data;
        this.Image1Name = this.Datas.image1_name;
        this.Image2Name = this.Datas.image2_name;
        this.Image1Path = this.Datas.image1_path;
        this.Image2Path = this.Datas.image2_path;
        this.Image1VoteNum = this.Datas.image1_votenum;
        this.Image2VoteNum = this.Datas.image2_votenum;
      });
  },
  methods: {
    user1VoteClick() {
      if (!this.bUser1Vote) {
        // User1に投票されていない場合
        this.bUser1Vote = true;
        this.nUser1VoteCnt = 1;
        this.bUser2Vote = false;
        this.nUser2VoteCnt = 0;

        this.VoteButtonHighlight(this.bUser1Vote, this.bUser2Vote);
      }
    },
    user2VoteClick() {
      if (!this.bUser2Vote) {
        // User2に投票されていない場合
        this.bUser2Vote = true;
        this.nUser2VoteCnt = 1;
        this.bUser1Vote = false;
        this.nUser1VoteCnt = 0;

        this.VoteButtonHighlight(this.bUser1Vote, this.bUser2Vote);
      }
    },
    VoteButtonHighlight(vote1, vote2) {
      let elembutton1 = document.querySelector('#vote-button1');
      let elembutton2 = document.querySelector('#vote-button2');
      if (vote1) {
        elembutton1.classList.add('highlight');
      }
      else {
        elembutton1.classList.remove('highlight');
      }

      if (vote2) {
        elembutton2.classList.add('highlight');
      }
      else {
        elembutton2.classList.remove('highlight');
      }

    },
    VoteResultSend() {
      if (this.bUser1Vote || this.bUser2Vote) {
        this.axios
          .patch("/api/v1/room/vote/" + this.RoomToken, {
            image1_votenum: this.Image1VoteNum + this.nUser1VoteCnt,
            image2_votenum: this.Image2VoteNum + this.nUser2VoteCnt,
          })
          .then((response) => {
            console.log("【PATCH】API OK!!");
            // console.log(response.data);
            this.Image1VoteNum = response.data.image1_votenum;
            this.Image2VoteNum = response.data.image2_votenum;
            // DOMの更新まで遅延させる
            this.$nextTick(function () {
              // nextTickを使用してコンソールにログを出力します。
              this.bUser1Vote = false;
              this.bUser2Vote = false;
              this.VoteButtonHighlight(this.bUser1Vote, this.bUser2Vote);
            });
            // ここでページのリロードと同ユーザーからの送信制御を行いたい
          });
      } else {
        alert("投票を行ってから送信してください");
      }
    },
  },
};
</script>

<style scoped>
img {
  width: 500px;
  margin: 30px;
}

.img_frame {
  display: inline-block;
  text-align: center;
}

.box-vote {
  height: 40px;
  display: flex;
  justify-content: center;
  gap: 15px;
}

.container {
  margin: 100px;
}

.btn-solid {
  color: #fff;
  border-top: 4px solid #48ecc4;
  border-right: 4px solid #0a5f4a;
  border-bottom: 4px solid #0f745b;
  border-left: 4px solid #8cf9de;
  border-radius: 0;
  background: #11a37f;
}

.btn-solid:hover {
  color: #fff;
  border-top: 4px solid #0f745b;
  border-right: 4px solid #8cf9de;
  border-bottom: 4px solid #48ecc4;
  border-left: 4px solid #0a5f4a;
}

.btn-solid.highlight {
  color: #fff;
  border-top: 6px solid #f25656;
  border-right: 6px solid #e02626;
  border-bottom: 6px solid #d53e3e;
  border-left: 6px solid #ea6868;
  border-radius: 0;
  background: #11a37f;
}
</style>
