
# Online Python - IDE, Editor, Compiler, Interpreter

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
            

def verifyValue(value, listArr):
    #check value against every value inside array
    valPos = listArr.index(value)
    #verify value against page rules
        #verify val as in page rules
    for ruleArr in pageRules:
        if ruleArr[0] == value: ##66,72
            for otherVal in listArr:
                if listArr.index(otherVal) > valPos and otherVal == ruleArr[1]:
                    return False
            
            
            
                
            
            
    return True

#main 

finalVal = 0

for inputLine in inputTest:
    for val in inputLine:
        if verifyValue(val, inputLine):
            finalVal += int(inputLine[round(len(inputLine)/2)])
            #print(inputLine)
            
print(finalVal)


