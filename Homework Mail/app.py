from flask import Flask, render_template, request, jsonify
import pickle

model = None
filename = "models/mail_spam_model.sav"

app = Flask(__name__)

@app.route("/")
def render_default():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():
    text = request.form.get("email", None)

    cls = model.predict([text])[0]

    if cls == 1:
        value = 'Spam'
    else:
        value = 'Not Spam'

    return jsonify(result=value)

if __name__ == "__main__":
    model = pickle.load(open(filename, 'rb'))
    app.run(host="127.0.0.1", port=8000, threaded=True, debug=True)