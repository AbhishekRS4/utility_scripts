"""
@author : Abhishek R S
"""

import os
import sys
import cv2
import argparse
import numpy as np

def image_mask_overlay_generator(FLAGS):
    if not os.path.isdir(FLAGS.dir_overlays):
        os.makedirs(FLAGS.dir_overlays)

    # list of all images
    target_image_files = [f for f in os.listdir(
        FLAGS.dir_images) if f.endswith(FLAGS.img_format)]
    target_image_files.sort()

    # overlay image and mask and save the output image
    for img_file in target_image_files:
        image_path = os.path.join(FLAGS.dir_images, img_file)
        mask_path = os.path.join(FLAGS.dir_masks, img_file)
        output_path = os.path.join(FLAGS.dir_overlays, img_file)

        img = cv2.cvtColor(cv2.imread(image_path), cv2.COLOR_BGR2RGB)
        mask = cv2.cvtColor(cv2.imread(mask_path), cv2.COLOR_BGR2RGB)

        img_copy = img.copy()
        img_mask_overlay = cv2.addWeighted(img_copy, 1, mask, FLAGS.alpha, 0, img)
        img_mask_overlay = cv2.cvtColor(img_mask_overlay, cv2.COLOR_BGR2RGB)

        cv2.imwrite(output_path, img_mask_overlay)

def main():
    # image, masks and output directories
    # image format
    # alpha, 0.0 - 1.0
    dir_images = "/home/user/dir_images/"
    dir_masks = "/home/user/dir_masks/"
    dir_overlays = "/home/user/dir_overlays/"
    img_format = "png"
    alpha = 0.2

    parser = argparse.ArgumentParser(
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument("--dir_images", default=dir_images,
        type=str, help="path to load images")
    parser.add_argument("--dir_masks", default=dir_masks,
        type=str, help="path to load corresponding masks")
    parser.add_argument("--dir_overlays", default=dir_overlays,
        type=str, help="path to save overlay images")
    parser.add_argument("--img_format", default=img_format, type=str,
        choices=["jpg", "png"], help="image format, png or jpg etc.")
    parser.add_argument("--alpha", default=alpha, type=float,
        help="alpha (float 0.0-1.0) to control transparency of masks")

    FLAGS, unparsed = parser.parse_known_args()
    image_mask_overlay_generator(FLAGS)

main()
