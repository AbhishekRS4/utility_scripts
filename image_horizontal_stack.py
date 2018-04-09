'''
@author : Abhishek R S
'''

import os
import numpy as np
import cv2

# image, overlay and output directories
target_image_directory = "/home/user/target_image_directory/"
target_overlay_directory = "/home/user/target_overlay_directory/"
target_output_directory = "/home/user/target_output_directory/"

# list of all images
image_format = ".png"
target_image_files = [x for x in os.listdir(target_image_directory) if x.endswith(image_format)]
target_image_files.sort()

# combine image and overlay and save the output image
for img_file in target_image_files:
	image_path = os.path.join(target_image_directory, img_file)
	overlay_path = os.path.join(target_overlay_directory, ("overlay_" + img_file))
	output_path = os.path.join(target_output_directory, ("out_" + img_file))

	img1 = cv2.imread(image_path)
	img2 = cv2.imread(overlay_path)
	
	img_combined = np.hstack((img1, img2))

	cv2.imwrite(output_path, img_combined)