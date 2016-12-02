import pyccda,xmltodict,json
import sys, string, os

length = len(sys.argv)
print "Parameters: %s"%length
if length != 2:
    raise Exception("Usage: Python Filename XmlFileName")
XmlFileName = str(sys.argv[1])
print "XmlFileName: %s"%XmlFileName
#section = sys.argv[2]

ccda = pyccda.CcdaDocument(open(XmlFileName))    #CCDA_CCD_b1_Ambulatory_v2.xml')) # Creation of ccda object for C-CDA XML file

# My modification starts here...

#print ccda  # ccda Object will parse entire C-CDA XML file to produce ProtoRPC message or CSV document
ccda_message = ccda.to_message()        # Using ccda object, we create ProtoRPC message for entire C-CDA XML
#print ccda_message
ccda_csv = ccda.to_csv()                # Using ccda object, we create CSV document object
#print ccda_csv

#print ccda_message.medications   # ProtoRPC message for tag 'Medication" in given C-CDA XML file from folder testdata
print "Allergies in ProtoRPC message:"
print ccda_message.allergies     # ProtoRPC message for tag 'Allergy" in given C-CDA XML file from folder testdata

#print "Complete JSON for given C-CDA XML"
complete_JSON = ccda.to_json()   # Apply to_json() from ccda.py to produce string from C-CDA XML
#print complete_JSON
#print type(complete_JSON)


JSON_file = json.loads(complete_JSON)  # Convert complete_JSON from string to JSON file
#print "JSON file:"
#print JSON_file
print "\nJSON file for Allergies:"
print JSON_file["allergies"]   # Entries for allergies from JSON_file

# Mymodification ends here ....
