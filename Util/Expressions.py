def locationExpressionValue(expression, center_X = int, center_Y = int):

    if (type(expression) is str):
        if (expression in ["cX", "cx", "centerX", "centerx", "CenterX", "Centerx", "Cx", "CX", "center_X", "center_x", "Center_X", "Center_x"]):
            return center_X
        elif (expression in ["cY", "cy", "centerY", "centery", "CenterY", "Centery", "y", "CY", "center_Y", "center_y", "Center_Y", "Center_y"]):
            return center_Y
        formatList = locationExpressionFormatter(expression, center_X, center_Y)
    else:
        return expression
    
    exponentExists, processedListExponents = checkExponent(formatList)
    while (exponentExists):
         exponentExists, processedListExponents = checkExponent(processedListExponents)

    operationMDExists, processedListMD = checkMultiplicationOrDivision(processedListExponents)
    while (operationMDExists):
         operationMDExists, processedListMD = checkMultiplicationOrDivision(processedListMD)

    operationASExists, processedListAS = checkAdditionOrSubtraction(processedListMD)
    while (operationASExists):
        operationASExists, processedListAS = checkAdditionOrSubtraction(processedListAS)

    return processedListAS[0]

def operationValue(expression, variableDict):

    if (type(expression) is str):
        formatList = expressionFormatter(expression, variableDict)
    else:
        return expression
    
    exponentExists, processedListExponents = checkExponent(formatList)
    while (exponentExists):
         exponentExists, processedListExponents = checkExponent(processedListExponents)

    operationMDExists, processedListMD = checkMultiplicationOrDivision(processedListExponents)
    while (operationMDExists):
         operationMDExists, processedListMD = checkMultiplicationOrDivision(processedListMD)

    operationASExists, processedListAS = checkAdditionOrSubtraction(processedListMD)
    while (operationASExists):
        operationASExists, processedListAS = checkAdditionOrSubtraction(processedListAS)

    return processedListAS[0]

# Computes values for exponents symbols
def checkExponent(formatList):

    processedListExponents = []
    i = len(formatList)-1
    exponentExists = False
    while (i > 0):
        if (formatList[i-1] == "^" and exponentExists == False):
            processedListExponents.append(formatList[i-2]**formatList[i])
            exponentExists = True
            i -= 3
        else: 
            processedListExponents.append(formatList[i])
            i -= 1
    if (formatList[1] != "^"):
        processedListExponents.append(formatList[0])

    processedListExponents.reverse()

    return exponentExists, processedListExponents

# Computes values for multiplication and division symbols
def checkMultiplicationOrDivision(formatList):

    multiplicationExists = False
    processedListMD = []
    i = 0
    while (i < len(formatList)-1):
        if (formatList[i+1] == "*"):
            multiplicationExists = True
            processedListMD.append(formatList[i]*formatList[i+2])
            i += 3
            while (i < len(formatList)):
                processedListMD.append(formatList[i])
                i += 1
            break
        elif (formatList[i+1] == "/"):
            multiplicationExists = True
            if (formatList[i+2] != 0):
                processedListMD.append(formatList[i]/formatList[i+2])
            else:
                return "DIVISION BY 0"
            i += 3
            while (i < len(formatList)):
                processedListMD.append(formatList[i])
            i += 1
            break
        else: 
            processedListMD.append(formatList[i])
            i += 1
    if (formatList[len(formatList)-2] != "*" and formatList[len(formatList)-2] != "/"):
        processedListMD.append(formatList[len(formatList)-1])

    return multiplicationExists, processedListMD

# Computes values for addition and subtraction symbols
def checkAdditionOrSubtraction(formatList):

    operationExists = False
    processedListAS = []
    i = 0
    while (i < len(formatList)-1):
        if (formatList[i+1] == "-"):
            operationExists = True
            processedListAS.append(formatList[i]-formatList[i+2])
            i += 3
            while (i < len(formatList)):
                processedListAS.append(formatList[i])
                i += 1
            break
        elif (formatList[i+1] == "+"):
            operationExists = True
            processedListAS.append(formatList[i]+formatList[i+2])
            i += 3
            while (i < len(formatList)):
                processedListAS.append(formatList[i])
                i += 1
            break
        else: 
            processedListAS.append(formatList[i])
            i += 1

    if (formatList[len(formatList)-2] != "-" and formatList[len(formatList)-2] != "+"):
        processedListAS.append(formatList[len(formatList)-1])

    return operationExists, processedListAS

def locationExpressionFormatter(string, center_X, center_Y):

    #Removing Spaces
    string = string.split(" ")

    string = "".join(string)

    value = 0
    
    formatList = []
    operations = ["+","-","*","/","^", "(",")"]

    #Turning into a list of numbers and operations
    substring = ""
    for i in range(len(string)):
        if (string[i] in operations):
            if (substring in ["cX", "cx", "centerX", "centerx", "CenterX", "Centerx", "Cx", "CX", "center_X", "center_x", "Center_X", "Center_x"]):
                formatList.append(center_X)
            elif (substring in ["cY", "cy", "centerY", "centery", "CenterY", "Centery", "y", "CY", "center_Y", "center_y", "Center_Y", "Center_y"]):
                formatList.append(center_Y)
            elif (substring == ""):
                formatList.append(0)
            else:
                formatList.append(float(substring))
            formatList.append(string[i])
            substring = ""
        else:
            substring += string[i]
    if (substring == "cX"):
        formatList.append(center_X)
    elif (substring == "cY"):
        formatList.append(center_Y)
    elif (substring == ""):
        formatList.append(0)
    else:
        formatList.append(float(substring))

    return formatList

def expressionFormatter(string, variableDict):

    #Removing Spaces
    string = string.split(" ")

    string = "".join(string)

    value = 0
    
    formatList = []
    operations = ["+","-","*","/","^", "(",")"]

    #Turning into a list of numbers and operations
    substring = ""
    for i in range(len(string)):
        if (string[i] in operations):
            try:
                formatList.append(variableDict[substring])
            except:
                print("ERROR! " + substring + " symbol not found")
                return "ERROR"
            if (substring == ""):
                formatList.append(0)
            else:
                formatList.append(float(substring))

            formatList.append(string[i])
            substring = ""
        else:
            substring += string[i]
            
    try:
        formatList.append(variableDict[substring])
    except:
        print("ERROR! " + substring + " symbol not found")
        return "ERROR"

    if (substring == ""):
        formatList.append(0)
    else:
        formatList.append(float(substring))

    return formatList

#Testing
#print(locationExpressionValue("cX+171-600-2", 500, 300))
