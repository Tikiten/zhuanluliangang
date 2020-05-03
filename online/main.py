from __future__ import print_function, division
import os
import shutil
import subprocess
import time
import torch
from subprocess import check_output
from PIL import Image
from ucf101_json import convert_ucf101_csv_to_activitynet_json
from model_process import model_process
from opts import parse_opts
from model import generate_model
  
def n_frames_generate(dir_path, fake_label):
  class_path = os.path.join(dir_path, fake_label)
  if not os.path.isdir(class_path):
    return

  for file_name in os.listdir(class_path):
    video_dir_path = os.path.join(class_path, file_name)
    image_indices = []
    for image_file_name in os.listdir(video_dir_path):
      if 'image' not in image_file_name:
        continue
      image_indices.append(int(image_file_name[6:11]))

    if len(image_indices) == 0:
      print('no image files', video_dir_path)
      n_frames = 0
    else:
      image_indices.sort(reverse=True)
      n_frames = image_indices[0]
      #print(video_dir_path, n_frames)
    with open(os.path.join(video_dir_path, 'n_frames'), 'w') as dst_file:
      dst_file.write(str(n_frames))
    
def read_to_txt(file_path, class_name):
    class_path = os.path.join(file_path, class_name)
    
    # os.listdir(file)会历遍文件夹内的文件并返回一个列表
    path_list = os.listdir(class_path)
    # print(path_list)
    # 定义一个空列表,不需要path_list中的后缀名
    path_name = []
    # 利用循环历遍path_list列表并且利用split去掉后缀名
    for i in path_list:
        path_name.append(i.split(".")[0])
    # 排序一下
    path_name.sort()
    
    for file_name in path_name:
        # "a"表示以不覆盖的形式写入到文件中,当前文件夹如果没有txt会自动创建
        with open("data/"+'test'+".txt", "a") as f:
            f.write(class_name+'/'+file_name + "\n")
            # print(file_name)
        f.close()
        
def crop(im):
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
    blackIMG = Image.new(region1.mode, (width, height*2))

    blackIMG.paste(region1, box=(0, 0))
    blackIMG.paste(region2, box=(0, height))
    #blackIMG.save('res.jpg')
    return blackIMG


if __name__ == "__main__":
    '''
    dir_path:place the original video
    dst_dir_path:place the 50 frames of the 10-second video
    re_dir_path:place the cropped frames
    '''
    
    dir_path = "D:/Spyder/zhuanluliangang_online/data/demo_video"
    dst_dir_path = "D:/Spyder/zhuanluliangang_online/data/demo_jpg_org"
    re_dir_path = 'D:/Spyder/zhuanluliangang_online/data/demo_jpg_crop'
    
    #create temporary folders if they do not exist
    if not os.path.exists(dst_dir_path):
        os.mkdir(dst_dir_path)   
     
    if not os.path.exists(re_dir_path):
        os.mkdir(re_dir_path)   
    
    if not os.path.isdir(dir_path):
        print("wrong")
    
    for file_name in os.listdir(dir_path):
      #check the video format
      if '.avi' not in file_name:
          continue
      
      video_file_path = os.path.join(dir_path, file_name)
      #new_video_file_path = os.path.join(crop_dir_path, file_name)
     
      #get duration of a video for Windows
      get_duration = str(check_output('ffprobe -i  "'\
                                      + video_file_path \
                                          +'" 2>&1 |findstr "Duration"', shell=True)) 
          
      #For Linux
      #a = str(check_output('ffprobe -i  "'+file_name+'" 2>&1 |grep "Duration"',shell=True)) 
      get_duration = get_duration.split(",")[0].split("Duration:")[1].strip()
      hour, minute, second = get_duration.split(':')
      duration = int(hour) * 3600 + int(minute) * 60 + float(second)
      #print(duration)
      
      opt = parse_opts() 
      
      #delete previous testing results
      result_path = os.path.join(opt.result_path, 'pr_label.txt')
      if os.path.exists(result_path):
          os.remove(result_path)
          
      #build model  
      model, parameters = generate_model(opt)
      
      opt.arch = '{}-{}'.format(opt.model, opt.model_depth)
      if opt.resume_path:
        print('loading checkpoint {}'.format(opt.resume_path))
        checkpoint = torch.load(opt.resume_path)
        assert opt.arch == checkpoint['arch']

        opt.begin_epoch = checkpoint['epoch']
        model.load_state_dict(checkpoint['state_dict'])
      
      #start processing
      gap = 2
      for start_time in range(0, int(duration)-9, gap):
        start0 = time.time()
        #delete temporary video and frames
        '''shutil.rmtree(dst_dir_path)  
        os.mkdir(dst_dir_path) '''
      
        startcmd = time.time()
        #turn the temporary video into a sequence of 5 frames per second
        speed = 5
        cmd = 'ffmpeg -ss '+ str(start_time)\
            +' -t 10 ' +'-i \"{}\"'.format(video_file_path) \
                + ' -vf "select=between(n\,0\,250)*not(mod(n\,{}))" -vsync 0 \"{}\image_%05d.jpg\"'\
            .format(speed, dst_dir_path)
        #print("cmd is",cmd)
        #print("\n")
        subprocess.call(cmd, shell=True)

        end = time.time() - startcmd
        print("ffmpeg time:", end)
        #print('\n')
        
        #print("video to jpg is done!") 
        
        #crop to square 
        #choose fake_label(anyone of [normal,piangan,pianhua,penjian])
        fake_label = 'normal'
        
        re_class_path = os.path.join(re_dir_path, fake_label)
        dir_class_path = os.path.join(dst_dir_path, fake_label)
        if not os.path.exists(re_class_path):
            os.mkdir(re_class_path)   #建文件夹
        
        croping = 0
        saving = 0
        for i in os.listdir(dir_path):
            file_name = i.split(".")[0]
            re_file_name = os.path.join(re_class_path, file_name)
            dir_file_name = os.path.join(dir_class_path, file_name)
            if not os.path.exists(re_file_name):
                os.mkdir(re_file_name)   #建文件夹
            for img_name in os.listdir(dst_dir_path):
                img = Image.open(os.path.join(dst_dir_path, img_name))
                
                start1 = time.time()
                img = crop(img)
                c = time.time() - start1
                croping = croping + c
                
                start2 = time.time()
                img.save(re_file_name+'\\'+img_name)    
                s = time.time() - start2
                saving = saving + s

        #print("temp",start_time,"crop is done!")

        print("croping time:", croping)
        print("saving time:", saving)
        #generate test.txt
        read_to_txt(re_dir_path, fake_label)
        #print("test.txt is generated!")
        
        #generate n_frames
        n_frames_generate(re_dir_path, fake_label)
        #print("n_frames is generated!")

        #generate labels
        csv_dir_path = 'data/'#sys.argv[1]
        label_csv_path = os.path.join(csv_dir_path, 'classInd.txt')
        #train_csv_path = os.path.join(csv_dir_path, 'train.txt')
        val_csv_path = os.path.join(csv_dir_path, 'test.txt')
        dst_json_path = os.path.join(csv_dir_path, 'label.json')
        
        #print("here")
        convert_ucf101_csv_to_activitynet_json(label_csv_path, val_csv_path, dst_json_path)
        #print('video_process is done!')
        #testing
        preprocessing = time.time() - start0
        print("preprocessing time:", preprocessing)
        
        start4 = time.time()
        model_process(start_time, model)
        testing = time.time() - start4
        print("testing time:", testing)
        
        os.remove(val_csv_path)  
        os.remove(dst_json_path)
        total_time = preprocessing + testing

        print("temp", start_time, "is done!", "using time:%2f"%total_time, "s.")
        print("\n")
        
    #empty folders
    shutil.rmtree(dst_dir_path)  
    #os.mkdir(dst_dir_path) 
    shutil.rmtree(re_dir_path)  
    #os.mkdir(re_dir_path) 
    print('OK')
  