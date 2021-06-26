"""
@author : Abhishek R S
"""

import os
import sys
import shutil
import argparse

def copy_files(FLAGS):
    # list all files in src directory
    src_files = os.listdir(FLAGS.dir_src)

    # create the output directory if not present
    if not os.path.isdir(FLAGS.dir_out):
        os.makedirs(FLAGS.dir_out)

    print(f"Total Files in src directory : {len(src_files)}")
    print("Copying files started")

    # copy all files in src directory to destination directory with the same names
    for i in range(len(src_files)):
        shutil.copy2(os.path.join(FLAGS.dir_src, src_files[i]), FLAGS.dir_out)

    print("Copying files finished")

def main():
    # path for source and destination directories
    dir_src = "/home/user/source/"
    dir_out = "/home/user/destination/"

    parser = argparse.ArgumentParser(
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument("--dir_src", default=dir_src,
        type=str, help="path to source directory")
    parser.add_argument("--dir_out", default=dir_out,
        type=str, help="path to output directory")

    FLAGS, unparsed = parser.parse_known_args()
    copy_files(FLAGS)

if __name__ == "__main__":
    main()
