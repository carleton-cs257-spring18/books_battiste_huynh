import csv 
import sys
import re

#def findLastName(name):
#    lastName = name.split(' ')[-2]
#    print(lastName)
#    return lastName

def main():
    filename = sys.argv[1]
    action = sys.argv[2]
    direction = sys.argv[3]
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
                outputList.sort(key = lambda name: name.split(' ')[-1])
            elif direction == "reverse":
                outputList.sort(key = lambda name: name.split(' ')[-1], reverse=True)
            else:
                print("Improperly added direction")
        for i in range(len(outputList)):
            print(outputList[i])
main()
