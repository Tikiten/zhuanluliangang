# -*- coding: utf-8 -*-
"""
Created on Fri Mar 20 16:23:29 2020

@author: PC
"""

#coding=utf-8  
  
import os
path = 'D:/Desktop/dataset2/penjian'
count = 1
for file in os.listdir(path):
    os.rename(os.path.join(path,file),os.path.join(path,"penjian_"+str(count)+".mp4"))
    count+=1