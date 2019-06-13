import json
import csv 
import argparse

parser = argparse.ArgumentParser()

parser.add_argument('--infile',default=None, type=str, help='JSON file to be processed')

arguments = parser.parse_args()

s = arguments.infile[0:len(arguments.infile)-1].split('.')
data = json.load(open(arguments.infile))

# open a file for writing
#employ_data = open(s[0]+'.'+s[1]+'.'+s[2]+'.csv', 'w') #For MayFair depositions

employ_data = open(s[0]+'.'+s[1]+'.csv', 'w') #For Tobacco depositions

# create the csv writer object
csvwriter = csv.writer(employ_data)

count = 0

for emp in data['oral_deposition']['parsed_examinations']:
    for event in emp['examination']:
        if count==0:
            header = event.keys()  
            print(event.keys())      
            csvwriter.writerow(list(header)+['Declarative_Text'])
            count += 1

        if 'question' in event.keys() and 'answer' in event.keys():
            csvwriter.writerow(event.values())
employ_data.close()
