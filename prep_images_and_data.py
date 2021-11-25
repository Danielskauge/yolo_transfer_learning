import os
import cv2
import numpy as np
original_width = 1280
original_height = 720
img_width = 640
img_height = 360
height_scale = int(img_width/original_width)
width_scale = int(img_height/original_height)

def prep_small_images():
   myimages = os.path.join(os.getcwd(),"rgb")
   print(myimages)
   for img in os.listdir(myimages):
      image_path = cv2.imread(os.path.join(myimages,img))
      image_path = cv2.resize(image_path,(img_height,img_width))
      print(image_path.shape)
      cv2.imwrite(os.path.join(os.getcwd(),"small_images",img),
                  image_path)

def prep_train_txt():
#makes txt file with adress to each image and bounding box information
   width = 624
   height = 832
   bbox_2d_tight = os.path.join(os.getcwd(),'bbox_2d_tight')
   file_object = open('train.txt', 'a+')

   for npy_name in os.listdir(bbox_2d_tight): #returns file names as strings
      with open(os.path.join(bbox_2d_tight,npy_name)) as f:
         npy = np.load('f',allow_pickle=True)
         x1 , y1 , x2 , y2 = npy[5], npy[6], npy[7], npy[8]
         x1 , y1 , x2 , y2 = int(x1*width_scale) , int(y1*height_scale) , int(x2*width_scale) , int(y2*height_scale)

         small_img_name = npy_name[:-3] + 'jpg'
         text = ('small_images/' + small_img_name + ' ' + str(x1) + ' '
                + ', ' +  str(y1) + ',' + str(x2) + ','
                + str(y2) + ',' + str(0) + '\n')
         file_object.write(text) # image adress and bounding box info to training text file

