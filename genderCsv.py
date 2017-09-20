#!/usr/bin/env python

__author__ = "Ivano Malavolta"
__organization__ = "Vrije Universiteit Amsterdam"
__copyright__ = "Copyright 2017"
__license__ = "MIT"
__version__ = "0.0.1"
__maintainer__ = "Ivano Malavolta"
__email__ = "i.malavolta@vu.nl"
__status__ = "Prototype"

import sys
import time
import csv
from gender import getGenders

def printUsageAndExit():
	print("Usage: python gender.py input_csv_file output_csv_file")
	print("where:")
	print("- input_csv_file: path in the file system where a CSV file exists with a column named either as 'name' or 'first name' (any combination of lower/upper case")
	print("- output_csv_file: path in the file system where the output CSV file will be produced")
	exit()

## Here we manage the argument passed via the command line
if(len(sys.argv) != 3):
	printUsageAndExit()

try:
	f = open(sys.argv[1], 'rt')
	reader = csv.DictReader(f, delimiter=',')
except:
	print("ERROR. The " + sys.argv[1] + " file does not exist. Exiting.")
	exit()

columnName = ""
genderColumnFound = False
confidenceColumnFound = False
documentsColumnFound = False

# Let's check which column we should consider
for header in reader.fieldnames:
	if((header.lower() == "name") | (header.lower() == "first name")):
		columnName = header
	if(header == "gender"):
		genderColumnFound = True
	if(header == "confidence"):
		confidenceColumnFound = True
	if(header == "documents"):
		documentsColumnFound = True
if(columnName == ""):
	print("ERROR. No 'name' or 'first name' identified in " + sys.argv[1])
	exit()

# Let's open a file to write
if(sys.argv[2]):
	fileName = sys.argv[2]
else:
	# invent a name so that we do not block the execution
	fileName = './temp_' + str(time.time()) + ".csv"

try:
	resultFile = open(fileName, 'wb')
except:
	print("ERROR in creating the output file (local folder)")

fieldnames = reader.fieldnames
if(not (genderColumnFound & confidenceColumnFound & documentsColumnFound)):
	fieldnames = reader.fieldnames + ['gender', 'confidence', 'documents']

writer = csv.DictWriter(resultFile, fieldnames=fieldnames)
writer.writeheader()

for index, row in enumerate(reader):
	name = row[columnName]
	if((not('gender' in row.keys())) or (row['gender'] is None) or (row['gender'] == "")):
		try:
			time.sleep(0.1)
			gendersInfo = getGenders([name])
			row['gender'] = gendersInfo[0][0]
			row['confidence'] = gendersInfo[0][1]
			row['documents'] = gendersInfo[0][2]
		except Exception as e:
			print("ERROR making the request at index " + str(index))
	writer.writerow(row)
	print(str(index) + ' --- ' + str(row))

print('Result in ' + fileName)
