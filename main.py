import os
from flask import Flask, request, json, abort, Response

import wav_handler

SERVER_HOST = os.getenv('SERVER_HOST')
SERVER_PORT = os.environ.get('SERVER_PORT')
api = Flask(__name__)


@api.route('/harmonic_filter', methods=['POST'])
def harmonic_filter():
    if request.method == 'POST':
        json_request = request.json
        try:
            sample_rate = json_request['sample_rate']
            base_freq = json_request['base_freq']
            harmonics = json_request['num_harmonics']
            samples = json_request['samples']
        except:
            abort(Response('ERROR: invalid input', 400))
        return wav_handler.perform_filter(sample_rate, base_freq, harmonics, samples)

if __name__ == '__main__':
    api.run(host=SERVER_HOST, port=SERVER_PORT)