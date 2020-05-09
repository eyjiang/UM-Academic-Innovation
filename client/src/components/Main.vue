<template>
  <div class="container">
    <div class="row">
      <div class="col-sm">
        <h1>Meme Generator</h1>

        <!-- Search form -->
        <input class="form-control" v-model="user_input"
        type="text" placeholder="Search" aria-label="Search">
        <br>
        <button v-on:click="getData" type="button" class="btn btn-success btn-sm">Submit</button>

        <hr><br><br>
        <br><br>

        <div class="meme-photo"
        v-for="(photo, index) in photo_urls" :key="index"
        v-on:click="selectPhoto(photo)">
          <img v-bind:src="photo">
        </div>
      </div>

      <div class="col-md">
        <!-- Search form -->
        <input class="form-control" type="text"
        placeholder="Add text to selected image." aria-label="Search">

        <div class="meme-photo">
          <img v-bind:src="selected_photo_url">
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
      selected_photo_url: '',
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
    selectPhoto(photoUrl) {
      this.selected_photo_url = photoUrl;
      console.log('selected photo');
    },
  },
};
</script>


<style>
.meme-photo {
  padding: 5px;
}
</style>
