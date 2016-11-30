import pyccda,xmltodict,json

#ccda = pyccda.CcdaDocument('<?xml version="1.0" encoding="UTF-8"?><note><to>Tove</to><from>Jani</from><heading>Reminder</heading><body>Dont forget me this weekend!</body></note>')
#ccda = pyccda.CcdaDocument(open('testdata/CCDA_CCD_b1_Ambulatory_v2.xml') )    #CCDA_CCD_b1_Ambulatory_v2.xml'))
ccda = pyccda.CcdaDocument(open('testdata/example2.xml') )
#ccda = pyccda.CcdaDocument(open('testdata/Vitera_CCDA_SMART_Sample.xml') )
    # Returns CCDA represented as a simple CSV, which can be
    # useful to load data into an external data analysis tool.
#print ccda.to_csv()

    # Returns CCDA represented as a protocol buffer message, for easy
    # data access and transfer between systems.
ccda_message = ccda.to_message()

# Easily access health information using the protocol buffer message.
#print json.dumps(ccda_message.allergies) #xmltodict.parse(ccda_message.allergies)
#print json.dumps(ccda_message.demographics)
#print ccda_message.immunizations
#print ccda_message.labs
#print ccda_message.medications
#print ccda_message.problems
#print ccda_message.procedures
#print MessageJSONEncoder(ccda_message.vitals)
print ccda.to_json()
