import os, glob, shutil, fnmatch
from asyncore import file_dispatcher
from tkinter import *
from tkinter import filedialog

from soupsieve import select
from yaml import DocumentStartEvent

Documents = '/home/clayton/Documents/'
Logan = '/home/clayton/Documents/Sprinkler_Master/Logan/'
Ogden = '/home/clayton/Documents/Sprinkler_Master/Logan'

OPTIONS = [
"Logan",
"Ogden",
"SLC",
"West Jordan",
"Davis County",
"Provo",
"St. George",
"Reno",
"Carson City",
"Boise",
"Fresno",
"Temecula",
"Colorado Springs",
"Jefferson County",
"Douglas County"
] #etc

master = Tk()
master.geometry('300x150')

variable = StringVar(master)
variable.set(OPTIONS[0]) # default value

w = OptionMenu(master, variable, *OPTIONS)
w.pack()

#def ok():
#    print ("value is:" + variable.get())

def get_file_path():
    global file_path
    # Open and return file path
    file_path = filedialog.askopenfilename(title = 'Select a File', initialdir='/home/clayton/Downloads/', filetypes=[
        ('.zip files', '*.zip'),
        ('all files', '*.*')
    ])

def close():
    master.destroy()

button = Button(master, text="Select", command=get_file_path)
Button2 = Button(master, text='OK', command=close)
button.pack()
Button2.pack()
mainloop()
print(variable.get())
print(file_path)

#This is the Directory that the files will be saved to
selected_area = variable.get()

area_dir = Documents + str(selected_area) + '/'

area_dir_run = area_dir + 'run/Takeout/Voice/Calls/'

shutil.unpack_archive(file_path, (area_dir + 'run'))

number_of_missed_calls = len(fnmatch.filter(os.listdir(area_dir_run), '*Missed*.html'))
number_of_placed_calls = len(fnmatch.filter(os.listdir(area_dir_run), '*Placed*.html'))
number_of_texts = len(fnmatch.filter(os.listdir(area_dir_run), '*Text*.html'))

message_placed_calls = ('Total Number of Placed Calls is: ' + str(number_of_placed_calls))
message_missed_calls =('Total Number of Missed Calls is: ' + str(number_of_missed_calls))
message_text = ('Total Number of Texts is: ' + str(number_of_texts))

with open(area_dir + 'log.txt', 'a') as f:
    f.write(message_placed_calls + message_missed_calls + message_text)

shutil.rmtree(area_dir + 'run/')

print('Log Recorded, Files Cleaned Up!')