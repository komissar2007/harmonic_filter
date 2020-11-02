import numpy as np
import wave
import math

from flask import Response, abort, jsonify


def running_mean(x, window_size):
    cumsum = np.cumsum(np.insert(x, 0, 0))
    value = (cumsum[window_size:] - cumsum[:-window_size]) / window_size
    return value


def remove_harmonic(cut_off_freq, filtered, sample_rate):
    freq_ratio = (cut_off_freq / sample_rate)
    N = int(math.sqrt(0.196196 + freq_ratio ** 2) / freq_ratio)
    result = running_mean(filtered, N).astype(np.float)
    return result


def interpret_wav(raw_bytes, n_frames, n_channels):
    dtype = np.int16
    channels = np.fromstring(raw_bytes, dtype=dtype)
    channels.shape = (n_frames, n_channels)
    channels = channels.T
    return channels


def perform_filter(sample_rate, base_freq, harmonics, samples):
    response = Response()
    response.mimetype = "application/json"
    cut_off_freq = (int(base_freq) * int(harmonics))
    samples = remove_harmonic(cut_off_freq, samples, sample_rate)
    return jsonify({'filtered_samples': samples.tolist()})


def filter(cut_off_freq, channels, filtered, sample_rate):
    freq_ratio = (cut_off_freq / sample_rate)
    N = int(math.sqrt(0.196196 + freq_ratio ** 2) / freq_ratio)

    return running_mean(filtered, N).astype(channels.dtype)


def perform_filter_file(file_name, base_freq, nharmonics):
    response = Response()
    response.mimetype = "application/json"
    cut_off_freq = (int(base_freq) * int(nharmonics))
    output_file = 'filtered-' + file_name

    try:
        input_file = wave.open("files/" + file_name, 'rb')
        sample_rate = input_file.getframerate()
        amp_width = input_file.getsampwidth()
        n_channels = input_file.getnchannels()
        n_frames = input_file.getnframes()
        signal = input_file.readframes(n_frames * n_channels)
        input_file.close()
    except FileNotFoundError:
        abort(Response('ERROR: failed to handle given file', 400))

    channels = interpret_wav(signal, n_frames, n_channels)
    filtered = channels[0]
    for x in range(2, int(nharmonics)):
        freq = x*int(base_freq)
        filtered = filter(freq, channels, filtered, sample_rate)
    wav_file = wave.open("filtered/" + output_file, "w")
    wav_file.setparams((1, amp_width, sample_rate, n_frames, input_file.getcomptype(), input_file.getcompname()))
    wav_file.writeframes(filtered.tobytes('C'))
    wav_file.close()
    response.data = "file is created: " + output_file
    return response
