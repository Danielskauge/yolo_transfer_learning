import os
import cv2
import numpy as np
original_width = 1280
original_height = 720
img_width = 624
img_height = 832
height_scale = float(img_width/original_width)
width_scale = float(img_height/original_height)


def prep_train_txt():
   #makes txt file with adress to each image and bounding box information
   print(height_scale)
   print(width_scale)
   bbox_2d_tight = os.path.join(os.getcwd(),'bbox_2d_tight')
   file_object = open('train.txt', 'w')
   
   for npy_name in os.listdir(bbox_2d_tight): #returns file names as strings
        bbox_path = os.path.join(bbox_2d_tight,npy_name)
        rgb_path = os.path.join(os.getcwd(),'small_images',npy_name[:-3] + 'png')
        npy = np.load(bbox_path,allow_pickle=True)

        if(len(npy) != 0):

            x1 , y1 , x2 , y2 = npy[0][6], npy[0][7], npy[0][8], npy[0][9]
            x1 , y1 , x2 , y2 = int(x1*width_scale) , int(y1*height_scale) , int(x2*width_scale) , int(y2*height_scale)
            print(npy)
            small_img_name = npy_name[:-3] + 'jpg'
            text = ('small_images/' + small_img_name + ' ' + str(x1)
                    + ',' +  str(y1) + ',' + str(x2) + ','
                    + str(y2) + ',' + str(0) + '\n')
            file_object.write(text) # image adress and bounding box info to training text file
prep_train_txt()