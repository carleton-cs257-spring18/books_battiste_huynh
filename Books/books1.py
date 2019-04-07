import csv 
import sys
import re

#def findLastName(name):
#    lastName = name.split(' ')[-2]
#    print(lastName)
#    return lastName

def main():
    if (len(sys.argv)) < 3:
        print('Usage: blah blah blah', file=sys.stderr)
    
    
    filename = sys.argv[1]
    action = sys.argv[2]
    if len(sys.argv) > 3:
        direction = sys.argv[3]
    else: 
        direction = "forward"
        
    with open(filename, newline = '') as csvfile:
        reader = csv.reader(csvfile)
        outputList = []
        if action == "books":
            for row in reader:
                book = row[0]
                outputList.append(book)
            if direction == "forward":
                outputList.sort()
            elif direction == "reverse":
                outputList.sort(reverse=True)
            else:
                print("Improperly added direction")
        elif action == "authors":
            for row in reader:
                author = row[2]
                name = author.split('(')[0]
                outputList.append(name)
            if direction == "forward":
                outputList.sort(key = lambda x: x.split(' ')[-2])
            elif direction == "reverse":
                outputList.sort(key = lambda x: x.split(' ')[-2], reverse=True)
        
        for i in range(len(outputList)):
            print(outputList[i])
            
main()
