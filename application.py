import os

from flask import Flask, request, jsonify, make_response
import pickle as pkl

app = Flask(__name__)

# os.chdir(os.path.dirname(__file__))
# with open('model/decision_tree.pkl', 'rb') as fp:
#     model = pkl.load(fp)

# @app.route('/predict', methods=['POST'])
# def predict():
#     request_json = request.get_json()
#     predict_list = [
#         request_json["sepal_length_cm"],
#         request_json["sepal_width_cm"],
#         request_json["petal_length_cm"],
#         request_json["petal_width_cm"]
#         ]

#     prediction = model.predict([predict_list])[0]
#     return make_response(prediction, 200)


@app.route("/")
def hello():
    return "Hello, World!"

@app.route("/test")
def hello_test():
    return test.ret_message()
