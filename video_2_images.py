'''
@author : Abhishek R S
'''

import os
import sys
import argparse
import numpy as np
import cv2

def video_to_images(vid_name, out_dir, img_prefix, img_format):
    # create the output directory if not present
    if not os.path.exists(out_dir):
        os.makedirs(out_dir)

    # create video capture object
    video_capture = cv2.VideoCapture(vid_name)
    success = True

    frame_count = 0

    print('Extracting images started')
    while success:
        # try to extract a frame
        success, image_frame = video_capture.read()

        # if not successful then break
        if not success:
            break

        # save the successfully extracted frame
        cv2.imwrite(os.path.join(out_dir, img_prefix + str(frame_count) + img_format), image_frame)
        frame_count += 1

    print('Extracting images completed')
    print('Extracted images are in : ' + out_dir)
    print('')

def main():  
    # video file path whose frames have to be saved
    # destination directory where the frames have to be saved
    # file name with which the frames should be saved
    # image format which should be used to save the frame
    vid_name = 'output.avi'
    out_dir = '.'
    img_prefix = 'image_'
    img_format = '.png'

    parser = argparse.ArgumentParser()
    parser.add_argument('-vid_name', default=vid_name,
                        type=str, help='name for input video file')
    parser.add_argument('-out_dir', default=out_dir,
                        type=str, help='path to save output images')
    parser.add_argument('-img_prefix', default=img_prefix,
                        type=str, help='prefix for image names')
    parser.add_argument('-img_format', default=img_format,
                        type=str, help='image saving format') 

    input_args = vars(parser.parse_args(sys.argv[1:]))
    for k in input_args.keys():
        print(k + ': ' + str(input_args[k]))
    print('')

    video_to_images(input_args['vid_name'], input_args['out_dir'], input_args['img_prefix'], input_args['img_format'])

if __name__ == '__main__':
    main()
