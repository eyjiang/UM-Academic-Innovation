# Evan Jiang's Academic Innovation Summer Fellowship Application

Hello! This is a single-page VueJS/Flask implementation of the Meme Generator problem as described.

My email is eyjiang@umich.edu.


## Installation

Dependencies to install for this app to work:
- Vue v2.6.10
- Vue CLI v3.7.0
- Node v12.1.0
- npm v6.9.0
- Flask v1.0.2
- Python v3.7.3

Install Vue:
```bash
npm i vue
```

Install VueCLI:
```bash
npm install -g @vue/cli@3.7.0
```

Install Server Requirements:
```bash
cd server
pip install -r requirements.txt
```


## Running the App

Running the server:

```bash
cd server
python app.py
```

Running the client:

```bash
cd client
npm run serve
```

**You must add your own Flickr API key in /server/config.py: https://www.flickr.com/services/api/**

After both the server and client are running, paste http://localhost:8080/ into the URL to visit the page.




This project uses the flickr.photos.search endpoint to conduct photo searches, which sometimes results in some odd images.
It is rather funny, however, that Flickr's database for "University of Michigan" returns 20+ images of our campus' fat squirrels.

![alt-text](https://github.com/eyjiang/UM-Academic-Innovation/blob/master/README-Img.png)