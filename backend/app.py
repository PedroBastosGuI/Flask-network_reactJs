import os
from flask import Flask, render_template, request
import os
import cv2 as cv
from matplotlib.pyplot import get
import tensorflow as tf
import pandas as pd
from segmentation import Segmentation
from normalization import Normalization
from PIL import Image
import numpy as np
from reverseProxy import proxyRequest

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
    global meu_dic  
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
                neural_model = tf.keras.models.load_model("C:\\Users\\Galpão-Desktop\\Documents\\Aibeans_project\\Flask-network_reactJs\\backend\\treinamento_dois")

                result_predict = neural_model.predict(normalization_classifier_model)
                

                result_predict_argmax = []
                for list_argmax in result_predict:
                    argmax =  np.argmax(list_argmax, axis=0)
                result_predict_argmax.append(argmax)
                
                results_index = pd.Series(result_predict_argmax)
                results_count = results_index.value_counts()
                print("OIA EU AI",results_count)
                


                list_test = ['Amassados','Ardidos','Chochos','Esverdeados','Germinados','Impurezas','Maduros','Mofados','Picados_por_inseto','Quebrados','Queimados']
                meu_dic = {list_test[i]:str(result_predict[0][i]) for i in range(len(list_test))}
                return meu_dic

            else:
                return 'error'

        
@app.route('/teste', methods=['GET'])
def getClassification():
    return meu_dic


