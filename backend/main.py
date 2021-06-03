# Copyright 2018 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# [START gae_python38_render_template]
# [START gae_python3_render_template]
import datetime

from flask import Flask, request, jsonify, abort, render_template
from keras_preprocessing.text import tokenizer_from_json

import tensorflow as tf
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences

from Sastrawi.Stemmer.StemmerFactory import StemmerFactory
from Sastrawi.StopWordRemover.StopWordRemoverFactory import StopWordRemoverFactory

import os
import json
import string

app = Flask(__name__)

filepath = os.getcwd()

model = tf.keras.models.load_model(
    os.path.join(filepath, 'ml', 'sm', 'classify_model'))

tokenizer = None

with open(os.path.join(filepath, 'ml', 'tokenizer.json')) as f:
    data = json.load(f)
    tokenizer = tokenizer_from_json(data)

stemmer_factory = StemmerFactory()
stemmer = stemmer_factory.create_stemmer()

stopword_factory = StopWordRemoverFactory()
stopword = stopword_factory.create_stop_word_remover()

label_list = [
    "perselisihan", "infrastruktur", "pemerintah", "kesehatan", "teknologi",
    "administrasi", "fasilitas", "lingkungan", "ketertiban", "listrik",
    "bahaya", "lainnya", "pungli", "ilegal", "lalulintas", "bencana", "air",
    "pendidikan", "kebersihan", "sosial", "wisata", "sara", "pencurian",
    "korupsi", "bbm", "keuangan"
]


def clean_text(inp):
    # Make string into lowercase string
    treated = inp.lower()
    # remove punctuation
    treated = treated.translate(str.maketrans("", "", string.punctuation))
    # remove trailing whitespace
    treated = treated.strip()
    # Remove stopwords
    treated = stopword.remove(treated)
    # Stem string
    treated = stemmer.stem(treated)
    return treated


@app.route('/infer', methods=['POST'])
def infer():
    if not request.json or not 'text' in request.json:
        abort(400)

    raw_text = request.json['text']

    sample_laporan = raw_text
    treated_input = clean_text(sample_laporan)
    pad = pad_sequences(tokenizer.texts_to_sequences([treated_input]),
                        maxlen=300,
                        truncating='post')
    prediction = model.predict(pad)

    res = dict(zip(label_list, ["{:.5f}".format(i) for i in prediction[0]]))

    return jsonify(res), 200


@app.route('/')
def root():

    return render_template('index.html')


if __name__ == '__main__':
    # This is used when running locally only. When deploying to Google App
    # Engine, a webserver process such as Gunicorn will serve the app. This
    # can be configured by adding an `entrypoint` to app.yaml.
    # Flask's development server will automatically serve static files in
    # the "static" directory. See:
    # http://flask.pocoo.org/docs/1.0/quickstart/#static-files. Once deployed,
    # App Engine itself will serve those files as configured in app.yaml.
    app.run(host='127.0.0.1', port=8080, debug=True)
# [END gae_python3_render_template]
# [END gae_python38_render_template]
