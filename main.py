import os
from flask import Flask, request, json, abort, Response

import wav_handler

SERVER_HOST = os.getenv('SERVER_HOST')
SERVER_PORT = os.environ.get('SERVER_PORT')
api = Flask(__name__)



@api.route('/filter', methods=['POST'])
def perform_filter():
    if request.method == 'POST':
        json_request = request.json
        try:
            file_name = json_request['file_name']
            base_freq = json_request['base_freq']
            harmonics = json_request['harmonics']
        except:
            abort(Response('ERROR: invalid input', 400))
        return wav_handler.perform_filter(file_name, base_freq, harmonics)

if __name__ == '__main__':
    api.run(host=SERVER_HOST, port=SERVER_PORT)