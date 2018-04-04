'''
@author : Abhishek R S
'''

import os
import cv2

# source and destination directories for images that have to be resized and saved
src_images_path = "/home/user/src_images_path/"
dst_images_path = "/home/user/dst_images_path/"

# list all the image files in the source directory
image_format = ".png"
src_images_list = [x for x in os.listdir(src_images_path) if x.endswith(image_format)]

# set target image size and interpolation to use for resize
target_image_size = (640, 480)
interpolation = cv2.INTER_LINEAR

# resize the images and save in the destination directory
for img_file in src_images_list:
	img = cv2.imread(os.path.join(src_images_path, img_file))
	img = cv2.resize(img, target_image_size, interpolation = interpolation)
	cv2.imwrite(os.path.join(dst_images_path, img_file), img)
