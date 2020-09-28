# -*- coding: utf-8 -*-
"""
Created on Mon Sep 28 23:39:58 2020

@author: ashup
"""
import flask 
from flask import Flask,request

from Summarizer import SummarizeDoc

app= Flask(__name__)

@app.route('/Summry_home',methods=['GET'])
def finddummery():
    summarizeObj = SummarizeDoc()
    summary = summarizeObj.findSummary()
    return summary

app.run(host='localhost',port=8023) 