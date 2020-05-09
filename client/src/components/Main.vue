<template>
  <div class="container">
    <div class="row">
      <div class="col-sm-10">
        <h1>Meme Generator</h1>
        <hr><br><br>
        <button type="button" class="btn btn-success btn-sm">Temp Button</button>
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
    };
  },
  methods: {
    getData() {
      const path = 'http://localhost:5000/';
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
  created() {
    this.getData();
  },
};
</script>
