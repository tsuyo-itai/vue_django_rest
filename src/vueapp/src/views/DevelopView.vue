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
                
                <div class="container">
                    <div class="left-column">
                        <p>名前を入力</p>
                        <input type="text" v-model="Name1" placeholder="1人目の名前を入力">
                    </div>
                    <div class="right-column">
                        <p>画像をアップロード</p>
                        <ImageUpload v-model="UploadImage1" v-on:image-upload-emit="uploadImage1($event)" />
                        <img :src="UploadImage1" />

                    </div>
                </div>

                <div class="container">
                    <div class="left-column">
                        <p>名前を入力</p>
                        <input type="text" v-model="Name2" placeholder="2人目の名前を入力">
                    </div>
                    <div class="right-column">
                        <p>画像をアップロード</p>
                        <ImageUpload v-model="UploadImage2" v-on:image-upload-emit="uploadImage2($event)" />
                        <img :src="UploadImage2" />

                    </div>
                </div>

                
                <button v-on:click="addRoomAPI">作成</button>
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
// @ is an alias to /src
import ImageUpload from "@/components/ImageUpload.vue";

export default {
    data() {
        return {
            ShowContentRoomSetting: false,
            ShowContentRoomAddComp: false,
            RoomName: "",
            RoomURL: "",
            Name1: null,
            Name2: null,
            UploadImage1: null,
            UploadImage2: null,
        };
    },
    components: {
        ImageUpload,
    },
    mounted() {

    },
    methods: {
        uploadImage1 (event) {
            this.UploadImage1 = event
            console.log("event1 ok")
        },
        uploadImage2 (event) {
            this.UploadImage2 = event
            console.log("event2 ok")
        },
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
                room_name: this.RoomName,
                image1_name: this.Name1,
                upload_image1: this.UploadImage1,
                image2_name: this.Name2,
                upload_image2: this.UploadImage2,
            })
            .then((response) => {
                console.log("【POST】API OK!!")
                console.log(response.data)
                this.RoomURL = response.data.room_url
                // DOMの更新まで遅延させる
                this.$nextTick(function() {
                    // nextTickを使用してコンソールにログを出力します。
                    console.log(this.RoomURL);
                    this. ShowContentRoomSetting = false
                    this.roomAddCompPopUp()
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
                    this. ShowContentRoomSetting = false
                    this.roomAddCompPopUp()
                });
            });
        },

    }
};
</script>

<style scoped>
img {
    width: 250px;
}

.container {
    display: flex;
    width: 100%;
}

.left-column {

    float: left;

    width: 40%; /* 要素の幅の定義 */
    background-color: #aaa; /* 視覚化のための背景色 */
    margin: 10px;

}

.right-column {

    float: right;

    width: 60%; /* 要素の幅の定義 */
    background-color: #ddd; /* 視覚化のための背景色 */
    margin: 10px;

}

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
width:65%;
max-height: 650px;
padding: 1em;
background:#fff;
overflow-y: auto;
overflow-y: scroll;
}

.close_popup {
position: sticky;
top: 0;
height: 0;
text-align: right;
}

</style>