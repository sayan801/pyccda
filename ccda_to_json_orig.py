import pyccda,xmltodict,json

import sys, string, os

length = len(sys.argv)

print "Parameters: %s"%length

if length != 2 :
    raise Exception("Usage: Python Filename XmlFileName")

XmlFileName = sys.argv[1]

print "XmlFileName: %s"%XmlFileName

#section = sys.argv[2]

ccda = pyccda.CcdaDocument(open(XmlFileName) )    #CCDA_CCD_b1_Ambulatory_v2.xml'))

ccda_message = ccda.to_message()

print ccda.to_json()
