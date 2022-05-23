# -*- coding: utf-8 -*-
"""
Created on Thu May 19 16:58:41 2022

@author: nomut
"""
import class_path

class Class_checker():
    """
    
    """
    def __init__(self):
        pass
    
    
    
    def is_int(self,data):
        return type(data)==int
    
    def is_float(self,data):
        return type(data)==float
    
    def is_str(self,data):
        return type(data)==str
    
    def is_list(self,data):
        return type(data)==list
    
    def is_tuple(self,data):
        return type(data)==tuple
    
    def is_Paths(self,data):
        return type(data)==class_path.Paths
    
    