"""
# @author : Abhishek R S
# script to convert camvid mask to label only for road class
"""

import os
import sys
import cv2
import argparse
import numpy as np

def mask_to_label(FLAGS):
    # create the output directory if not present
    if not os.path.isdir(FLAGS.dir_out):
        os.makedirs(FLAGS.dir_out)

    # list of all masks
    src_mask_files = os.listdir(FLAGS.dir_src)

    print(f"number of masks to convert to labels : {len(src_mask_files)}")
    print("mask to label conversion started\n")

    for mask_file in src_mask_files:
        mask = cv2.imread(os.path.join(FLAGS.dir_src, mask_file))
        temp_label = np.zeros(
            (mask.shape[0], mask.shape[1], 1), dtype=np.int32)
        temp_label[:, :, 0] = 1 * \
            np.all((mask[:, :] == [192, 128, 0]), axis=2) # bicyclist
        temp_label[:, :, 0] += 2 * \
            np.all((mask[:, :] == [128,  0, 64]), axis=2) # car
        temp_label[:, :, 0] += 3 * \
            np.all((mask[:, :] == [64, 128, 192]), axis=2) # person
        temp_label[:, :, 0] += 3 * \
            np.all((mask[:, :] == [0,  64,  64]), axis=2) # person
        temp_label[:, :, 0] += 4 * \
            np.all((mask[:, :] == [192, 0,  128]), axis=2) # road
        temp_label[:, :, 0] += 4 * \
            np.all((mask[:, :] == [64,  0, 192]), axis=2) # road
        temp_label[:, :, 0] += 4 * \
            np.all((mask[:, :] == [128, 64, 128]), axis=2) # road
        temp_label[:, :, 0] += 5 * \
            np.all((mask[:, :] == [192,  0, 192]), axis=2) # two wheeler
        temp_label[:, :, 0] += 6 * \
            np.all((mask[:, :] == [192,  0, 0]), axis=2) # sidewalk
        temp_label[:, :, 0] += 7 * \
            np.all((mask[:, :] == [128, 128, 192]), axis=2) # sign
        temp_label[:, :, 0] += 8 * \
            np.all((mask[:, :] == [192, 128, 64]), axis=2) # truck
        temp_label[:, :, 0] += 8 * \
            np.all((mask[:, :] == [192, 128, 192]), axis=2) # truck
        temp_label[:, :, 0] += 9 * \
            np.all((mask[:, :] == [128, 64, 192]), axis=2) # train
        temp_label[:, :, 0] += 10 * \
            np.all((mask[:, :] == [64, 64, 0]), axis=2) # traffic light
        temp_label[:, :, 0] += 11 * \
            np.all((mask[:, :] == [64, 64, 128]), axis=2) # other moving
        temp_label = temp_label.astype(np.uint8)

        cv2.imwrite(os.path.join(FLAGS.dir_out, mask_file), temp_label)

    print("mask to label conversion completed")
    print(f"labels are in : {FLAGS.dir_out}")

def main():
    # dir containing masks
    dir_src = "/home/abhishek/Desktop/datasets/camvid/masks_resized/"

    # dir to save labels
    dir_out = "/home/abhishek/Desktop/datasets/camvid/labels_resized/"

    parser = argparse.ArgumentParser(
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument("--dir_src", default=dir_src,
        type=str, help="path to load masks")
    parser.add_argument("--dir_out", default=dir_out,
        type=str, help="path to save labels")

    FLAGS, unparsed = parser.parse_known_args()
    mask_to_label(FLAGS)

if __name__ == "__main__":
    main()
