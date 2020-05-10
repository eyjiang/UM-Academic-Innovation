from flask import Flask, jsonify, request
from flask_cors import CORS
import requests
import config


# configuration
DEBUG = True

# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)

# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})


API_KEY = config.api_key


@app.route('/photos', methods=['GET'])
def retrieve_photos():
    search_text = request.args['user_input']
    print(search_text)
    photo_url_list = retrieve_flickr_imgs(search_text)

    return jsonify({
        'status': 'success',
        'photo_urls': photo_url_list
    })


def retrieve_flickr_imgs(search_text):
    photo_url_list = []
    r = requests.get(
    'https://www.flickr.com/services/rest/?method=flickr.photos.search&api_key={API_KEY}&text={search_text}&per_page=20&page=1&format=json&nojsoncallback=1'.format(API_KEY=API_KEY, search_text=search_text)).json()

    # TODO: Handle no-results error case

    photos = r['photos']['photo']
    for photo in photos:
        photo_id = photo['id']
        farm_id = photo['farm']
        server_id = photo['server']
        secret = photo['secret']

        photo_url = 'https://farm{farm}.staticflickr.com/{server}/{id}_{secret}.jpg'.format(farm=farm_id, server=server_id, id=photo_id, secret=secret)

        photo_url_list.append(photo_url)

    return photo_url_list


if __name__ == '__main__':
    app.run()