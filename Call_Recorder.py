import glob, os, shutil, fnmatch

list_of_files = glob.glob('/home/clayton/Downloads/*.zip')
latest_file = max(list_of_files, key=os.path.getctime)
print(latest_file)

#This is the Directory that the files will be saved to
run_in = '/home/clayton/Documents/Call_Recording/Run'

shutil.unpack_archive(latest_file, '/home/clayton/Documents/Call_Recording/Run')

number_of_missed_calls = len(fnmatch.filter(os.listdir('/home/clayton/Documents/Call_Recording/Run/Takeout/Voice/Calls/'), '*Missed*.html'))
number_of_placed_calls = len(fnmatch.filter(os.listdir('/home/clayton/Documents/Call_Recording/Run/Takeout/Voice/Calls/'), '*Placed*.html'))
number_of_texts = len(fnmatch.filter(os.listdir('/home/clayton/Documents/Call_Recording/Run/Takeout/Voice/Calls/'), '*Text*.html'))

message_placed_calls = ('Total Number of Placed Calls is: ' + str(number_of_placed_calls))
message_missed_calls =('Total Number of Missed Calls is: ' + str(number_of_missed_calls))
message_text = ('Total Number of Texts is: ' + str(number_of_texts))

#print(message_placed_calls + ' ')
#print(message_missed_calls + ' ')
#print(message_text)

with open('/home/clayton/Documents/Call_Recording/log.txt', 'a') as f:
    f.write(message_placed_calls + message_missed_calls + message_text)

shutil.rmtree(run_in)

print('Log Recorded, Files Cleaned Up!')