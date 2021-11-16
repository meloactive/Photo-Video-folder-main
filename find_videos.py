from collections import OrderedDict
import os
import win32api

# global list for pictures & videos
pic_list = []
pic_direc_names = []
vid_direc_names = []
vid_list = []
# global tests
# tests = []
files = []

drives = win32api.GetLogicalDriveStrings()
drives = drives.split('\000')[:-1]
for drive in drives:
    print(drive)

# function to find photos/videos
# in the desired path.
def check_drive(dir_path):
    tests =[]
    try:
        # lists the files in the directory
        files_in_list = os.listdir(dir_path)
        for file_ in files_in_list:
            # storing the name of the file
            search_file = file_
            # checks file or directory
            dir_if = os.path.join(dir_path, search_file)
            # file extension
            name, ext = os.path.splitext(file_)            
            # checks if the file is a image
            # if ext[1:] in ('jpg', 'png', 'jpeg', 'gif', 'webp', 'tiff', 'tif', 'bmp', 'dib', 'raw', 'arw', 'svg', 'svgz', 'psd', 'jpe', 'jif', 'jfif', 'jfi'):
            #     # if the file is image then
            #     # the file's folder name is added to a list
            #     pic_direc_names.append(os.path.basename(dir_path))
            # checks if the file is video
            if ext[1:] in ('mp4', 'mov', 'flv', 'wmv', 'avi', 'avchd', 'mpeg-2'):
                # if the file is video then
                # the file's folder name is added to a list
                vid_direc_names.append(dir_path)
                # print(list(set(vid_direc_names)))
                # tests = list(set(vid_direc_names))
                # print(tests)
            # checks if the file is a directory 
            if os.path.isdir(dir_if):
                # if the file is a directory
                # then the function is called 
                # to check for image/video in the directory.
                check_drive(dir_if)
    # excepts if the file is 
    # protected.
    except PermissionError:
        pass
    # print(tests)
    for test in list(set(vid_direc_names)):
        # print(test)
        files_in_list = os.listdir(test)
        for files2 in files_in_list:
            # print(test + "\\" + files2)
            files.append(test + "\\" + files2)
    return files

t1 = check_drive("E:\\")
print(len(list(set(t1))))
# for test in list(set(vid_direc_names)):
#     print(test)
#     files_in_list = os.listdir(test)
#     for files in files_in_list:
#         print(test + "\\" + files)