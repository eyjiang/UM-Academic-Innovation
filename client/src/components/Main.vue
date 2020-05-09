<template>
  <div class="container">
    <div class="row">
      <div class="col-sm-10">
        <h1>Meme Generator</h1>

        <!-- Search form -->
        <input class="form-control" v-model="user_input"
        type="text" placeholder="Search" aria-label="Search">
        <button v-on:click="getData" type="button" class="btn btn-success btn-sm">Submit</button>

        <hr><br><br>
        <br><br>

        <div v-for="(photo, index) in photo_urls" :key="index">
          <img v-bind:src="photo">
        </div>

      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      photo_urls: [],
      user_input: '',
    };
  },
  methods: {
    getData() {
      const path = `http://localhost:5000/photos?user_input=${this.user_input}`;
      axios.get(path)
        .then((res) => {
          this.photo_urls = res.data.photo_urls;
          console.log(this.photo_urls);
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
        });
    },
  },
};
</script>
