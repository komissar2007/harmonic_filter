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


def perform_filter(sample_rate, base_freq, harmonics, samples):
    response = Response()
    response.mimetype = "application/json"
    cut_off_freq = (int(base_freq) * int(harmonics))
    samples = remove_harmonic(cut_off_freq, samples, sample_rate)
    return jsonify({'filtered_samples': samples.tolist()})
    # return response
