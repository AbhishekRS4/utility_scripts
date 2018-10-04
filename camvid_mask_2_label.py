# @author : Abhishek R S
# script to convert camvid mask to label only for road class

import os
import sys
import argparse
import numpy as np
import cv2


def mask_to_label(src_dir, out_dir):
    # create the output directory if not present
    if not os.path.exists(out_dir):
        os.makedirs(out_dir)

    # list of all masks
    src_mask_files = os.listdir(src_dir)

    print('number of masks to convert to labels : ' + str(len(src_mask_files)))
    print('mask to label conversion started')
    print('')

    for mask_file in src_mask_files:
        mask = cv2.imread(os.path.join(src_dir, mask_file))
        temp_label = np.zeros(
            (mask.shape[0], mask.shape[1], 1), dtype=np.uint8)
        temp_label[:, :, 0] = 1 * \
            np.all((mask[:, :] == [128, 64, 128]), axis=2)
        cv2.imwrite(os.path.join(out_dir, mask_file), temp_label)

    print('mask to label conversion completed')
    print('labels are in : ' + str(out_dir))


def main():
    # dir containing masks
    src_dir = '/home/abhishek/Desktop/datasets/camvid/masks_resized/'

    # dir to save labels
    out_dir = '/home/abhishek/Desktop/datasets/camvid/labels_resized/'

    parser = argparse.ArgumentParser()
    parser.add_argument('-src_dir', default=src_dir,
                        type=str, help='path to load images')
    parser.add_argument('-out_dir', default=out_dir,
                        type=str, help='path to save video')

    input_args = vars(parser.parse_args(sys.argv[1:]))
    for k in input_args.keys():
        print(k + ': ' + str(input_args[k]))
    print('')

    mask_to_label(input_args['src_dir'], input_args['out_dir'])


if __name__ == '__main__':
    main()
