import sys, string, os

length = len(sys.argv)

print "Parameters: %s"%length

if length != 2 :
    raise Exception("Usage: Python Digit")

digit = sys.argv[1]

print "Given string %s " % digit

trueFalse = digit.isdigit()

print "Is it digit? :  %s " % trueFalse

trueFalse = digit.isalnum()

print "Is it Alpha Numeric? :  %s " % trueFalse

try:
    trueFalse = long(float(digit))
except ValueError:
    trueFalse = None

print "Is it float? :  %s " % trueFalse