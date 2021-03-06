#pyccda

A Python library for CCDA XML files. Part of the BlueButton+ health data liberation initiative

##Development notice

This project is *under development* and is not fully-featured yet. However, pyccda is capable of
parsing CCDA XML files and converting them to structured ProtoRPC messages or simplified CSV
documents, which can be used to pipeline the data into data analysis tools.

##Usage

Before using, run `pip install -r requirements.txt` to install dependencies.

    import pyccda
    ccda = pyccda.CcdaDocument(open('ccda_file.xml'))

    # Returns CCDA represented as a simple CSV, which can be
    # useful to load data into an external data analysis tool.
    ccda.to_csv()

    # Returns CCDA represented as a protocol buffer message, for easy
    # data access and transfer between systems.
    ccda_message = ccda_doc.to_message()

    # Easily access health information using the protocol buffer message.
    ccda_message.allergies
    ccda_message.demographics
    ccda_message.immunizations
    ccda_message.labs
    ccda_message.medications
    ccda_message.problems
    ccda_message.procedures
    ccda_message.vitals

##Running tests

    # Verifies basic functionality against test data.
    python ccda_test.py
    
## Checking vitals details (unit and exsiatance of value) and logged information in a log file
# to run the code use following command.
python vitals_ccda_test.py
# to see .log file use following commands..
cd pyccda
gedit Vitals_test.log

## To see text files for all vital section from a set of XML files, follow the following commands
cd pyccda
python vitals_ccda_test_text_file.py
-- see the .txt files for vital section in /pyccda

