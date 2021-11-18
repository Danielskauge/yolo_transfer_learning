import os
import cv2
img_width = 640
img_height = 3600

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
   width = 624
   height = 832
   small_images = os.path.join(os.getcwd(),”small_images”)
   file_object = open(‘train.txt’, ‘a’)
   for img in os.listdir(small_images):
      if img[-3:] == ‘txt’:
         with open(os.path.join(small_images,img)) as f:
            lines = f.readlines()
            ans = lines[0]
            line = ans.split(“ “)
            x1 , y1 , w , h = float(line[1]) , 
                              float(line[2]) ,      
                              float(line[3]) , 
                              float(line[4][:-1])
            x1 , y1 , w , h = x1 — w/2 , y1-h/2 , w , h
            x1 , y1 , w , h = int(x1*width) , 
                             int(y1*height) ,  
                             int(w*width) , 
                             int(h*height)
            nameee = img[:-3] + “jpg”
            img_name = os.path.join(“small_images” , nameee)
            img_name = cv2.imread(img_name)
            text = “small_images/” + nameee + “ “ + str(x1) + 
                  “,” +  str(y1) + “,” + str(x1+w) + “,” + 
                  str(y1+h) + “,” + str(0) + “\n”
            file_object.write(text)