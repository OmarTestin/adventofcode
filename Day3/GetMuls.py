
import os
#print(os.listdir())

charsFound = []
totalAmount = 0
inputFile = "Day3/input.txt"

with open(inputFile, "r") as file:
    fileSize =  os.path.getsize(inputFile)
    #print(fileSize)
    for x in range(fileSize):
        charsFound.append(file.read(1))

#print(charsFound)

inExpression = False
gettingFirstNum = True
gettingSecondNum = False
gettingComma = False
gettingRightString = False
leftStringHolder = ''
firstNum = ''
secondNum = ''
matchingLeftString = 'mul('

def matchStrings(currIndex):
    for idx, item in enumerate(matchingLeftString):
        if item != leftStringHolder[idx]:
            currIndex += 1
            if currIndex > 8:
                print(charsFound[currIndex - 8: currIndex])
            return False
    global inExpression
    inExpression = True
    return True

def checkIfCharInString(char):
    global leftStringHolder
    leftStringHolder += char
    if leftStringHolder[0:len(leftStringHolder)] == matchingLeftString[0:len(leftStringHolder)]:
        if len(leftStringHolder) == len(matchingLeftString):
            global inExpression
            inExpression = True
        return True
    else:
        leftStringHolder = ''
        return False

def resetVars(currIndex):

    currIndex += 1
    # if currIndex > 8:
    #     print(charsFound[currIndex - 8: currIndex])

    global inExpression
    inExpression = False
    global gettingFirstNum
    gettingFirstNum = True
    global gettingSecondNum
    gettingSecondNum = False
    global gettingComma
    gettingComma = False
    global gettingRightString
    gettingRightString = False
    global leftStringHolder
    leftStringHolder = ''
    global firstNum
    firstNum = ''
    global secondNum
    secondNum = ''

def mulNumbers():
    global firstNum
    global secondNum
    global totalAmount
    tempFirstNum = int(firstNum)
    tempSecondNum = int(secondNum)
    totalAmount += (tempFirstNum * tempSecondNum)

#loop here
for idx, char in enumerate(charsFound):
    if inExpression:
        #print("evaluating numbers")
        if gettingFirstNum:
            if char == ',' and firstNum != '':
                gettingFirstNum = False
                gettingSecondNum = True
                continue
            if char.isdigit():
                firstNum += char
                continue
            else:
                firstNum += char
                #print(firstNum)
                resetVars(idx)
                continue
        if gettingSecondNum:
            if char == ')' and secondNum != '':
                gettingSecondNum = False
                # multiply numbers and add to total amount
                mulNumbers()
                #print("mul added")
                resetVars(1)
                continue
            if char.isdigit():
                secondNum += char
                continue
            else:
                secondNum += char
                #print(firstNum)
                #print(secondNum)
                resetVars(idx)
                continue
    else:
        if checkIfCharInString(char):
            continue
    
print(totalAmount)

