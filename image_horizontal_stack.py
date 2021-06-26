"""
@author : Abhishek R S
"""

import os
import sys
import cv2
import argparse
import numpy as np

def horizontal_stack_images(FLAGS):
    dir_images = FLAGS.dir_images
    dir_overlays = FLAGS.dir_overlays
    dir_stacked = FLAGS.dir_stacked
    img_format = FLAGS.img_format

    if not os.path.isdir(FLAGS.dir_stacked):
        os.makedirs(FLAGS.dir_stacked)

    # list of all images
    target_image_files = [f for f in os.listdir(
        FLAGS.dir_images) if f.endswith(FLAGS.img_format)]
    target_image_files.sort()

    # combine image and overlay and save the output image
    for img_file in target_image_files:
        image_path = os.path.join(FLAGS.dir_images, img_file)
        overlay_path = os.path.join(FLAGS.dir_overlays, img_file)
        output_path = os.path.join(FLAGS.dir_stacked, img_file)

        img1 = cv2.imread(image_path)
        img2 = cv2.imread(overlay_path)

        img_stacked = np.hstack((img1, img2))

        cv2.imwrite(output_path, img_stacked)

def main():
    # image, overlay and output directories
    # image format
    dir_images = "/home/user/dir_images/"
    dir_overlays = "/home/user/dir_overlays/"
    dir_stacked = "/home/user/dir_stacked/"
    img_format = "png"

    parser = argparse.ArgumentParser(
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument("--dir_images", default=dir_images,
        type=str, help="path to load original images")
    parser.add_argument("--dir_overlays", default=dir_overlays,
        type=str, help="path to load corresponding overlay images")
    parser.add_argument("--dir_stacked", default=dir_stacked,
        type=str, help="path to save horizontally stacked images")
    parser.add_argument("--img_format", default=img_format, type=str,
        choices=["jpg", "png"], help="image format, png or jpg etc.")

    FLAGS, unparsed = parser.parse_known_args()
    horizontal_stack_images(FLAGS)

main()
