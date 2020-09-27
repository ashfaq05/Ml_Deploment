# -*- coding: utf-8 -*-
"""
Created on Thu Sep 24 18:05:02 2020

@author: ashup
"""
import yaml
import numpy as np
import pandas as pd

class SummarizeDoc:
    def __init__(self):
        with open('../config/config.yml','r') as f1:
            self.config = yaml.load(f1)
            
        
    def lodedocs(self,filepath):
        with open(filepath,'r') as f1:
            text = f1.read()
        return text
        
    
    def splitSentences(self,text):
        
        sentences=text.split('.')
        return sentences
    
    def groupSentences(self,sentences):
        firstsent,restofsent = sentences[0],sentences[1:]
        
        return firstsent ,restofsent
    
    def findsentlength(self,text):
        return text.split()
    def findsentlentarray(self,sentences):
        return [self.findsentlength(sent) for sent in sentences]
    
    def findtopsent(self,sentlength,sentences,n):
        sotedidx = np.argsort(sentlength)
        topidx = sotedidx[-n:]
        topsent = [sentlength[i] for i in topidx]
        return topsent
    
    def finssummery(self):
        filepath = self.config['data_path']['train_data']
        text =self.lodedocs(filepath)
        sentences = self.splitSentences(text)
        firstsent,restofsent =self.groupSentences(sentences)
        sentlents = self.findsentlentarray(restofsent)
        topsentenses =self.findtopsent(sentlents,restofsent,self.config['sentene_num])
        allsent = [firstsent]+ topsentenses
        summery =' '.join(allsent)
        return summery
    
    
summarizeOBJ = SummarizeDoc()





    
    