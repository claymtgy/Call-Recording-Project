import fnmatch

#DEBUGGING (Delete Later)
#print(len(fnmatch.filter(os.listdir('/home/clayton/Downloads/Google_Voice/Takeout/Voice/Calls/'), '*Missed*.html')))
#print(len(fnmatch.filter(os.listdir('/home/clayton/Downloads/Google_Voice/Takeout/Voice/Calls/'), '*Placed*.html')))

number_of_missed_calls = len(fnmatch.filter(os.listdir('/home/clayton/Downloads/Google_Voice/Takeout/Voice/Calls/'), '*Missed*.html'))
number_of_placed_calls = len(fnmatch.filter(os.listdir('/home/clayton/Downloads/Google_Voice/Takeout/Voice/Calls/'), '*Placed*.html'))
number_of_texts = len(fnmatch.filter(os.listdir('/home/clayton/Downloads/Google_Voice/Takeout/Voice/Calls/'), '*Text*.html'))

print('Total Number of Placed Calls is: ' + str(number_of_placed_calls))
print('Total Number of Missed Calls is: ' + str(number_of_missed_calls))
print('Total Number of Texts is: ' + str(number_of_texts))