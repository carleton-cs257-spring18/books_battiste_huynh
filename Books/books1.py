import csv 
import sys
import re

def main():
    if (len(sys.argv)) < 3:
        print('Usage: not enough arguments', file=sys.stderr)
    else: 
        filename = sys.argv[1]
        action = sys.argv[2]
        if len(sys.argv) > 3:
            direction = sys.argv[3]
        else: 
            direction = "forward"
    
        if action != "books" and action!= "authors":
            print("Usage: action not included. Please enter books or authors as the second argument.", file=sys.stderr)
        elif direction != "forward" and direction != "reverse":
            print("Usage: misspelled direction. Please enter forward or reverse as the last argument or leave it blank.", file=sys.stderr)
        else:
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
