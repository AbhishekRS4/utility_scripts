'''
@author : Abhishek R S
'''

import os
import sys
import argparse
import cv2


def resize_images(src_dir, out_dir, height, width, img_pattern):
    # create the output directory if not present
    if not os.path.exists(out_dir):
        os.makedirs(out_dir)

    # list all the image files in the source directory
    src_images_list = [x for x in os.listdir(
        src_dir) if x.endswith(img_pattern)]

    # set target image size and interpolation to use for resize
    target_image_size = (width, height)
    interpolation = cv2.INTER_LINEAR

    print('number of images to process : ' + str(len(src_images_list)))
    print('resizing images started')

    # resize the images and save in the destination directory
    for img_file in src_images_list:
        img = cv2.imread(os.path.join(src_dir, img_file))
        img = cv2.resize(img, target_image_size, interpolation=interpolation)
        cv2.imwrite(os.path.join(out_dir, img_file), img)

    print('resizing images completed')
    print('resized images are in : ' + str(out_dir))


def main():
    # source and destination directories for images that have to be resized and saved
    src_dir = '/home/user/src_dir/'
    out_dir = '/home/user/out_dir/'
    height = 480
    width = 640
    img_pattern = '.png'

    parser = argparse.ArgumentParser()
    parser.add_argument('-src_dir', default=src_dir,
                        type=str, help='path to load original images')
    parser.add_argument('-out_dir', default=out_dir,
                        type=str, help='path to save resized images')
    parser.add_argument('-height', default=height,
                        type=int, help='height of the image')
    parser.add_argument('-width', default=width, type=int,
                        help='width of the image')
    parser.add_argument('-img_pattern', default=img_pattern,
                        type=str, help='image pattern .png or .jpg etc.')

    input_args = vars(parser.parse_args(sys.argv[1:]))
    for k in input_args.keys():
        print(k + ': ' + str(input_args[k]))
    print('')

    resize_images(input_args['src_dir'], input_args['out_dir'],
                  input_args['height'], input_args['width'], input_args['img_pattern'])


if __name__ == '__main__':
    main()
