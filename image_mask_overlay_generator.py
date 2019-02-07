'''
@author : Abhishek R S
'''

import sys
import argparse
import os
import numpy as np
import cv2


def image_mask_overlay_generator(FLAGS):
    src_image_dir = FLAGS.src_image_dir
    src_mask_dir = FLAGS.src_mask_dir
    tar_overlay_dir = FLAGS.tar_overlay_dir
    img_format = FLAGS.img_format
    alpha = FLAGS.alpha

    if not os.path.exists(tar_overlay_dir):
        os.makedirs(tar_overlay_dir)

    # list of all images
    target_image_files = [x for x in os.listdir(
        src_image_dir) if x.endswith(img_format)]
    target_image_files.sort()

    # overlay image and mask and save the output image
    for img_file in target_image_files:
        image_path = os.path.join(src_image_dir, img_file)
        mask_path = os.path.join(src_mask_dir, img_file)
        output_path = os.path.join(tar_overlay_dir, img_file)

        img = cv2.cvtColor(cv2.imread(image_path), cv2.COLOR_BGR2RGB)
        mask = cv2.cvtColor(cv2.imread(mask_path), cv2.COLOR_BGR2RGB)

        img_copy = img.copy()
        img_mask_overlay = cv2.addWeighted(img_copy, 1, mask, alpha, 0, img)
        img_mask_overlay = cv2.cvtColor(img_mask_overlay, cv2.COLOR_BGR2RGB)

        cv2.imwrite(output_path, img_mask_overlay)


def main():
    # image, masks and output directories
    # image format
    # alpha, 0.0 - 1.0
    src_image_dir = '/home/user/src_image_dir/'
    src_mask_dir = '/home/user/src_mask_dir/'
    tar_overlay_dir = '/home/user/tar_overlay_dir/'
    img_format = 'png'
    alpha = 0.2

    parser = argparse.ArgumentParser()
    parser.add_argument('-src_image_dir', default=src_image_dir,
                        type=str, help='path to load images')
    parser.add_argument('-src_mask_dir', default=src_mask_dir,
                        type=str, help='path to load corresponding masks')
    parser.add_argument('-tar_overlay_dir', default=tar_overlay_dir,
                        type=str, help='path to save overlay images')
    parser.add_argument('-img_format', default=img_format, type=str,
                        choices=['jpg', 'png'], help='image format, png or jpg etc.')
    parser.add_argument('-alpha', default=alpha, type=float,
                        help='alpha (float 0.0-1.0) to control transparency of masks')

    FLAGS, unparsed = parser.parse_known_args()
    image_mask_overlay_generator(FLAGS)


main()
