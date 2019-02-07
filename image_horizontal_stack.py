'''
@author : Abhishek R S
'''

import os
import sys
import argparse
import numpy as np
import cv2


def horizontal_stack_images(FLAGS):
    src_image_dir = FLAGS.src_image_dir
    src_overlay_dir = FLAGS.src_overlay_dir
    tar_output_dir = FLAGS.tar_output_dir
    img_format = FLAGS.img_format

    if not os.path.exists(tar_output_dir):
        os.makedirs(tar_output_dir)

    # list of all images
    target_image_files = [x for x in os.listdir(
        src_image_dir) if x.endswith(img_format)]
    target_image_files.sort()

    # combine image and overlay and save the output image
    for img_file in target_image_files:
        image_path = os.path.join(src_image_dir, img_file)
        overlay_path = os.path.join(src_overlay_dir, img_file)
        output_path = os.path.join(tar_output_dir, img_file)

        img1 = cv2.imread(image_path)
        img2 = cv2.imread(overlay_path)

        img_stacked = np.hstack((img1, img2))

        cv2.imwrite(output_path, img_stacked)


def main():
    # image, overlay and output directories
    # image format
    src_image_dir = '/home/user/src_image_dir/'
    src_overlay_dir = '/home/user/src_overlay_dir/'
    tar_output_dir = '/home/user/tar_output_dir/'
    img_format = 'png'

    parser = argparse.ArgumentParser()
    parser.add_argument('-src_image_dir', default=src_image_dir,
                        type=str, help='path to load original images')
    parser.add_argument('-src_overlay_dir', default=src_overlay_dir,
                        type=str, help='path to load corresponding overlay images')
    parser.add_argument('-tar_output_dir', default=tar_output_dir,
                        type=str, help='path to save horizontally stacked images')
    parser.add_argument('-img_format', default=img_format, type=str,
                        choices=['jpg', 'png'], help='image format, png or jpg etc.')

    FLAGS, unparsed = parser.parse_known_args()
    horizontal_stack_images(FLAGS)


main()
