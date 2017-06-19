# Recruitment task :: Documentation
- Karan Jhaveri

This application examines data stored in xml, yml or csv format files to produce a sum of the 'value' attribute.

Example Parameters:
- python script.py --input data/file.yml
- python script.py --input data/file.xml --output results/results.txt

2 inputs are taken:
--input is Mandatory and --output is Optional

If no output argument supplied, the output prints to stdout .

Steps Performed (Log):-

1. Install Python v.3
2. Open Command Line
3. Run Commands:
4. Navigate to the script's directory
cd /d D:\..\Github\recruitment-task\Python
5. Install the necessary packages for this project using pip
- csv
- xmltodict
- argparse
- yaml
6. Completed script.py
7. Functional tests conducted using test.py 

Development Strategy:
- Create code stub and roughly flesh out the idea
- Break each functionality of the application into smaller modules.
- Test each module independently and after including in the script
- Once script was complete, made a test script that validates the output of the main script
