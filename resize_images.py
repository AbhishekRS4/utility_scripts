"""
@author : Abhishek R S
"""

import os
import sys
import cv2
import argparse

def resize_images(FLAGS):
    # create the output directory if not present
    if not os.path.isdir(FLAGS.dir_out):
        os.makedirs(FLAGS.dir_out)

    # list all the image files in the source directory
    src_images_list = [f for f in os.listdir(
        FLAGS.dir_src) if f.endswith(FLAGS.img_format)]

    # set target image size and interpolation to use for resize
    target_image_size = (FLAGS.width, FLAGS.height)
    interpolation = cv2.INTER_LINEAR

    print(f"number of images to process : {len(src_images_list)}")
    print("resizing images started")

    # resize the images and save in the destination directory
    for img_file in src_images_list:
        img = cv2.imread(os.path.join(FLAGS.dir_src, img_file))
        img = cv2.resize(img, target_image_size, interpolation=interpolation)
        cv2.imwrite(os.path.join(FLAGS.dir_out, img_file), img)

    print("resizing images completed")
    print(f"resized images are in : {FLAGS.dir_out}")

def main():
    # source and destination directories for images that have to be resized and saved
    dir_src = "/home/user/dir_src/"
    dir_out = "/home/user/dir_out/"
    height = 480
    width = 640
    img_format = ".png"

    parser = argparse.ArgumentParser(
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument("--dir_src", default=dir_src,
        type=str, help="path to load original images")
    parser.add_argument("--dir_out", default=dir_out,
        type=str, help="path to save resized images")
    parser.add_argument("--height", default=height,
        type=int, help="height of the image")
    parser.add_argument("--width", default=width, type=int,
        help="width of the image")
    parser.add_argument("--img_format", default=img_format,
        type=str, choices=[".png", ".jpg"], help="image pattern .png or .jpg etc.")

    FLAGS, unparsed = parser.parse_known_args()
    resize_images(FLAGS)

if __name__ == "__main__":
    main()
