import os

from flask import Flask, request, jsonify, make_response, render_template
import pickle as pkl

app = Flask(__name__)

os.chdir(os.path.dirname(__file__))
with open('model/decision_tree.pkl', 'rb') as fp:
    model = pkl.load(fp)

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')


@app.route('/predict', methods=['POST'])
def predict():
    try:
        request_dict = request.form if request.form else request.get_json()

        predict_list = [
            request_dict["sepal_length_cm"],
            request_dict["sepal_width_cm"],
            request_dict["petal_length_cm"],
            request_dict["petal_width_cm"]
            ]

        prediction = model.predict([predict_list])[0]
        return make_response( prediction, 200)

    except Exception as e:
        return make_response(str(e), 500)

@app.route("/hi")
def hello():
    return "Hello, World!"

@app.route("/list")
def hello_test():
    ls_list = os.listdir()
    return ','.join(ls_list)

if __name__ == "__main__":
    app.run()