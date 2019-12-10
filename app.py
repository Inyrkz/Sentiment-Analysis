'''flask restful api'''
#importing some libraries
import json
from flask import Flask, request, jsonify
from flask_restful import Api
import sentiment
import pickle

#load pickled model i.e model pkl
model = pickle.load(open('model.pkl', 'rb'))

app = Flask(__name__)
api = Api(app)

@app.route('/', methods=['POST'])
def predict():
    '''function under post request'''
    #Get data from Post request
    data = request.json.get('URL')
    #fit input data into get recommendation function
    sent = model(data)
    return jsonify({"Sentiment": sent})
    

if __name__ == "__main__":
    app.run(debug=True)
