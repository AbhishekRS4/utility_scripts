'''
@author : Abhishek R S
'''

import os
import numpy as np
import cv2

# source directory which contains the video
# destination directory where the frames have to be saved
# video file name whose frames have to be saved
# file name with which the frames should be saved
# image format which should be used to save the frame
src_video_directory = "."
dst_video_directory = "."
src_video_name = "output.avi"
frame_name = "frame_"
image_format = ".png"

def main():
	# create video capture object
	video_capture = cv2.VideoCapture(os.path.join(src_video_directory, src_video_name))
	success = True

	frame_count = 0

	print("Extracting Frames.........")
	while success:
		# try to extract a frame
		success, image_frame = video_capture.read()

		# if not successful then break
		if not success:
			break

		# save the successfully extracted frame
		cv2.imwrite(os.path.join(dst_video_directory, (frame_name + str(frame_count) + image_format)), image_frame)
		frame_count += 1
	
	print("Extracting Frames Completed")
	print("")

if __name__ == "__main__":
	main()