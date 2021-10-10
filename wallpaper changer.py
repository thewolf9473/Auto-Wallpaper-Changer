import os
from os.path import isfile, join
import time
import ctypes
# the path where the images are saved
folderpath = r"C:\Users\Harsh Mishra\Desktop\Wallpaper"
# Making a list of all the images in that particular folder
all_files = [ f for f in os.listdir(folderpath) if isfile(join(folderpath, f))]

def changer():
    for image in all_files:
        ctypes.windll.user32.SystemParametersInfoW(100, 0, folderpath+ "\\" + image, 0)
        # the time after which you want to chnage the wallpaper
        time.sleep(5.5)
    # for changing the wallpaper regularly
    changer()

if __name__=="__main__":
    changer()