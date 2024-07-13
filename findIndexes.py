


def findIndexes(super_string,sub_string):
    indexes = list()  
    for index in range(len(super_string)):
        if index + len(sub_string) <= len(super_string):
           if sub_string == super_string[index:index+len(sub_string)]: 
              indexes.append((index,index + len(sub_string)))
    return indexes   


def removeSpaces(string): 
    return [character for character in string if character != ' ']




print(findIndexes('This is good, python1. Python2'.lower(),'python'))

