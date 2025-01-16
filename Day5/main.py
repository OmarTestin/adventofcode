
# Online Python - IDE, Editor, Compiler, Interpreter
import math
pageRules = []
inputTest = []

readingPages = True

with open('input.txt', 'r') as file:
    for line in file:
        if line == "\n":
            print("break here")
            readingPages = False
            continue
        if readingPages:
            ruleValues = line.strip().split("|")
            pageRules.append(ruleValues)
        else:
            inputLineValues = line.strip().split(",")
            inputTest.append(inputLineValues)
            

def verifyValue(prevVal, curVal, nextVal):
    # could check for a specific rule by checking current input value and previous/next
    #check value against every value inside array
    #print("Checking", prevVal, curVal, nextVal)
    for rule in pageRules:
        if prevVal == None:
            if rule[0] == curVal and rule[1] == nextVal:
                return True
            else:
                #print("rule not work", rule[0], rule[1])
                continue
        else:
            if rule[0] == prevVal and rule[1] == curVal:
                return True
            else:
                #print("rule not work", rule[0], rule[1])
                continue
    return False

#main 

finalVal = 0

for inputLine in inputTest:
    previousVal = None
    currentVal = None
    validLine = True
    for idx, val in enumerate(inputLine):
        #print("reading line")
        currentVal = val
        if idx != 0:
            if not (verifyValue(previousVal, currentVal, None)):
                validLine = False
            previousVal = val
        else:
            previousVal = None
            if not (verifyValue(previousVal, currentVal, inputLine[idx+1])):
                validLine = False
            previousVal = val
            #print(inputLine)
    if validLine:
            finalVal += int(inputLine[math.ceil(len(inputLine)/2)-1])
            print("adding", int(inputLine[math.ceil(len(inputLine)/2)-1]))
            #print(inputLine)
    print(inputLine)
    print(validLine)
    
print(inputTest)
print(finalVal)

