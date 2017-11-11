from datetime import datetime
from flask import Flask, render_template, jsonify
from sklearn.externals import joblib

app = Flask(__name__)
clf = joblib.load('models/randomtree-10-4-2017-11-11.pkl')


@app.route('/')
def index():
    return render_template('index.html')


def _predict(time=None):
    if time is None:
        time = datetime.now()
    dow = time.weekday()
    hour = time.hour
    minute = time.minute + hour * 60
    # // is integer division
    m5 = minute // 5
    m2 = minute // 2
    m15 = minute // 15
    m30 = minute // 30
    now = [[dow, minute, hour, m5, m2, m15, m30]]
    return list(zip(clf.classes_, clf.predict_proba(now)[0]))


@app.route('/prediction/')
def predict():
    # json.dumps doesn't know how to handle numpy int64s,
    # but fortunately the repr of `predict` happens to be valid json
    prediction = _predict()
    response = jsonify([
        float(prediction[0][1]),
        float(prediction[1][1]),
    ])
    # Make sure this won't be cached for more than a minute
    response.cache_control.max_age = 60
    return response


if __name__ == '__main__':
    app.run(host='0.0.0.0')
