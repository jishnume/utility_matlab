import os
import numpy as np
# import matplotlib.pyplot as plt
from datetime import datetime,timezone


# Full path of the folder that contains the images to be read
folder_path='C://Users//e59832jg//PhD//Utility-functions//test_images'

# printing out all the entities inside a directory
all_filenames=os.listdir(folder_path)

# converting the list output of os.listdir() function into a numpy array
all_filenames=np.array(all_filenames)

# print('length of the filename array = '+str(len(all_filenames)))

name1=all_filenames[0]


# # checking for the extensions of the files
# for i in range(len(all_filenames)):
#     name=all_filenames[i]

# Learning a separate way of writing the for loop
desired_extension='.png'

correct_files_counter=0;

# Checking for consistency of the file types
for f in all_filenames:
    if f.endswith(desired_extension):
        correct_files_counter=correct_files_counter+1
    
if correct_files_counter==len(all_filenames):
    print('\nThe directory contains files with a single extension !!')
elif correct_files_counter==0:
    print('\nNo files with the given extension !! Check again !!')
else:
    print('\nThe folder contains multiple types of files !!\n')


'''
Once the previous task is done, now I am trying to create a numpy array
with only the filenames without the extensions
'''

# a null array to store all the name of the files without the extension
filename_array=np.array([])

for single_file in all_filenames:
    name_wo_extension,_=os.path.splitext(single_file)
    filename_array=np.concatenate((filename_array,np.array([name_wo_extension])))


# Testing the conversion of filenames to human readable text names
for i in range(len(filename_array)):
    hex_name=filename_array[i]
    # print('A sample name (in hexadecimal format) = ',hex_name)

    # Spiltting the filename
    left_part,right_part=hex_name.split("_")
    print('\nThe left part is (hex format) = ',left_part)
    print('The right part is (hex format) = ',right_part)

    # converting both the parts to human readable form
    left_part_in_deci=int(left_part,16)
    right_part_in_deci=int(right_part,16)
    # print('The left part is (decimal format) = ',left_part_in_deci)
    # print('The right part is (decimal format) = \n',right_part_in_deci)

    timestamp_dec=right_part_in_deci

    # getting a timestamp
    dt=datetime.fromtimestamp(timestamp_dec)
    print('the first (unknown) part : ',left_part_in_deci)
    print('Readable time : ',dt)

print('\nThe code is successful !!\n')