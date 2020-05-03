# -*- coding: utf-8 -*-
"""
Created on Wed Jan 15 16:26:29 2020

@author: PC
"""
import os

file_path = "D:/Spyder/zhuanluliangang/data/heyuxiacroptest/pianhua"
# os.listdir(file)会历遍文件夹内的文件并返回一个列表
path_list = os.listdir(file_path)
# print(path_list)
# 定义一个空列表,我不需要path_list中的后缀名
path_name=[]
# 利用循环历遍path_list列表并且利用split去掉后缀名
for i in path_list:
    path_name.append(i.split(".")[0])

# 排序一下
path_name.sort()

for file_name in path_name:
    # "a"表示以不覆盖的形式写入到文件中,当前文件夹如果没有"save.txt"会自动创建
    with open("pianhua_list.txt","a") as f:
        f.write('pianhua/'+file_name + "\n")
        # print(file_name)
    f.close()

file_path = "D:/Spyder/zhuanluliangang/data/heyuxiacroptest/piangan"
# os.listdir(file)会历遍文件夹内的文件并返回一个列表
path_list = os.listdir(file_path)
# print(path_list)
# 定义一个空列表,我不需要path_list中的后缀名
path_name=[]
# 利用循环历遍path_list列表并且利用split去掉后缀名
for i in path_list:
    path_name.append(i.split(".")[0])

# 排序一下
path_name.sort()

for file_name in path_name:
    # "a"表示以不覆盖的形式写入到文件中,当前文件夹如果没有"save.txt"会自动创建
    with open("piangan_list.txt","a") as f:
        f.write('piangan/'+file_name + "\n")
        # print(file_name)
    f.close()
    
file_path = "D:/Spyder/zhuanluliangang/data/heyuxiacroptest/normal"
# os.listdir(file)会历遍文件夹内的文件并返回一个列表
path_list = os.listdir(file_path)
# print(path_list)
# 定义一个空列表,我不需要path_list中的后缀名
path_name=[]
# 利用循环历遍path_list列表并且利用split去掉后缀名
for i in path_list:
    path_name.append(i.split(".")[0])

# 排序一下
path_name.sort()

for file_name in path_name:
    # "a"表示以不覆盖的形式写入到文件中,当前文件夹如果没有"save.txt"会自动创建
    with open("normal_list.txt","a") as f:
        f.write('normal/'+file_name + "\n")
        # print(file_name)
    f.close()
    
file_path = "D:/Spyder/zhuanluliangang/data/heyuxiacroptest/penjian"
# os.listdir(file)会历遍文件夹内的文件并返回一个列表
path_list = os.listdir(file_path)
# print(path_list)
# 定义一个空列表,我不需要path_list中的后缀名
path_name=[]
# 利用循环历遍path_list列表并且利用split去掉后缀名
for i in path_list:
    path_name.append(i.split(".")[0])

# 排序一下
path_name.sort()

for file_name in path_name:
    # "a"表示以不覆盖的形式写入到文件中,当前文件夹如果没有"save.txt"会自动创建
    with open("penjian_list.txt","a") as f:
        f.write('penjian/'+file_name + "\n")
        # print(file_name)
    f.close()
