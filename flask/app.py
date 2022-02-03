from flask import Flask, jsonify
from celery_app import run_train, prediction

from sqlalchemy.orm import load_only
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://postgres:postgres@db:5432/postgres'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


@app.route("/app/predict/<text>", methods=['POST'])
def predict_data(text):
    result = prediction(text).tolist()
    return {
        "result":result
    }



@app.route("/app/train", methods=['GET'])
def train_data():
    text, label = get_data()
    task = run_train.delay(text,label)
    return "Task state is " + task.state


class Data(db.Model):
    __tablename__ = "data_data"
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String)
    label = db.Column(db.String)


def get_data():
    datas = Data.query.options(load_only('text', 'label')).all()
    texts = []
    labels = []
    for data in datas:
        texts.append(data.text)
        labels.append(data.label)

    return texts, labels


if __name__ == "__main__":
    app.run(debug=True)
