# -*- coding: utf-8 -*-
"""
Created on Thu Sep 24 18:05:02 2020

@author: ashup
"""
import yaml

class SummarizeDoc:
    def __init__(self):
        with open('../config/config.yml','r') as f1:
            self.config = yaml.load(f1)
            
        
    def lodedocs(self):
        pass
    
    def lodconfig(self):
        pass
    
    def splitter(self):
        pass
    
summarizeOBJ = SummarizeDoc()
summarizeOBJ.lodconfig()
    
    