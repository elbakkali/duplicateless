import os
import pprint
import io

def getListOfFiles(dirName):
    listOfFile = os.listdir(dirName)
    allFiles = list()
    for entry in listOfFile:
        fullPath = os.path.join(dirName, entry)
        if os.path.isdir(fullPath):
            allFiles = allFiles + getListOfFiles(fullPath)
        else:
            allFiles.append(fullPath)
                
    return allFiles        

def main():
    dirName = 'D:\\'
    
    listOfFiles = list()

    for (dirpath, dirnames, filenames) in os.walk(dirName):
        listOfFiles += [os.path.join(dirpath, file) for file in filenames]
        
    sortedDuplicates = {}

    for elem in listOfFiles:
        if os.path.splitext(elem)[1] == '.jpg':
            sortedDuplicates[elem] = os.path.basename(elem)

    sorted_x = sorted(sortedDuplicates.items(), key=lambda kv: kv[1])
    previousElem = ''
    # fileObject = open('filesList.txt', 'w')
    fileObject = io.open('filesList.txt', 'w', encoding="utf-8")
    
    for elem in sorted_x:
        valueToAdd = elem[0]
        if elem[1] == previousElem:
            valueToAdd = '*********   ' + elem[0]
        previousElem = elem[1]
        fileObject.write(valueToAdd + '\n')

    fileObject.close()
    print('DOOOONE')

if __name__ == '__main__':
    main()