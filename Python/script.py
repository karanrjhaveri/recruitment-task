import os # Path
import argparse # Arguments
import yaml # parse YML files
import xmltodict # parse XML files
import csv # parse CSV files


# Extracts necesary information from a 'directory' string
def fileDirectory(thisFile,projectPath):
	thisFile = thisFile.replace('/', '\\')
	os.chdir(projectPath)
	os.chdir('..')
	path = (os.path.abspath(os.curdir)+'\\'+thisFile)
	ext = path[-3:]
	delimiter = '\\' # \
	delimiter_pos = path.find(delimiter)+1 # index of character after delimiter
	path_len = len(path)
	fileName = path[delimiter_pos:path_len] # substring that contains the screenshot filename e.g. xyz.csv
	return projectPath,path,ext,fileName
	
# Construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--input", required=True, help="Path to input file")
ap.add_argument("-o", "--output", required=False,help="Path to output file")
args = vars(ap.parse_args())

sum,i=0,0
projectPath=(os.path.abspath(os.curdir))
_,inPath,inExt,inFileName = fileDirectory(args['input'],projectPath)
	
# Make sure file-type is compatible
while not (inExt=='yml' or inExt=='xml' or inExt=='csv'):
	inPath = input('Invalid Entry!\nPlease enter a valid input:')
	
	_,inPath,inExt,inFileName = fileDirectory(inPath,projectPath)
	
if(inExt=="yml"):
	with open(inPath, 'r') as stream:
		try:
			doc = (yaml.load(stream))
			
			while True:
				value = int(doc["users"][i]["value"])
				sum+= value
				i+=1
				
		except yaml.YAMLError as exc:
			print(exc)
		except IndexError as exc:
			pass
elif(inExt=="xml"):
	with open(inPath) as fd:
		doc = xmltodict.parse(fd.read())
	
	try:
		while True:
			value = int(doc['users']['user'][i].get('value'))
			sum += value
			i+=1
	except IndexError as exc:
		pass
elif(inExt=="csv"):
	inputFile = csv.DictReader(open(inPath))

	for row in inputFile:
		value = int(row['value'])
		sum += value

# Handle the output as intended (stdout or file)
if (args["output"]):
	outPath=args["output"]
	_,outPath,_,_=fileDirectory(outPath,projectPath)
	f = open(outPath, 'w')
	f.write(str(sum))
	f.close()
else:
	print(sum)



