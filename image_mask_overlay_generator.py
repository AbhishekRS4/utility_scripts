'''
@author : Abhishek R S
'''

import os
import numpy as np
import cv2

# image, masks and output directories
target_image_directory = "/home/user/target_image_directory/"
target_mask_directory = "/home/user/target_mask_directory/"
target_output_directory = "/home/user/target_output_directory/"

# list of all images
image_format = ".png"
target_image_files = [x for x in os.listdir(target_image_directory) if x.endswith(image_format)]

# alpha to control transparency of masks
alpha = 0.2

# overlay image and mask and save the output image
for img_file in target_image_files:
	image_path = os.path.join(target_image_directory, img_file)
	mask_path = os.path.join(target_mask_directory, ("mask_" + img_file))
	output_path = os.path.join(target_output_directory, ("overlay_" + img_file))  

 	img = cv2.cvtColor(cv2.imread(image_path), cv2.COLOR_BGR2RGB)
	mask = cv2.cvtColor(cv2.imread(mask_path), cv2.COLOR_BGR2RGB)

	img_copy = img.copy()
	img_mask_overlay = cv2.addWeighted(img_copy, 1, mask, alpha, 0, img)
 	img_mask_overlay = cv2.cvtColor(img_mask_overlay, cv2.COLOR_BGR2RGB)

	cv2.imwrite(output_path, img_mask_overlay)
