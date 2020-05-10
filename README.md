# Evan Jiang's Academic Innovation Summer Fellowship Application

Hello! This is a single-page VueJS/Flask implementation of the Meme Generator problem as described.

My email is eyjiang@umich.edu.


## Installation

Dependencies to install for this app to work:
- Vue
- VueCLI
- Node
- npm
- Python
- Flask


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

You must add your own Flickr API key in /server/config.py: https://www.flickr.com/services/api/

After both the server and client are running, paste http://localhost:8080/ into the URL to visit the page.