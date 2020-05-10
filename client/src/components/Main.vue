<template>
  <div class="container">
    <div class="row">
      <div class="col-sm">
        <h1>Meme Generator</h1>

        <!-- Search form -->
        <input class="form-control" v-model="user_input"
        type="text" placeholder="Search" aria-label="Search">
        <br>
        <button v-on:click="getData" type="button"
        class="btn btn-success btn-sm">Search for an Image!</button>

        <hr><br><br>

        <div v-for="(photo_urls, index) in chunked_urls" :key="index" class="row">
          <div v-for="(photo_url, index) in photo_urls" :key="index" class="col-lg-4">
            <div class="select-meme-photo">
              <img class="select-meme-img" v-bind:src="photo_url"
               v-on:click="selected_photo_url = photo_url">
            </div>
          </div>
        </div>
      </div>

      <div class="col-md">
        <!-- Search form -->
        <input class="form-control" type="text" v-model="user_meme_text"
        placeholder="Add text to selected image." aria-label="Search">

        <br>

        <figure>
          <img v-bind:src="selected_photo_url">
          <figcaption>{{ selected_photo_url ? user_meme_text : ''}}</figcaption>
        </figure>
      </div>

    </div>
  </div>
</template>

<script>
import axios from 'axios';

function chunkArray(photoCols, photoUrls, chunkedUrls) {
  let chunk = [];
  for (let i = 0; i < photoUrls.length; i += 1) {
    if (i !== 0 && i % photoCols === 0) {
      chunkedUrls.push(chunk);
      chunk = [];
    }
    chunk.push(photoUrls[i]);
  }
  if (chunk.length !== 0) chunkedUrls.push(chunk);
  return chunkedUrls;
}

export default {
  data() {
    return {
      photo_urls: [],
      chunked_urls: [],
      user_input: '',
      selected_photo_url: '',
      user_meme_text: '',
      photo_cols: 2,
    };
  },
  methods: {
    getData() {
      const searchTerms = this.user_input.replace(' ', '+');
      const path = `http://localhost:5000/photos?user_input=${searchTerms}`;
      axios.get(path)
        .then((res) => {
          this.photo_urls = res.data.photo_urls;
          this.chunked_urls = [];
          this.chunked_urls = chunkArray(this.photo_cols, this.photo_urls, this.chunked_urls);
          console.log(this.chunked_urls);
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
        });
    },

  },
};

</script>


<style>
.select-meme-photo {
  position: relative;
}
.select-meme-img {
  display: inline-block;
  width: 200px;
  height: 200px;
  border-radius: 5px;
  background-color: #fff;
  box-shadow: 0 3px 5px rgba(0,0,0,0.3);
  transition: all 0.3s ease-in-out;
  margin: 10px;
}
.select-meme-img::after {
  content: '';
  position: absolute;
  z-index: -1;
  width: 100%;
  height: 100%;
  opacity: 0;
  border-radius: 5px;
  box-shadow: 0 5px 15px rgba(0,0,0,0.6);
  transition: opacity 0.15s ease-in-out;
}
.select-meme-img:hover {
  transform: scale(1.15, 1.15);
}
/* Fade in the pseudo-element with the bigger shadow */
.select-meme-img:hover::after {
  opacity: 1;
}
figcaption {
  display: block;
  font-family: impact;
  font-size: 40px;
}
</style>
