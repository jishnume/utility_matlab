import os
import numpy as np
import matplotlib.pyplot as plt


# Full path of the folder that contains the images to be read
folder_path='C://Users//e59832jg//PhD//Utility-functions//test_images_new'

# printing out all the entities inside a directory
all_filenames=os.listdir(folder_path)

# converting the list output of os.listdir() function into a numpy array
all_filenames=np.array(all_filenames)

# Learning a separate way of writing the for loop
desired_extension='.png'

correct_files_counter=0;

# Checking for consistency of the file types
for f in all_filenames:
    if f.endswith(desired_extension):
        correct_files_counter=correct_files_counter+1
    
if correct_files_counter==len(all_filenames):
    print('\nThe directory contains files with a single extension '+ desired_extension + ' !!')
elif correct_files_counter==0:
    print('\nNo files with the extension '+desired_extension+' !! Check again !!')
else:
    print('\nThe folder contains multiple types of files !!\n')



# a null array to store all the name of the files without the extension
filename_array=np.array([])

for single_file in all_filenames:
    name_wo_extension,_=os.path.splitext(single_file)
    filename_array=np.concatenate((filename_array,np.array([name_wo_extension])))


# temporary variable to store the seconds
t_vec=np.array([]);

for i in range(len(filename_array)):
    hex_name=filename_array[i]

    # Spiltting the filename
    left_part,right_part=hex_name.split("_")
    # print('\nThe left part is (hex format) = ',left_part)
    # print('The right part is (hex format) = ',right_part)

    # # converting both the parts to human readable form
    left_part_in_deci=int(left_part,16)
    right_part_in_deci=int(right_part,16)
    t_vec=np.concatenate((t_vec,np.array([right_part_in_deci])))

    # print('The left part is (decimal format) = ',left_part_in_deci)
    # print('The right part is (decimal format) = ',right_part_in_deci)

# A vector to say the image number 1,2,3, etc.
file_vec=np.arange(1,correct_files_counter+1,1)

# fitting a straight line to get the framerate
image_number_vec=file_vec    # number of images 
time_vec=(t_vec-t_vec[0])*1e-3    # time stamps of the images in seconds

m,c=np.polyfit(image_number_vec,time_vec,1)
frame_rate_val=round(m,2)

print('Frame Rate = '+str(frame_rate_val)+' frames/sec')

fig,ax=plt.subplots(1,1,figsize=(8,6))
plt.subplots_adjust()

ax.scatter(image_number_vec,time_vec,color='black')
ax.set_xlabel('Image Number',fontsize=18)
ax.set_ylabel('time instant (s)',fontsize=18)
ax.tick_params('both',labelsize=18,direction='in')

plt.show()

