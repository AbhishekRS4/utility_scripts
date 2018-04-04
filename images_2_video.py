'''
@author : Abhishek R S
'''

import os
import numpy as np
import cv2

# source directory which contains all the images which need to be converted to a video
# destination directory where the video has to be saved
# video_file_name with which the video has to be saved
# image_format looks for .jpg, .png etc.
src_directory = "."
dst_directory = "."
video_file_name = "output.avi"
image_format = ".png"

# fps of the video
frames_per_second = 10

# dimension of the video
video_dimension = (640, 480)

'''
XVID - preferred
X264
DIVX
MJPG are other video encoders
'''


def main():
	# video_writer is a Video Writer object
	video_writer = cv2.VideoWriter(os.path.join(dst_directory, video_file_name), cv2.VideoWriter_fourcc(*"XVID"), frames_per_second, video_dimension)
	
	# list all the required frames for the video
	list_images = [x for x in os.listdir(src_directory) if x.endswith(image_format)]

	print("Number of files to be converted into a video : " + str(len(list_images)))

	# convert the frames to video
	for img_name in list_images:
		try:
			video_writer.write(cv2.imread(os.path.join(src_directory, img_name)))
		except IOError:
			print("File not an image or corrupted")

	# release the Video Writer object
	video_writer.release()

	print("Video has been successfully created in : " + dst_directory)


if __name__ == '__main__':
	main()