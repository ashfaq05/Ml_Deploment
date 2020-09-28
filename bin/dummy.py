# -*- coding: utf-8 -*-
"""
Created on Mon Sep 28 22:43:22 2020

@author: ashup
"""

import flask 
from flask import Flask,request

app= Flask(__name__)

@app.route('/home',methods =['GET'])

def checkstause():
    return "demo project"

app.run(host='localhost',port=8023) 