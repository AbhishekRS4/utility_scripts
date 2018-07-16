# @author : Abhishek R S
# script to convert camvid mask to label only for road class

import os
import numpy as np
import cv2

# dir containing masks
src_dir = '/home/abhishek/Desktop/datasets/camvid/masks_resized/'

# dir to save labels
target_dir = '/home/abhishek/Desktop/datasets/camvid/labels_resized/'

# list of all masks
src_mask_files = os.listdir(src_dir)

print('number of masks to convert to labels : ' + str(len(src_mask_files)))
print('mask to label conversion started')
print('')

for mask_file in src_mask_files:
    mask = cv2.imread(os.path.join(src_dir, mask_file))
    temp_label = np.zeros((mask.shape[0], mask.shape[1], 1), dtype = np.uint8)
    temp_label[:, :, 0] = 1 * np.all((mask[:, :] == [128, 64, 128]), axis = 2)
    cv2.imwrite(os.path.join(target_dir, mask_file), temp_label)

print('mask to label conversion completed')
