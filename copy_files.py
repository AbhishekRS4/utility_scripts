'''
@author : Abhishek R S
'''

import os
import sys
import argparse
import shutil


def copy_files(src_dir, out_dir):
    # list all files in src directory
    src_files = os.listdir(src_dir)

    # create the output directory if not present
    if not os.path.exists(out_dir):
        os.makedirs(out_dir)

    print('Total Files in src directory : ' + str(len(src_files)))
    print('Copying files started')

    # copy all files in src directory to destination directory with the same names
    for i in range(len(src_files)):
        shutil.copy2(os.path.join(src_dir, src_files[i]), out_dir)

    print('Copying files finished')


def main():
    # path for source and destination directories
    src_dir = '/home/user/source/'
    out_dir = '/home/user/destination/'

    parser = argparse.ArgumentParser()
    parser.add_argument('-src_dir', default=src_dir,
                        type=str, help='path to source directory')
    parser.add_argument('-out_dir', default=out_dir,
                        type=str, help='path to output directory')

    input_args = vars(parser.parse_args(sys.argv[1:]))
    for k in input_args.keys():
        print(k + ': ' + str(input_args[k]))
    print('')

    copy_files(input_args['src_dir'], input_args['out_dir'])


if __name__ == '__main__':
    main()
