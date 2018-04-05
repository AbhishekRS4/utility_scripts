'''
@author : Abhishek R S
'''

import os
import numpy as np
import cv2

# source images directory
# lbl directory
# lbl predicted file - .npy file
src_image_directory = "/home/user/src_images_path/"
lbl_directory = "/home/user/lbl_directory/"
lbl_predicted_file = "predicted_labels_dict.npy"


# load the lbl predicted file
predicted_labels = np.load(os.path.join(lbl_directory, lbl_predicted_file)).item()


# font of the label to be displayed
# text position
# text scale
# text color
# line type
font = cv2.FONT_HERSHEY_SIMPLEX
text_position = (20, 20)
font_scale = 1
font_color = (255, 255, 255)
line_type = 2


# image format
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

			# put the label as text on the image
			cv2.putText(img, "Label : " + str(predicted_labels[list_images[counter]]), text_position, font, font_scale, font_color, line_type)

			# show the resulting image
			cv2.imshow("Image Visualizer - " + str(list_images[counter]), img)
			
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
			print("File not an image or image file is corrupt")

		# handle the edge cases
		if counter >= len(list_images):
			counter = len(list_images) - 1

		if counter < 0:
			counter = 0

	
if __name__ == "__main__":
	main()