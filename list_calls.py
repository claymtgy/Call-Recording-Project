import glob, shutil, os

for missed in glob.glob('/home/clayton/Downloads/Google_Voice/Takeout/Voice/Calls/*Missed*'):
    shutil.move(missed, '/home/clayton/Downloads/Google_Voice/Takeout/Voice/Calls/Missed')
for placed in glob.glob('/home/clayton/Downloads/Google_Voice/Takeout/Voice/Calls/*Placed*'):
    shutil.move(placed, '/home/clayton/Downloads/Google_Voice/Takeout/Voice/Calls/Placed')