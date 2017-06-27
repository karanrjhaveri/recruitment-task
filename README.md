# Recruitment task :: Documentation
- Karan Jhaveri

This project was done twice using 2 different programming languages: 
- Python 
- PHP

This application examines data stored in xml, yml or csv format files to produce a sum of the 'value' attribute.

Example Parameters for Script:  
(Python)  
- python script.py --input data/file.yml  
- python script.py --input data/file.xml --output results/results.txt  
(PHP)  
- php script.py --input data/file.csv  
- php script.py --input data/file.yml --output results/results.txt  

2 inputs are taken:  
--input is Mandatory and --output is Optional  

If no output argument supplied, the output prints to stdout .  

Functional Test:  
(Python)  
- python test.py
(PHP)  
- php test.php

Steps Performed (Log):-  

(Python)  
1. Install Python v.3
2. Open Command-line
3. Run Commands:
a. Navigate to the script's directory: 'cd /d D:\..\Github\recruitment-task\Python'  
b. Install the necessary packages for this project using pip  
- csv
- xmltodict
- argparse
- yaml
4. Completed script.py
5. Functional tests conducted using test.py
(PHP)  
1. Install Xampp
2. Add PHP binary to Path (https://www.youtube.com/watch?v=neBVQBL_2P0)
3. Installed Composer: https://getcomposer.org/download/
3. Install Symfony:
a. Navigate to script's directory via Command-line  
b. 'composer require symfony/symfony' (or alternatively 'compser require symfony/yaml')  
4. Completed script.php
5. Functional tests conducted using test.php

Development Strategy:  
- Create code stub and roughly flesh out the idea
- Break each functionality of the application into smaller modules.
- Test each module independently and after including in the script
- Once script was complete, made a test script that validates the output of the main script