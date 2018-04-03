'''
@author : Abhishek R S
'''

import os
import shutil

# path for source and destination directories
src_directory = "/home/user/source/"
dst_directory = "/home/user/destination/"

# list all files in src directory
src_file_names = os.listdir(src_directory)

print("Total Files in src directory : " + str(len(src_file_names)))

# copy all files in src directory to destination directory with the same names
for i in range(len(src_file_names)):
    shutil.copy2(os.path.join(src_directory, src_file_names[i]), dst_directory)
