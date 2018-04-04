'''
@author : Abhishek R S
'''

import os
import numpy as np
import cv2

# source images and masks directory
src_image_directory = "inputs"
src_mask_directory = "masks"

# alpha value to control transparency of the mask
alpha = 0.2

# list all images
image_format = ".png"
list_images = [x for x in os.listdir(src_image_directory) if x.endswith(image_format)]

def main():
	counter = 0

	# run the visualizer in loop
	while(1):
		try:
			# read the image and the correspoding mask
			img = cv2.imread(os.path.join(src_image_directory, list_images[counter]))
			mask = cv2.imread(os.path.join(src_mask_directory, list_images[counter].replace('rs', 'mask')))

			# retain green channel of the mask
			mask[:, :, 0] = mask[:, :, 2] = 0

			# create a temp copy of the original image
			img_copy = img.copy()

			# create image-mask overlay with alpha which controls transparency
			overlay = cv2.addWeighted(img_copy, 1, mask, alpha, 0, img)

			# show the overlay
			cv2.imshow("Image Visualizer - " + str(list_images[counter]), overlay)
			
			# get the key pressed
			key_pressed = cv2.waitKey(0)
			
			#print(key_pressed)

			# if down arrow is pressed increase the counter
			# if up arrow is pressed decrease the counter
			# if 'q' is pressed quit the visualizer
			if key_pressed == 1:
				counter += 1
			elif key_pressed == 0:
				counter -= 1
			elif key_pressed == 113:
				cv2.destroyAllWindows()
				break

			cv2.destroyAllWindows()	
		except IOError:
			#print(3)
			print("File not an image or image file is corrupt")

		# handle the edge cases
		if counter >= len(list_images):
			counter = len(list_images) - 1

		if counter < 0:
			counter = 0

	
if __name__ == "__main__":
	main()