# -*- coding: utf-8 -*-

from flask import Flask, request, redirect, url_for
from flask_cors import CORS

from app.main.service import gservice


app = Flask(__name__)
CORS(app)


@app.route('/match', methods = ['POST'])
def get_match():
    content = request.get_json()
    user_id = content['user_id']
	sex = content['sex']
	job = contente['job']
	pets = content['pets']
	interests = content['interests']
	other_interests = content['other_interests']
    data = gservice.get_match(user_id,sex,job,pets,interests,other_interests)
    return data


if __name__ == '__main__':

    app.run(host = '0.0.0.0', debug = True)
