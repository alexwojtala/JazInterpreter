from analyzer import CallAnalyzer
import sys

if sys.version_info >= (3, 0):
    filename = input('Enter your jaz file: ')
elif sys.version_info >= (2, 0):
    filename = raw_input('Enter your jaz file: ')
else:
    print("Please update python to version 2.0 or newer")
    quit()

CallAnalyzer(filename)
