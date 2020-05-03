# -*-coding:utf-8-*-
from PIL import Image
import os
import sys
def pinjie(im):
    x = 200
    y = 240
    w = 1600
    h = 400
    region = im.crop((x, y, x+w, y+h))
    img_size = region.size

# 第1块
    w = img_size[0]/2.0
    h = img_size[1]
    x = 0
    y = 0
    region1 = region.crop((x, y, x+w, y+h))
#region1.save("./crop_average-1.jpeg")
# 第2块
    x = w
    y = 0
    region2 = region.crop((x, y, x+w, y+h))
#region2.save("./crop_average-2.jpeg")
    width, height = region1.size
    blackIMG = Image.new(region1.mode,(width,height*2))

    blackIMG.paste(region1,box=(0,0))
    blackIMG.paste(region2,box=(0,height))
    #blackIMG.save('res.jpg')
    return blackIMG

if __name__ == '__main__':
    dir_path = 'D:/Spyder/zhuanluliangang/data/dataset2test_1920'
    re_dir_path = 'D:\Spyder\zhuanluliangang\data\heyuxiacroptest'
    #img = Image.open("image_00249.jpg")
    
    for class_name in os.listdir(dir_path):
        re_class_path = os.path.join(re_dir_path,class_name)
        dir_class_path = os.path.join(dir_path,class_name)
        if not os.path.exists(re_class_path):
            os.mkdir(re_class_path)   #建文件夹
        for file_name in os.listdir(dir_class_path):
            re_file_name = os.path.join(re_class_path,file_name)
            dir_file_name = os.path.join(dir_class_path,file_name)
            if not os.path.exists(re_file_name):
                os.mkdir(re_file_name)   #建文件夹
            for img_name in os.listdir(dir_file_name):
                img = Image.open(os.path.join(dir_file_name,img_name))
                img = pinjie(img)
                img.save(re_file_name+'\\'+img_name)


        

        

    
    