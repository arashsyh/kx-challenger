import flask
from flask import request
from flask_api import status
from classifier import Model
import pandas as pd


app = flask.Flask(__name__)
app.config["DEBUG"] = True


@app.route('/upload', methods=['POST'])
def upload():
    # Todo: limit file size
    global train_data
    uploaded_file = request.files['file']
    if not uploaded_file.filename:
        return "No file is uploaded.", status.HTTP_400_BAD_REQUEST
    elif uploaded_file.filename.split('.')[1] != 'csv':
        return "The file format is not valid. Please upload a csv file.", status.HTTP_400_BAD_REQUEST
    train_data = pd.read_csv(uploaded_file)
    return "File Uploaded Successfully"


@app.route('/train', methods=['GET'])
def train():
    model = Model(train_data)
    model.pre_process()
    result = model.fit()
    return str(result)



app.run()