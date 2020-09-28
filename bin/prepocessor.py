# -*- coding: utf-8 -*-
"""
Created on Thu Sep 24 18:03:48 2020

@author: ashup
"""

import re

class PreprocessDoc:
    """
    Module for preprocessin articles
    """
    def removeSpclChar(self,text):
        """
        Remove special Characters
        
        Input:
            text: string
        Output:
            modifiedText: string
        """
        filteredText = re.sub(',|;|#|$|\|/','',text)
        return filteredText

    def convertToLower(self,text):
        return text.lower()