# -*- coding: utf-8 -*-
"""
Created on Thu Sep 24 18:03:48 2020

@author: ashup
"""

import re

class PreprocessDoc:
        """
        module for prepocessing articals
        """
    def removeSpclChar(self,text):
        """
        remove spacial chracaters
        
        input
            text:String
        output:
            modifiedtext: string
                
        """
        filtertext =re.sub(',|;|#|$','',text)
        return filtertext
    
    def convertolow(self,text):
        
        retuen text.lower()
    