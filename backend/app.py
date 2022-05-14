import os
from flask import Flask, render_template, request
import os
import cv2 as cv
import tensorflow as tf
import pandas as pd
from segmentation import Segmentation
from normalization import Normalization
from classifier import classifyImage
from PIL import Image
import numpy as np

from reverseProxy import proxyRequest
from seg import segmentation_two
MODE = os.getenv('FLASK_ENV')
DEV_SERVER_URL = 'http://localhost:3000/'

app = Flask(__name__)

# Ignore static folder in development mode.
if MODE == "development":
    app = Flask(__name__, static_folder=None)

@app.route('/')
@app.route('/<path:path>')
def index(path=''):
    if MODE == 'development':
        return proxyRequest(DEV_SERVER_URL, path)
    else:
        return render_template("index.html") 

@app.route('/classify', methods=['POST'])
def classify():
    if (request.files['image']): 
        file = request.files['image']

        img_response = Image.open(file.stream)

        img_array = np.array(img_response)[:,:,:-1]


        #print(img_array, 'bug aqui!!!')

        segmentation_value = Segmentation(img_array)


        

        if 1==1:
            
            print(segmentation_value)

            
            
            if len(segmentation_value.index) != 0 :
                normalization_classifier_model = Normalization(segmentation_value)
                print(normalization_classifier_model,"OLHA EU AQUI PEDRIN")
                neural_model = tf.keras.models.load_model("C:\\Users\\Galpão-Desktop\\Documents\\Aibeans_project\\Flask-network_reactJs\\backend\\treinamento_dois")

                result_predict = neural_model.predict(normalization_classifier_model)
                
                
                list_test = ['maduro','quebrado','esverdado','queimado','ardidos','mofados','mofados','maduro','maduro']
                meu_dic = {list_test[i]:str(result_predict[0][i]) for i in range(len(list_test))}
                
                print("aaaaaaaaaaa",meu_dic )
#" ".join([str(x) for x in result_predict[0]])

                return meu_dic

            else:
                return 'error'
        
