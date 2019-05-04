from flask import Flask,request, jsonify
from flask_restful import Resource, reqparse, Api
from flask_cors import CORS
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
    model = load_model('oto.h5')
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
            file.save(file.filename)
            imagePath = file.filename
            test = pd.read_csv('test.csv')
            test_image = []
            for i in tqdm(range(test.shape[0])):
                # img = image.load_img(test['id'][i].astype('str')+'.png', target_size=(28,28,1), grayscale=True)
                img = image.load_img(imagePath, target_size=(28,28,1), grayscale=True)
                img = image.img_to_array(img)
                img = img/255
                test_image.append(img)
            test = np.array(test_image)
            model = load_kmodel()
            prediction = model.predict_classes([test])
            # CLEARING SESSION FOR MODEL TO LOAD AGAIN
            K.clear_session()

            # RETURNING PREDICTION
            return jsonify({
                "prediction":str(prediction[0])
            })
    # if request.method == 'POST'
    # content = request.json


    #
    return jsonify({
        "prediction":"test 1"
    })


if __name__== '__main__':
    app.run(debug=True)
