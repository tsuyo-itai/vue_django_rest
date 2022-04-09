<template>
  <div>
    <div>
      <input
        type="text"
        @keypress.enter="searchPokemon"
        v-model="SearchName"
        placeholder="ポケモン名を入力"
      />
      <button v-on:click="searchPokemon">Search</button>
    </div>

    <img v-bind:src="PokemonImage" />
    <h3>{{ PokemonName }}</h3>
  </div>
</template>

<script>
// 下記Jsonはここから取得 https://gist.github.com/PonDad/93922f63c3143489e30c3716d3d176d2
import pokemon_name_json from "../assets/json/pokemonName.json";

export default {
  data() {
    return {
      SearchName: "",
      PokemonName: "",
      PokemonImage: "",
      pokemonNameJson: pokemon_name_json,
    };
  },
  mounted() {
    this.getPokemonApi(this.SearchName);
  },
  methods: {
    convertPokemonName(to_lang, org_name) {
      let json = this.pokemonNameJson;
      let name = org_name;
      var i = 0;
      if (to_lang === "ja") {
        for (i = 0; i < json.length; i++) {
          if (json[i].en.toUpperCase() === org_name.toUpperCase()) {
            // 日本語変換用jsonにマッチしたら日本語へ変換する
            name = json[i].ja;
          }
        }
      } else {
        for (i = 0; i < json.length; i++) {
          if (json[i].ja === org_name) {
            // 日本語変換用jsonにマッチしたら日本語へ変換する
            name = json[i].en;
          }
        }
      }
      return name;
    },
    searchPokemon() {
      this.getPokemonApi(this.SearchName);
      // テキストボックスのクリア
      this.SearchName = "";
    },
    getPokemonApi(searchname) {
      if (searchname !== "") {
        // 検索ワードが入力されたときにコール
        let apisearchname = this.convertPokemonName(
          "en",
          searchname
        ).toLowerCase();
        this.axios
          .get("https://pokeapi.co/api/v2/pokemon/" + apisearchname)
          .then((response) => {
            this.PokemonImage = response.data.sprites.other.home.front_default;
            this.PokemonName = response.data.forms[0].name;

            console.log(response.data);

            this.PokemonName = this.convertPokemonName("ja", this.PokemonName);
          })
          .catch((error) => {
            console.log(error.response);
            this.PokemonImage = "";
            this.PokemonName = "";
          });
      }
    },
  },
};
</script>

<style scoped>
button {
  margin: 5px;
}
</style>
