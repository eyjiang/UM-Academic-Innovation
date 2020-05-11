<template>
  <div class="container">
  <h1>Meme Generator</h1>
  <br>
    <div class="row">
      <div class="col-sm">

        <!-- Search form -->
        <input class="form-control" v-model="user_input"
        type="text" placeholder="Search for an image by typing here!" aria-label="Search">
        <br>
        <button v-on:click="getData" type="button"
        class="btn btn-success btn-sm">Search for an Image!</button>

        <hr><p>{{ response_text }}</p><br>

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
      <div>
        <!-- Search form -->
        <input class="form-control" id="add-text-box" type="text" v-model="user_meme_text"
        placeholder="Add text to selected image." aria-label="Search">

        <br>

        <figure class="selected-photo">
          <img v-bind:src="selected_photo_url">
            <!-- <figcaption>{{ selected_photo_url ? user_meme_text : ''}}</figcaption> -->
          <div class="figcapt">{{ selected_photo_url ? user_meme_text : ''}} </div>
        </figure>
        </div>
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
      response_text: '',
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
          this.response_text = this.photo_urls.length === 0 ? 'No pictures found.' : 'Click on an image to select it!';
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
  margin: auto;
  width: 50%;
  padding: 15px;
}
.select-meme-img {
  display: inline-block;
  width: 200px;
  height: 200px;
  border-radius: 5px;
  background-color: #fff;
  box-shadow: 0 3px 5px rgba(0,0,0,0.3);
  transition: all 0.15s ease-in-out;
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
.select-meme-img:hover::after {
  opacity: 1;
}
.selected-photo {
  position: relative;
  top: 20px;
}
.figcapt {
  overflow-wrap: break-word;
}
#add-text-box {
  position: relative;
}
.figcapt {
  width: 100%;
  font-family: impact;
  font-size: 40px;
  display: inline-block;
  word-break: break-all;
}
</style>
