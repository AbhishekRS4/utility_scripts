'''
@author : Abhishek R S
'''

import os
import sys
import argparse
import numpy as np
import cv2


def create_video(src_dir, out_dir, vid_name, vid_encoder, img_pattern, height, width, fps):
    # video_writer is a Video Writer object
    video_writer = cv2.VideoWriter(os.path.join(
        out_dir, vid_name), cv2.VideoWriter_fourcc(*vid_encoder), fps, (width, height))

    # list all the required frames for the video
    list_images = [x for x in os.listdir(src_dir) if x.endswith(img_pattern)]
    list_images.sort()

    print('Number of files to be converted into a video : ' + str(len(list_images)))

    # convert the frames to video
    for img_name in list_images:
        try:
            video_writer.write(cv2.imread(os.path.join(src_dir, img_name)))
        except IOError:
            print('File not an image or corrupted')

    # release the Video Writer object
    video_writer.release()

    print('Video has been successfully created in : ' + out_dir)


def main():
    # source directory which contains all the images which need to be converted to a video
    # output directory where the video has to be saved
    # vid_name with which the video has to be saved
    # img_pattern looks for .jpg, .png etc.
    '''
    XVID - preferred
    X264
    DIVX
    MJPG are other video encoders
    '''

    src_dir = '.'
    out_dir = '.'
    vid_name = 'output.avi'
    vid_encoder = 'XVID'
    img_pattern = '.png'
    height = 480
    width = 640
    fps = 10

    parser = argparse.ArgumentParser()
    parser.add_argument('-src_dir', default=src_dir,
                        type=str, help='path to load images')
    parser.add_argument('-out_dir', default=out_dir,
                        type=str, help='path to save video')
    parser.add_argument('-vid_name', default=vid_name,
                        type=str, help='name for output video')
    parser.add_argument('-vid_encoder', default=vid_encoder,
                        type=str, help='encoder for creation of output video')
    parser.add_argument('-img_pattern', default=img_pattern,
                        type=str, help='image pattern .png or .jpg etc.')
    parser.add_argument('-height', default=height,
                        type=int, help='height of the image')
    parser.add_argument('-width', default=width, type=int,
                        help='width of the image')
    parser.add_argument('-fps', default=fps, type=int,
                        help='fps of output video')

    input_args = vars(parser.parse_args(sys.argv[1:]))
    for k in input_args.keys():
        print(k + ': ' + str(input_args[k]))
    print('')

    print('Video generation started')
    create_video(input_args['src_dir'], input_args['out_dir'], input_args['vid_name'], input_args['vid_encoder'],
                 input_args['img_pattern'], input_args['height'], input_args['width'], input_args['fps'])
    print('Video generation completed')


if __name__ == '__main__':
    main()
