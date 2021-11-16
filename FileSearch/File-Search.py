from collections import OrderedDict
import os
import win32api

# global list for pictures & videos
pic_list = []
pic_direc_names = []
vid_direc_names = []
vid_list = []

# function to find photos/videos
# in the desired path.
def check_drive(dir_path):
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
                vid_direc_names.append(os.path.basename(dir_path))
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


# Main Function
if __name__ == '__main__':
    # lists all the drives
    # in your device
    drives = win32api.GetLogicalDriveStrings()    
    drives = drives.split('\000')[:-1]
    print('\n', drives)
    try:
            # asking user for the drive
            # to be scanned
            # driveToBeScanned = input('-> Select drive to be scanned: ') + ':' 
            # function to check the drive      
            for drive in drives:    
                check_drive(drive)
    except:
            pass
    # -----------------------------------------------------------
    # Alternative : checks the whole system for image/photo
    # checking drives one by one
    # for drivename in drives:
    #     # drive name is passed to path
    #     path = drivename[0:2]        
    #     # function call to get
    #     # images/videos from the 
    #     # current directory in the path
    #     check_drive(path)
    # -----------------------------------------------------------
    # removes any duplicate or multiple identical file
    # pic_list = list(OrderedDict.fromkeys(pic_list))
    vid_list = list(OrderedDict.fromkeys(vid_list))
    # pic_direc_names = list(OrderedDict.fromkeys(pic_direc_names))
    vid_direc_names = list(OrderedDict.fromkeys(vid_direc_names))
    try:
        # file opened in append 
        # mode to add the list of 
        # images/videos
        rec_file = open('Rec.txt', 'a')
        # clearing the file 
        # to remove previous records
        rec_file.seek(0)
        rec_file.truncate()
        # Adding image filenames into file
        # for picname in pic_list:
        #     rec_file.write(picname)
        #     rec_file.write('\n')            
        # rec_file.write('\n------------------------------------------\n\n\n------------------------------------\n')
        # Adding video filenames into file
        for vidname in vid_list:
            rec_file.write(vidname)
            rec_file.write('\n')
        # close file
        rec_file.close()
        # printing success message
        print('[+] Images/Videos present in the device has been appended to a file.\n')
        # print(pic_direc_names)
        print(vid_direc_names)
    except:
        # printing faliure message
        print('[-] Not able to append Images/Videos present in your device.\n')
        pass
