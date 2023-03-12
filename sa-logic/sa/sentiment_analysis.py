from textblob import TextBlob
from flask import Flask, request, jsonify

app = Flask(__name__)

import requests

@app.route('/')
def ping_service():
    try:
        response = requests.get('http://web:8080/')
    except requests.exceptions.RequestException as e:
        print('\n Cannot reach the pong service.')
        return 'Ping ...\n'
    return 'Ping ...' + response.text + ' \n'

@app.route("/analyse/sentiment", methods=['POST'])
def analyse_sentiment():
    sentence = request.get_json()['sentence']
    polarity = TextBlob(sentence).sentences[0].polarity
    return jsonify(
        sentence=sentence,
        polarity=polarity
    )


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
