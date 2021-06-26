"""
# @author : Abhishek R S
# script to convert camvid mask to label only for road class
"""

import os
import sys
import cv2
import argparse
import numpy as np
#from scipy.misc import imsave

def mask_to_label(FLAGS):
    # create the output directory if not present
    if not os.path.isdir(FLAGS.dir_out):
        os.makedirs(FLAGS.dir_out)

    # list of all masks
    src_mask_files = os.listdir(FLAGS.dir_src)

    print(f"number of images to be processed : {len(src_mask_files)}")
    print("mask to label conversion started\n")

    for mask_file in src_mask_files:
        mask = cv2.imread(os.path.join(FLAGS.dir_src, mask_file))
        temp_label = np.zeros(
            (mask.shape[0], mask.shape[1], 1), dtype = np.uint8)
        temp_label[:, :, 0] = 1 * \
            np.all((mask[:, :] == [0, 0, 6]), axis=2)  # road lane line
        temp_label = temp_label[:, :, 0].astype(np.uint8)

        cv2.imwrite(os.path.join(FLAGS.dir_out, mask_file), temp_label)
        #imsave(os.path.join(dir_out, mask_file), temp_label)

    print("mask to label conversion completed")
    print(f"labels are in : {FLAGS.dir_out}")

def main():
    # dir containing original carla format segmentation masks
    dir_src = "/home/abhishek/Desktop/datasets/carla/CameraRGB/"

    # dir to save lane segmentation labels
    dir_out = "/home/abhishek/Desktop/datasets/carla/CameraSeg/"

    parser = argparse.ArgumentParser(
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument("--dir_src", default=dir_src,
        type=str, help="path to load original carla segmentation labels")
    parser.add_argument("--dir_out", default=dir_out,
        type=str, help="path to save lane segmentation labels")

    FLAGS, unparsed = parser.parse_known_args()
    mask_to_label(FLAGS)

if __name__ == "__main__":
    main()
