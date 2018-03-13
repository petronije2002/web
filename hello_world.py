#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 12 23:43:36 2018

@author: Pera
"""
from flask import Flask

app = Flask(__name__)


@app.route("/")
def index():
    return "HELLO WORLD!!"

if __name__ == '__main__':
    app.run(port=5000, debug=True)
