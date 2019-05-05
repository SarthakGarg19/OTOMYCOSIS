from flask import Flask,request, jsonify
from flask_restful import Resource, reqparse, Api
from flask_cors import CORS
import os
import cv2
# data analysis and wrangling
import pandas as pd
import numpy as np
from sklearn import feature_extraction, model_selection, naive_bayes, metrics, svm
import pickle as pkl
import datetime as datetime
# machine learning
from sklearn.naive_bayes import GaussianNB
from keras.models import load_model
from keras.preprocessing import image
from tqdm import tqdm
import tensorflow as tensorflow
from keras.preprocessing import image
from IPython.display import display
from PIL import Image
tensorflow.logging.set_verbosity(tensorflow.logging.ERROR)
from keras import backend as K

#Instantiate a flask object

app = Flask(__name__)
CORS(app)

#Instantiate Api object
api = Api(app)



# Loading Models and Transformers

def load_kmodel():
    model = load_model('my_model_44.h5')
    model.compile(optimizer = 'adam', loss = 'binary_crossentropy', metrics = ['accuracy'])
    return model


@app.route('/')
def home():
    return jsonify({
        "text":"Please go to frontend"
    })



@app.route('/api/v0.1/inference',methods = ['POST'])
def inference():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            print('No file part')
            return jsonify({
                "error":"No file"
            })
            # return redirect(request.url)
        file = request.files['file']
        # if user does not select file, browser also
        # submit a empty part without filename
        if file.filename == '':
            print('No selected file')
            return jsonify({
                "error":"No selected file"
            })
            # return redirect(request.url)
        if file:
            print(file.filename)
            # file.save(file.filename)
            file.save(os.path.join(os.pardir, file.filename))
            imagePath = os.path.join(os.pardir, file.filename)
            image = cv2.imread(imagePath)
            gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            mask = gray>100
            image = image[np.ix_(mask.any(1),mask.any(0))]

            image = cv2.resize(image, (224,224))
            image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

            image= np.array(image, dtype="float") / 255.0

            image = np.expand_dims(image, axis=0)
            model = load_kmodel()
            prediction=model.predict([image])
            prediction=np.argmax(prediction)
            if(prediction==0):
                prediction="AOM"
            elif(prediction==6):
                prediction="CSOM"
            elif(prediction==2):
                prediction="Wax"
            elif(prediction==3):
                prediction="Glue Ear"
            elif(prediction==4):
                prediction="Normal Ear"
            elif(prediction==5):
                prediction="Others"
            elif(prediction==6):
                prediction="Otomycosis"


            # CLEARING SESSION FOR MODEL TO LOAD AGAIN
            K.clear_session()

            # RETURNING PREDICTION
            return jsonify({
                "prediction":str(prediction)
            })
    # if request.method == 'POST'
    # content = request.json


    #
    return jsonify({
        "prediction":"test 1"
    })


if __name__== '__main__':
    app.run(debug=True)
