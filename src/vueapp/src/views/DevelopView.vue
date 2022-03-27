<template>
  <div>
    <div>
        <p>ルームを作成</p>
        <button v-on:click="roomSettingPopUp">Add Room +</button>
        <!-- モーダルポップアップの要素を作成 -->
        <div id="room-setting-overlay" v-show="ShowContentRoomSetting" v-on:click="roomSettingPopDown">
            <div id="room-setting-content" v-on:click="stopEvent">
                <div class="close_popup">
                    <button type="button" v-on:click="roomSettingPopDown">✕</button>
                </div>
                <p>ルームの作成を行います</p>
                <input type="text" v-model="RoomName" placeholder="ルーム名を入力">
                <p><button v-on:click="addRoomAPI">作成</button></p>
            </div>
        </div>
        <div id="room-add-complete-overlay" v-show="ShowContentRoomAddComp" v-on:click="roomAddCompPopDown">
            <div id="room-add-complete-content" v-on:click="stopEvent">
                <div class="close_popup">
                    <button type="button" v-on:click="roomAddCompPopDown">✕</button>
                </div>

                
                <div v-if="RoomURL !== ''">
                    <p>ルーム作成完了のお知らせ</p>
                    <p>ルーム名: {{ RoomName }}</p>
                    ルームURL: <a v-bind:href="RoomURL">{{ RoomURL }}</a>
                </div>
                <div v-else>
                    <p>ルームの作成に失敗しました</p>
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
        ShowContentRoomSetting: false,
        ShowContentRoomAddComp: false,
        RoomName: "",
        RoomURL: ""
    };
  },
  mounted() {

  },
  methods: {
    roomSettingPopUp () {
        this. ShowContentRoomSetting = true
    },
    roomSettingPopDown () {
        this.RoomName = ""
        this. ShowContentRoomSetting = false
    },
    roomAddCompPopUp () {
        this. ShowContentRoomAddComp = true
    },
    roomAddCompPopDown () {
        this.RoomName = ""
        this. ShowContentRoomAddComp = false
    },
    stopEvent (event) {
        // モーダルウィンドウ内のクリックでウィンドウが閉じないように
        event.stopPropagation()
    },
    addRoom () {
        console.log(this.RoomName)
        this.RoomName = ""
        this. ShowContentRoomSetting = false
    },
    addRoomAPI () {
        // django側へpostAPIを実行し、ルームの作成を行う
        // this.axios.defaults.xsrfCookieName = 'csrftoken'
        // this.axios.defaults.xsrfHeaderName = "X-CSRFTOKEN"
        this.axios.post('/api/v1/room/add/', {
            room_name: this.RoomName
        })
        .then((response) => {
            console.log("【POST】API OK!!")
            console.log(response.data)
            this.RoomURL = response.data.room_url
            // DOMの更新まで遅延させる
            this.$nextTick(function() {
                // nextTickを使用してコンソールにログを出力します。
                console.log(this.RoomURL);
            });
        })
        .catch(error => {
            console.log("【POST】API NG!!")
            console.log(error.response)
            this.RoomURL = ""
            // DOMの更新まで遅延させる
            this.$nextTick(function() {
                // nextTickを使用してコンソールにログを出力します。
                console.log(this.RoomURL);
            });
        });

        this. ShowContentRoomSetting = false
        this.roomAddCompPopUp()
    },

  }
};
</script>

<style scoped>
#room-setting-overlay, #room-add-complete-overlay{
/* 要素を重ねた時の順番 */
z-index:1;

/* 画面全体を覆う設定 */
position:fixed;
top:0;
left:0;
width:100%;
height:100%;
background-color:rgba(0,0,0,0.5);

/* 画面の中央に要素を表示させる設定 */
display: flex;
align-items: center;
justify-content: center;

}

#room-setting-content, #room-add-complete-content{
z-index:2;
width:50%;
padding: 1em;
background:#fff;
}

.close_popup {
position: sticky;
top: 0;
height: 0;
text-align: right;
}

</style>