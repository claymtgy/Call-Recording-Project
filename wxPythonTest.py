import os, shutil, fnmatch, glob
from tkinter import *
from tkinter import filedialog

def get_file_path():
    global file_path
    # Open and return file path
    file_path= filedialog.askopenfilename(title = "Select A File", initialdir="/home/clayton/Downloads/")
    l1 = Label(window, text = "File path: " + file_path).pack()

window = Tk()
# Creating a button to search the file
b1 = Button(window, text = "Open File", command = get_file_path).pack()
window.mainloop()
print(file_path)

#This is the Directory that the files will be saved to
run_in = '/home/clayton/Documents/Call_Recording/Run'

shutil.unpack_archive(file_path, '/home/clayton/Documents/Call_Recording/Run')

number_of_missed_calls = len(fnmatch.filter(os.listdir('/home/clayton/Documents/Call_Recording/Run/Takeout/Voice/Calls/'), '*Missed*.html'))
number_of_placed_calls = len(fnmatch.filter(os.listdir('/home/clayton/Documents/Call_Recording/Run/Takeout/Voice/Calls/'), '*Placed*.html'))
number_of_texts = len(fnmatch.filter(os.listdir('/home/clayton/Documents/Call_Recording/Run/Takeout/Voice/Calls/'), '*Text*.html'))

message_placed_calls = ('Total Number of Placed Calls is: ' + str(number_of_placed_calls))
message_missed_calls =('Total Number of Missed Calls is: ' + str(number_of_missed_calls))
message_text = ('Total Number of Texts is: ' + str(number_of_texts))

with open('/home/clayton/Documents/Call_Recording/log.txt', 'a') as f:
    f.write(message_placed_calls + message_missed_calls + message_text)

shutil.rmtree(run_in)

print('Log Recorded, Files Cleaned Up!')