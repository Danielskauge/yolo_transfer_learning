import os
import glob
import cv2
import numpy as np
original_width = 1280
original_height = 720
img_width = 624
img_height = 832
height_scale = int(img_width/original_width)
width_scale = int(img_height/original_height)

def prep_small_images():
   original_images_path = os.path.join(os.getcwd(),"rgb")
   small_images_path = os.path.join(os.getcwd(),"small_images")

   #empties directory of altered images as not to compound tons of shit
   old_small_images = os.listdir(small_images_path)
   for img in old_small_images:
      os.remove(os.path.join(small_images_path,img))

   for img_name in os.listdir(original_images_path):
      original_image = cv2.imread(os.path.join(original_images_path,img_name))
      resized_image = cv2.resize(original_image,(img_width,img_height))
      cv2.imwrite(os.path.join(small_images_path,img_name), resized_image)

prep_small_images()
