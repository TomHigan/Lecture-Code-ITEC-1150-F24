from urllib import request  #allows python to make web requests. i.e. ping google.com
from time import sleep  #import the sleep function which pauses a program for a specified time
import winsound #imports windows sounds

url = 'https://www.google.com'
seconds_between_checks = 3

while True:
    print('checking if online....')
    try:
        #attempts ping the url in the url variable
        request.urlopen(url).read()
        print('You are online!')
        winsound.MessageBeep()
    except:
        #if url is failed to be connected to it runs this print function
        print('You are not online.')
    #sleep function is ran at the end of the while loop
    sleep(seconds_between_checks)