def mainCalculator(str):
    listedString = str.split(" ")
    return calc(listedString)

#Recursive calculator
def calc(listedString):
    #Checks if the phrase is simple (no brackets/brackets only in the edges + 1 kind of operator (*/ or +-))
    if simple_phrase(listedString):
        # Calculates simple phrases, returns float
        return simple_calculator(listedString)
    #Checks if the phrase is "semi-simple" (no brackets/brackets only in the edges + 2 kind of operator (*/ and +-)). If it is - the function calculates it
    elif semi_simple_phrase(listedString):
        for element in range(0, len(listedString)-2):
            if element >= (len(listedString)-1):
                break
            elif not((listedString[element] == "*") or (listedString[element] == "/")):
                element += 1
            else:
                while ((listedString[element] == "*") or (listedString[element] == "/")):
                    if listedString[element] == "*":
                        listedString[element-1] = float(listedString[element-1]) * float(listedString[element+1])
                        listedString.pop(element)
                        listedString.pop(element)
                        if element >= len(listedString):
                            break
                    elif listedString[element] == "/":
                        listedString[element-1] = float(listedString[element-1]) / float(listedString[element+1])
                        listedString.pop(element)
                        listedString.pop(element)
                        if element >= len(listedString):
                            break
                    else:
                        continue
                element += 1
        return simple_calculator(listedString)
    #If the phrase is not simple/semi-simple
    else:
        #2-dimension array of start/end indexes of the outside brackets
        brackets_chunks = []
        brackets_chunks = brackets_finder(listedString)
        index = len(brackets_chunks) - 1
        calculatedBrackets = 0
        #Iterating the list backwards, adding the solved brackets and popping the brackets itself.
        while index >= 0:
            #If all the brackets has already been solved - it calculates them easily
            if simple_phrase(listedString) or semi_simple_phrase(listedString):
                return calc(listedString)
            else:
                calculatedBrackets = calc(listedString[brackets_chunks[index][0]:brackets_chunks[index][1]+1])
                listedString.insert(brackets_chunks[index][1] + 1, calculatedBrackets)
                endOfBrackets = brackets_chunks[index][1]
                startOfBrackets = brackets_chunks[index][0]
                poppedIndex = startOfBrackets
                while startOfBrackets <= endOfBrackets:
                    listedString.pop(poppedIndex)
                    startOfBrackets += 1
                index -= index

#Checks if the phrase is simple (no brackets/brackets only in the edges + 1 kind of operator (*/ or +-))
def simple_phrase(listedString):
    #Input test
    if listedString.count("(") != listedString.count(")"):
        return False
    if listedString[0] == "+" or listedString[0] == "-" or listedString[0] == "*" or listedString[0] == "/" or listedString[len(listedString)-1] == "+" or listedString[len(listedString)-1] == "-" or listedString[len(listedString)-1] == "*" or listedString[len(listedString)-1] == "/":
        return False
    #More than 1 brackets
    elif listedString.count("(") > 1 :
        return False
    #1 brackets only
    elif listedString.count("(") == 1:
        #Brackets in the edges
        if (listedString[0] == "(") and (listedString[len(listedString)-1] == ")"):
            #Checks if the phrase is only numbers and +- or */  and returns true/false
            return only_one_kind_of_operator(listedString)
        #Brackets in the middle
        else:
            return False
    #No brackets at all
    else:
        return only_one_kind_of_operator(listedString)


# Checks if the phrase is only numbers and +- or */ and returns true/false
def only_one_kind_of_operator(listedString):
    if (listedString.count("+") > 0 or listedString.count("-") > 0) and (listedString.count("*") > 0 or listedString.count("/") > 0):
        return False
    else:
        return True


# Calculates simple lists, must get a list which starts with "(" and ends with ")" or starts and ends with number. returns float
def simple_calculator(listedString):
    if listedString[0] == ("("):
        listedString.pop(len(listedString)-1)
        listedString.pop(0)
    if ((listedString[0] == "+") or (listedString[0] == "-") or (listedString[0] == "*") or (listedString[0] == "/") or (listedString[len(listedString)-1] == "+") or (listedString[len(listedString)-1] == "-") or (listedString[len(listedString)-1] == "*") or (listedString[len(listedString)-1] == "/")):
        print("simple calculator got a wrong statement: %s" % listedString)
        return 0
    else:
        calculated = float(listedString[0])
        for letter in range (0, len(listedString)-1):
            if listedString[letter] == "+":
                calculated += float(listedString[letter+1])
                letter += 1
            elif listedString[letter] == "-":
                calculated -= float(listedString[letter+1])
                letter += 1
            elif listedString[letter] == "*":
                calculated = calculated * float(listedString[letter + 1])
                letter += 1
            elif listedString[letter] == "/":
                calculated = calculated / float(listedString[letter + 1])
                letter += 1
            else:
                continue
        return float(calculated)

# Checks if the phrase is "semi-simple" (no brackets/brackets only in the edges + 2 kind of operator (*/ and +-))
def semi_simple_phrase(listedString):
    if listedString[0] == "+" or listedString[0] == "-" or listedString[0] == "*" or listedString[0] == "/" or listedString[len(listedString)-1] == "+" or listedString[len(listedString)-1] == "-" or listedString[len(listedString)-1] == "*" or listedString[len(listedString)-1] == "/":
        return False
    if listedString.count("(") != listedString.count(")"):
        return False
    #More than 1 brackets
    elif listedString.count("(") > 1 :
        return False
    #1 brackets only
    elif listedString.count("(") == 1:
        #Brackets only in the edges
        if (listedString[0] == "(") and (listedString[len(listedString)-1] == ")"):
            return True
        #Brackets in the middle
        else:
            return False
    #No brackets at all
    else:
        return True

#Returns 2-dimension array of start/end indexes of the outside brackets
def brackets_finder(listedString):
    brackets_indexes = []
    counter = 0
    inside = False
    startIndex = 0
    endIndex = 0
    changed = False
    if ((listedString[0] == "(") and listedString[len(listedString)-1] == ")"):
        listedString[0] = 1
        listedString[len(listedString)-1] = 1
        changed = True
    for index in range(0, len(listedString)):
        if listedString[index] == "(":
            counter += 1
            if counter == 1:
                inside = True
                startIndex = index
        elif listedString[index] == ")":
            counter -= 1
        else:
            continue
        if (counter == 0 and inside == True):
            endIndex = index
            brackets_indexes.append([startIndex, endIndex])
            inside = False
        if changed == True:
            listedString[0] = "("
            listedString[len(listedString) - 1] = ")"
    return brackets_indexes

print(mainCalculator("( 2 * 4 - 5 / ( 5 * 2 ) - ( 5 + 20 + ( 7 + ( 1 / 1 ) ) ) )"))