# -*- coding: utf-8 -*-
"""
Created on Tue Jan  7 19:56:04 2020

@author: PC
"""

import random
 
with open("D:/Spyder/zhuanluliangang/data/normal_list.txt", 'rt') as f:
    dataset = [line for line in f.readlines()]

# 乱序
random.shuffle(dataset)
 
# [训练集, 测试集]
pos = round(len(dataset) *.1)
trainset = dataset[:pos]
testset = dataset[pos:]
with open('D:/Spyder/zhuanluliangang/data/normal_train.txt','w') as file_handle:   # .txt可以不自己新建,代码会自动新建
    for k in trainset:
        file_handle.write(str(k))     # 写入
        
with open('D:/Spyder/zhuanluliangang/data/normal_test.txt','w') as file_handle:   # .txt可以不自己新建,代码会自动新建
    for k in testset:
        file_handle.write(str(k))     # 写入

with open("D:/Spyder/zhuanluliangang/data/piangan_list.txt", 'rt') as f:
    dataset = [line for line in f.readlines()]

# 乱序
random.shuffle(dataset)
 
# [训练集, 测试集]
pos = round(len(dataset) *.1)
trainset = dataset[:pos]
testset = dataset[pos:]
with open('D:/Spyder/zhuanluliangang/data/piangan_train.txt','w') as file_handle:   # .txt可以不自己新建,代码会自动新建
    for k in trainset:
        file_handle.write(str(k))     # 写入
        
with open('D:/Spyder/zhuanluliangang/data/piangan_test.txt','w') as file_handle:   # .txt可以不自己新建,代码会自动新建
    for k in testset:
        file_handle.write(str(k))     # 写入

with open("D:/Spyder/zhuanluliangang/data/pianhua_list.txt", 'rt') as f:
    dataset = [line for line in f.readlines()]

# 乱序
random.shuffle(dataset)
 
# [训练集, 测试集]
pos = round(len(dataset) *.1)
trainset = dataset[:pos]
testset = dataset[pos:]
with open('D:/Spyder/zhuanluliangang/data/pianghua_train.txt','w') as file_handle:   # .txt可以不自己新建,代码会自动新建
    for k in trainset:
        file_handle.write(str(k))     # 写入
        
with open('D:/Spyder/zhuanluliangang/data/pianghua_test.txt','w') as file_handle:   # .txt可以不自己新建,代码会自动新建
    for k in testset:
        file_handle.write(str(k))     # 写入
        
        
with open("D:/Spyder/zhuanluliangang/data/penjian_list.txt", 'rt') as f:
    dataset = [line for line in f.readlines()]

# 乱序
random.shuffle(dataset)
 
# [训练集, 测试集]
pos = round(len(dataset) *.1)
trainset = dataset[:pos]
testset = dataset[pos:]
with open('D:/Spyder/zhuanluliangang/data/penjian_train.txt','w') as file_handle:   # .txt可以不自己新建,代码会自动新建
    for k in trainset:
        file_handle.write(str(k))     # 写入
        
with open('D:/Spyder/zhuanluliangang/data/penjian_test.txt','w') as file_handle:   # .txt可以不自己新建,代码会自动新建
    for k in testset:
        file_handle.write(str(k))     # 写入

