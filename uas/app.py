# Nama : Muhammad Ivan satria | Ikhlasul amal
# NIM : 19090082              | 19090007
# Kelas : 6D                  | 6A
import os
import sys
import numpy as np
from util import base64_to_pil
from flask import Flask, redirect, url_for, request, render_template, Response, jsonify, redirect
from werkzeug.utils import secure_filename
#from gevent.pywsgi import WSGIServer
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras.applications.imagenet_utils import preprocess_input, decode_predictions
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
from tensorflow.keras.utils import get_file


app = Flask(__name__)




model = load_model('models/model.h5') 

def model_predict(img, model):
    img = img.resize((200, 200))          
    
    x = image.img_to_array(img)
    x = x.reshape(-1, 200, 200, 3)
    x = x.astype('float32')
    x = x / 255.0
    preds = model.predict(x)
    return preds

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/predict', methods=['GET', 'POST'])
def predict():
    if request.method == 'POST':
        
        img = base64_to_pil(request.json)

        
        preds = model_predict(img, model)

        #==================================================================================#

        target_names = ['Annon', 'Ginaa', 'ivan', 'Wisnu', 'Nizar', 'Dani', 'Farhan', 'Khaepah']     # ⚠️ SESUAIKAN ⚠️

        hasil_label = target_names[np.argmax(preds)]
        hasil_prob = "{:.2f}".format(100 * np.max(preds)) 

        #==================================================================================#

        return jsonify(result=hasil_label, probability=hasil_prob)

    return None

if __name__ == '__main__':
  
    app.run(debug=True)
   