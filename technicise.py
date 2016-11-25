import pyccda

ccda = pyccda.CcdaDocument(open('testdata/CCDA_CCD_b1_Ambulatory_v2.xml'))

    # Returns CCDA represented as a simple CSV, which can be
    # useful to load data into an external data analysis tool.
print ccda.to_csv()

    # Returns CCDA represented as a protocol buffer message, for easy
    # data access and transfer between systems.
ccda_message = ccda.to_message()

# Easily access health information using the protocol buffer message.
print ccda_message.allergies
print ccda_message.demographics
print ccda_message.immunizations
print ccda_message.labs
print ccda_message.medications
print ccda_message.problems
print ccda_message.procedures
print ccda_message.vitals
