from __future__ import print_function, division
import os
import sys
import subprocess

def class_process(dir_path, dst_dir_path, class_name):
  class_path = os.path.join(dir_path, class_name)
  if not os.path.isdir(class_path):
    return

  dst_class_path = os.path.join(dst_dir_path, class_name)
  if not os.path.exists(dst_class_path):
    os.mkdir(dst_class_path)

  for file_name in os.listdir(class_path):
    if '.mp4' not in file_name:
      continue
    name, ext = os.path.splitext(file_name)
    dst_directory_path = os.path.join(dst_class_path, name)

    video_file_path = os.path.join(class_path, file_name)
    try:
      if os.path.exists(dst_directory_path):
        if not os.path.exists(os.path.join(dst_directory_path, 'image_00001.jpg')):
          subprocess.call('rm -r \"{}\"'.format(dst_directory_path), shell=True)
          print('remove {}'.format(dst_directory_path))
          os.mkdir(dst_directory_path)
        else:
          continue
      else:
        os.mkdir(dst_directory_path)
    except:
      print(dst_directory_path)
      continue
    #cmd = 'ffmpeg -i \"{}\" -vf  crop=1920:600:0:200 \"{}/image_%05d.jpg\"'.format(video_file_path, dst_directory_path)
    #cmd = 'ffmpeg -i \"{}\" -vf crop=1920:600:0:200,"select=between(n\,0\,250)*not(mod(n\,5))" -vsync 0 \"{}/image_%05d.jpg\"'.format(video_file_path, dst_directory_path)
    cmd = 'ffmpeg -i \"{}\" -vf "select=between(n\,0\,250)*not(mod(n\,5))" -vsync 0 \"{}/image_%05d.jpg\"'.format(video_file_path, dst_directory_path)

    print(cmd)
    subprocess.call(cmd, shell=True)
    print('\n')

if __name__=="__main__":
  dir_path = "D:/Desktop/dataset2test"#sys.argv[1]
  dst_dir_path = "D:/Spyder/zhuanluliangang/data/dataset2test_1920"#sys.argv[2]

  for class_name in os.listdir(dir_path):
      class_process(dir_path, dst_dir_path, class_name)
  print('OK')
#"D:/Spyder/3D-ResNets-PyTorch-master/datasets/UCF-101/"
#"D:/Spyder/3D-ResNets-PyTorch-master/datasets/UCF101_JPG/"
  #D:/Spyder/zhuanluliangang/data/videos
  #D:/Spyder/zhuanluliangang/data/jpg/
  #scale=-1:240
    #ffmpeg -i 10.mp4 -vf crop=1400:350:300:250,"select=between(n\,0\,250)*not(mod(n\,5))" -vsync 0 D:/Desktop/test/jpg/image_%05d.jpg
  #ffmpeg -i 10.mp4 -vf crop=1920:600:0:200,"select=between(n\,0\,250)*not(mod(n\,5))" -vsync 0 D:/Desktop/10/image_%05d.jpg