# @author : Abhishek R S
# script to convert camvid mask to label only for road class

import os
import sys
import argparse
import numpy as np
import cv2
from scipy.misc import imsave

def mask_to_label(FLAGS):
    src_dir = FLAGS.src_dir
    out_dir = FLAGS.out_dir

    # create the output directory if not present
    if not os.path.exists(out_dir):
        os.makedirs(out_dir)

    # list of all masks
    src_mask_files = os.listdir(src_dir)

    print('number of images to be processed : ' + str(len(src_mask_files)))
    print('mask to label conversion started')
    print('')

    for mask_file in src_mask_files:
        mask = cv2.imread(os.path.join(src_dir, mask_file))
        temp_label = np.zeros(
            (mask.shape[0], mask.shape[1], 1), dtype = np.uint8)
        temp_label[:, :, 0] = 1 * \
            np.all((mask[:, :] == [0, 0, 6]), axis=2)  # road lane line
        temp_label = temp_label[:, :, 0].astype(np.uint8)

        cv2.imwrite(os.path.join(out_dir, mask_file), temp_label)
        #imsave(os.path.join(out_dir, mask_file), temp_label)

    print('mask to label conversion completed')
    print('labels are in : ' + str(out_dir))


def main():
    # dir containing original carla format segmentation masks
    src_dir = '/home/abhishek/Desktop/datasets/carla/CameraRGB/'

    # dir to save lane segmentation labels
    out_dir = '/home/abhishek/Desktop/datasets/carla/CameraSeg/'

    parser = argparse.ArgumentParser()
    parser.add_argument('-src_dir', default=src_dir,
                        type=str, help='path to load original carla segmentation labels')
    parser.add_argument('-out_dir', default=out_dir,
                        type=str, help='path to save lane segmentation labels')

    FLAGS, unparsed = parser.parse_known_args()

    mask_to_label(FLAGS)


if __name__ == '__main__':
    main()
