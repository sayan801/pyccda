import pyccda,xmltodict,json

#ccda = pyccda.CcdaDocument('<?xml version="1.0" encoding="UTF-8"?><note><to>Tove</to><from>Jani</from><heading>Reminder</heading><body>Dont forget me this weekend!</body></note>')
#ccda = pyccda.CcdaDocument(open('testdata/CCDA_CCD_b1_Ambulatory_v2.xml') )    #CCDA_CCD_b1_Ambulatory_v2.xml'))
#ccda = pyccda.CcdaDocument(open('testdata/example.xml') )
#ccda = pyccda.CcdaDocument(open('testdata/ca62bccf-2038-4b11-ab7a-9f6d6902397b.xml') )
#ccda = pyccda.CcdaDocument(open('testdata/Vitera_CCDA_SMART_Sample.xml') )
#ccda = pyccda.CcdaDocument(open('testdata/Patient-140.xml') )
#ccda = pyccda.CcdaDocument(open('testdata/InPt_Discharge_Summary_CED_Type.xml') )
#ccda = pyccda.CcdaDocument(open('testdata/AdamEveryman-ReferralSummary.xml') ) 
#ccda = pyccda.CcdaDocument(open('testdata/DOC0002.XML') )  
ccda = pyccda.CcdaDocument(open('testdata/C-CDA_R2_CCD_2.xml') ) 
#ccda = pyccda.CcdaDocument(open('testdata/2-problems.xml') ) 
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
