import glob
import os
import shutil

src_folder = r"/home/clayton/Downloads/Google_Voice/Takeout/Voice/Calls/"
dst_folder = r"/home/clayton/Documents/Google_Voice/Takeout/Voice/Calls/Missed/"

# Search files with .txt extension in source directory
pattern = "*Missed*"
files = glob.glob(src_folder + pattern)

# move the files with txt extension
for file in files:
    # extract file name form file path
    file_name = os.path.basename(file)
    shutil.move(file, dst_folder + file_name)
    print('Moved:', file)