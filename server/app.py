from flask import Flask, jsonify, request
from flask_cors import CORS
import requests
import config


# configuration
DEBUG = True
API_KEY = config.api_key

# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)

# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})

# Route to retrieve Flickr photos based on user_input search
# Uses flickr.photos.search endpoint
@app.route('/photos', methods=['GET'])
def retrieve_photos():
    search_text = request.args['user_input']
    photo_url_list = retrieve_flickr_imgs(search_text)

    return jsonify({
        'status': 'success',
        'photo_urls': photo_url_list
    })


def retrieve_flickr_imgs(search_text):
    photo_url_list = []

    try:
        r = requests.get(
            'https://www.flickr.com/services/rest/?method=flickr.photos.search&api_key={API_KEY}&text={search_text}&per_page=20&page=1&format=json&nojsoncallback=1'.format(
                API_KEY=API_KEY,
                search_text=search_text)).json()
    # Currently handles failed requests as simply returning "No Results"
    except requests.exceptions.RequestException as e:
        return []

    # Constructs a list of photo urls using info retrieved from GET request
    # as described by: https://www.flickr.com/services/api/misc.urls.html
    photos = r['photos']['photo']
    for photo in photos:
        photo_id = photo['id']
        farm_id = photo['farm']
        server_id = photo['server']
        secret = photo['secret']

        photo_url = 'https://farm{farm}.staticflickr.com/{server}/{id}_{secret}.jpg'.format(
            farm=farm_id, server=server_id, id=photo_id, secret=secret)

        photo_url_list.append(photo_url)

    return photo_url_list


if __name__ == '__main__':
    app.run()
