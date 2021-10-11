#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 22 10:29:45 2021

@author: vaibhavsaxena
"""
from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
import json
import os
from hb_classification import *

app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False

@app.route('/')
def index():
    return json.dumps({'version': '3.0',
                       'last-update': '22/09/2021 10:50:20'})

@app.route('/upload')
def upload():
   return render_template('upload.html')       


@app.route('/static_del')
def del_files():
    path = './static/'
    with os.scandir(path) as it:
        for entry in it:
            if entry.is_file():
                os.unlink(os.path.join(path, entry.name))
    return "Success"     


@app.route('/hardboards', methods = ['GET', 'POST'])
def upload_file():
   if request.method == 'POST':
      img = request.files['image']
      #file = secure_filename(img.filename)
      path = './static/main.jpg'
      img.save(path)
      results = predictions(path)
      return {'Grade': results}

    
if __name__ == '__main__':
    # Only for debugging while developing
    server_port = os.environ.get('PORT', '5000')
    app.run(host='0.0.0.0', port=server_port)
