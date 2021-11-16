from tkinter import *
from tkinter.font import Font
from tkinter import ttk
from tkinter import scrolledtext
from collections import OrderedDict
import win32api, os

# global variables
nDrive = ''
pic_direc_names = []
vid_direc_names = []

class SearchPV:
    def __init__(self, window, drives):
        self.window = window
        self.drives = drives
        window.title("Find Folder (listing folder containing Photo/Video)")
        window.geometry('500x500')        

        self.label1 = Label(window, text = 'Select Preferred Drive:', font = ("Arial", 15))
        self.label1.place(x = 120, y = 20)

        self.cdriveButton = Button(window, text = " C Drive ", width = 20, height = 2, command = self.cButtonFun)
        self.cdriveButton.place(x = 150, y = 70)

        self.ddriveButton = Button(window, text = " D Drive ", width = 20, height = 2, command = self.dButtonFun)
        self.ddriveButton.place(x = 150, y = 120)

        self.edriveButton = Button(window, text = " E Drive ", width = 20, height = 2, command = self.eButtonFun)
        self.edriveButton.place(x = 150, y = 170)

        self.driveLabel = Label(window, text = "If any other drive (other than mentioned above): ", font = ("Arial"))
        self.driveLabel.place(x = 80, y = 240)

        self.otherDrives = ttk.Combobox(window, width = 27)
        drives.insert(0, 'Select')
        self.otherDrives['values'] = drives
        self.otherDrives.place(x = 150, y = 280)
        self.otherDrives.current(0)
        self.otherDrives['state'] = 'readonly'


        self.subButton = Button(window, text = "Submit", width = 20, height = 1, command = self.submit)
        self.subButton.place(x = 150, y = 310)

        self.closeButton = Button(window, text = " Close ", width = 20, height = 1, command = window.destroy)
        self.closeButton.place(x = 150, y = 350)

    # displays photo/video files in new window.
    def driveWindow(self):
        self.drive = Toplevel()
        self.drive.geometry('500x500')

        self.label2 = Label(self.drive, text = 'Folders : ', font = ('Arial', 15))
        self.label2.place(x = 15, y = 20)
        
        self.readText = scrolledtext.ScrolledText(self.drive, width = 38, height = 22)
        global pic_direc_names
        global vid_direc_names
        pic_direc_names = list(OrderedDict.fromkeys(pic_direc_names))
        vid_direc_names = list(OrderedDict.fromkeys(vid_direc_names))
        self.readText.insert(END, 'Folders with Photos: \n')
        for i in pic_direc_names:
            self.readText.insert(END, ' -> ' + i + '\n')
            self.readText.yview(END)
        self.readText.insert(END, '\nFolders with Videos: \n')
        for i in vid_direc_names:
            self.readText.insert(END, ' -> ' + i + '\n')
            self.readText.yview(END)
        self.readText.configure(state = DISABLED)
        self.readText.place(x = 20, y = 80)

        self.exitButton = Button(self.drive, text  = "Exit", width = 15, height = 1, command = self.drive.destroy)
        self.exitButton.place(x = 80, y = 450)
    
    # searches C Drive for photos/videos.
    def cButtonFun(self):        
        self.check_drive('C:\\')
        self.driveWindow()
        global pic_direc_names
        pic_direc_names.clear()
        global vid_direc_names
        vid_direc_names.clear()

    # searches D Drive for photos/videos.
    def dButtonFun(self):        
        self.check_drive('D:\\')
        self.driveWindow()
        global pic_direc_names
        pic_direc_names.clear()
        global vid_direc_names
        vid_direc_names.clear()

    # searches E Drive for photos/videos.
    def eButtonFun(self):        
        self.check_drive('E:\\')
        self.driveWindow()
        global pic_direc_names
        pic_direc_names.clear()
        global vid_direc_names
        vid_direc_names.clear()

    # for searching other drives.
    def submit(self):
        nDrive = self.otherDrives.get()
        if nDrive == 'Select':
            pass
        else:
            self.check_drive(nDrive)
            self.driveWindow()
            global pic_direc_names
            pic_direc_names.clear()
            global vid_direc_names
            vid_direc_names.clear()

    # search function
    def check_drive(self, dir_path):
        try:
            files_in_list = os.listdir(dir_path)
            for file_ in files_in_list:
                search_file = file_
                dir_if = os.path.join(dir_path, search_file)
                name, ext = os.path.splitext(file_)            
                if ext[1:] in ('jpg', 'png', 'jpeg', 'gif', 'webp', 'tiff', 'tif', 'bmp', 'dib', 'raw', 'arw', 'svg', 'svgz', 'psd', 'jpe', 'jif', 'jfif', 'jfi'):
                    pic_direc_names.append(os.path.basename(dir_path))
                if ext[1:] in ('mp4', 'mov', 'flv', 'wmv', 'avi', 'avchd', 'mpeg-2'):
                    vid_direc_names.append(os.path.basename(dir_path))
                if os.path.isdir(dir_if):
                    self.check_drive(dir_if)
        except PermissionError:
            pass

# Main Function.
if __name__ == '__main__':
    drives = win32api.GetLogicalDriveStrings()
    drives = drives.split('\000')[:-1]    
    window = Tk()
    SearchPV(window, drives)
    window.mainloop()
