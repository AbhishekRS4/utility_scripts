"""
@author : Abhishek R S
"""

import os
import sys
import cv2
import argparse
import numpy as np

def video_to_images(FLAGS):
    # create the output directory if not present
    if not os.path.isdir(FLAGS.dir_images):
        os.makedirs(FLAGS.dir_images)

    # create video capture object
    video_capture = cv2.VideoCapture(FLAGS.file_video)
    success = True

    frame_count = 10000

    print("Extracting images..........")
    while success:
        # try to extract a frame
        success, image_frame = video_capture.read()

        # if not successful then break
        if not success:
            break

        # save the successfully extracted frame
        cv2.imwrite(os.path.join(FLAGS.dir_images, FLAGS.img_prefix +
            str(frame_count) + FLAGS.img_format), image_frame)
        frame_count += 1

    print("Extracting images completed")
    print(f"Extracted images are in : {FLAGS.dir_images}")

def main():
    # video file path whose frames have to be saved
    # destination directory where the frames have to be saved
    # file name with which the frames should be saved
    # image format which should be used to save the frame
    file_video = "output.avi"
    dir_images = "."
    img_prefix = "image_"
    img_format = ".png"

    parser = argparse.ArgumentParser(
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument("--file_video", default=file_video,
        type=str, help="name for input video file")
    parser.add_argument("--dir_images", default=dir_images,
        type=str, help="path to save output images")
    parser.add_argument("--img_prefix", default=img_prefix,
        type=str, help="prefix for image names")
    parser.add_argument("--img_format", default=img_format,
        type=str, choices=[".png", ".jpg"], help="image saving format")

    FLAGS, unparsed = parser.parse_known_args()
    video_to_images(FLAGS)

if __name__ == "__main__":
    main()
