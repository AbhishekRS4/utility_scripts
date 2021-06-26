"""
@author : Abhishek R S
"""

import os
import sys
import cv2
import argparse
import numpy as np

def create_video(FLAGS):
    # create the output directory if not present
    if not os.path.isdir(FLAGS.dir_out):
        os.makedirs(FLAGS.dir_out)

    # video_writer is a Video Writer object
    video_writer = cv2.VideoWriter(os.path.join(
        FLAGS.dir_out, FLAGS.file_video),
        cv2.VideoWriter_fourcc(*FLAGS.video_encoder),
        FLAGS.fps, (FLAGS.width, FLAGS.height))

    # list all the required frames for the video
    list_images = [f for f in os.listdir(FLAGS.dir_src) if f.endswith(FLAGS.img_format)]
    list_images.sort()

    print("Video generation started")
    print(f"Number of images to be converted into a video : {len(list_images)}")

    # convert the frames to video
    for img_name in list_images:
        try:
            video_writer.write(cv2.imread(os.path.join(FLAGS.dir_src, img_name)))
        except IOError:
            print("File not an image or corrupted")

    # release the Video Writer object
    video_writer.release()

    print(f"{FLAGS.file_video} has been successfully created in : {FLAGS.dir_out}")

def main():
    # source directory which contains all the images which need to be converted to a video
    # output directory where the video has to be saved
    # file_video with which the video has to be saved
    # img_format looks for .jpg, .png etc.
    """
    XVID - for avi
    MP4V - for mp4
    """

    dir_src = "."
    dir_out = "."
    file_video = "output.mp4"
    video_encoder = "MP4V"
    img_format = ".png"
    height = 480
    width = 640
    fps = 10

    parser = argparse.ArgumentParser(
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument("--dir_src", default=dir_src,
        type=str, help="path to load images")
    parser.add_argument("--dir_out", default=dir_out,
        type=str, help="path to save video")
    parser.add_argument("--file_video", default=file_video,
        type=str, help="name for output video")
    parser.add_argument("--video_encoder", default=video_encoder,
        type=str, choices=["MP4V", "XVID"], help="encoder for creation of output video")
    parser.add_argument("--img_format", default=img_format,
        type=str, choices=[".png", ".jpg"], help="image pattern .png or .jpg etc.")
    parser.add_argument("--height", default=height,
        type=int, help="height of the image")
    parser.add_argument("--width", default=width, type=int,
        help="width of the image")
    parser.add_argument("--fps", default=fps, type=int,
        help="fps of output video")

    FLAGS, unparsed = parser.parse_known_args()
    create_video(FLAGS)

if __name__ == "__main__":
    main()
