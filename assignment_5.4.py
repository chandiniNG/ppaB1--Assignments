# problem 5.4 : Fixing Blog Titles

string = 'TheProgrammersGuideToEffectiveLearning'

def spacer(str):

    sentence = []                 # create empty list

    sentence.append(str[0])       # put first letter in list. First letter doesn't need a space.
    for char in str[1::]:         # begin iteration after first letter
        if char.islower():
            sentence.append(char) # if character is lower add to list
        elif char.isupper():
            sentence.append( " ") # if character is upper add a space to list
            sentence.append(char) # then add the upper case character to list  
    result = ''.join(sentence)    # use () join to convert the list to a string
    return result                 # return end result

spacer(string)

# problem_2:

string = 'MyReviewOfTheNewPhone:SamsungGalaxyS9'

def spacer(str):

    sentence = []                 # create empty list

    sentence.append(str[0])       # put first letter in list. First letter doesn't need a space.
    for char in str[1::]:         # begin iteration after first letter
        if char.islower():
            sentence.append(char) # if character is lower add to list
        elif char.isupper():
            sentence.append( " ") # if character is upper add a space to list
            sentence.append(char) # then add the upper case character to list  
    result = ''.join(sentence)    # use () join to convert the list to a string
    return result                 # return end result

spacer(string)

