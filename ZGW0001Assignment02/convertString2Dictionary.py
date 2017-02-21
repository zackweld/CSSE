import urllib

def convertString2Dictionary(inputString = ""):
    if inputString.__contains__("%3D"):
        errorDict = urllib.unquote(inputString)
        errorDict = errorDict.replace(',', '=')
        errorDict = errorDict.split('=')

        for index in range(len(errorDict)):
            # j = errorDict[index].replace(' ', '')
            j = errorDict[index].strip()
            errorDict[index] = j
            if errorDict[index] == "" or not errorDict[index][0].isalpha() or len(errorDict[index]) < 2 or errorDict[index].__contains__(' '):
                errorDict = {'error':'true'}
                print(errorDict)
                return errorDict

            for value in range(len(errorDict[index])):
                if not (errorDict[index][value].isalpha() or errorDict[index][value].isdigit() or errorDict[index][value] == "="):
                    errorDict = {'error':'true'}
                    print(errorDict)
                    return errorDict

            if index % 2 == 0:
                for even in range(index):
                    if even % 2 == 0:
                        if errorDict[index] == errorDict[even]:
                            errorDict = {'error':'true'}
                            print(errorDict)
                            return errorDict

            # Uncomment to see individual elements of the array as the pass or fail
            # print errorDict[index]

        dictionary = {errorDict[i]: errorDict[i+1] for i in range(0, len(errorDict), 2)}

        errorDict = dictionary
    else:
        errorDict = {'error':'true'}

    print(errorDict)
    return errorDict

#### Test inputs from the excel customer needs tab

# convertString2Dictionary("Key%3Dinput")
# convertString2Dictionary("function%20%3D%20get_stars")
# convertString2Dictionary("function%3D%20calculatePosition%2C%20sighting%3DBetelgeuse")
# convertString2Dictionary("key%3Dvalue%2C%20key%3Dvalue")
# convertString2Dictionary("Key%3D")
# convertString2Dictionary("1key%3Dvalue")
# convertString2Dictionary("k%3Dvalue")
# convertString2Dictionary('k%2Dey%3D%20value')
# convertString2Dictionary("key%3Dvalue%3bkey2%3Dvalue2")

