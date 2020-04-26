# problem 5.1: pattern matrix generator

array = [[ ['*' for col in range(6)] for col in range(4)] for row in range(3)]
print(array)


# problem 5.2: Reverse Dictionary Fetch

def get_key(val): 
    for key, value in my_dict.items(): 
         if val == value: 
             return key

my_dict ={"hello" : "world", "speckbit" : "self-learning", "life" : "meaning"} 
  
print(get_key("meaning"))

# problem 5.3 : Processing Skewed Names

bad_chars = ['%','!', '+', '23','6576']

given_string = "%Harry !Potter, !+Steven Rogers23, Peter6576"
for i in bad_chars : 
    given_string = given_string.replace(i, '') 
    
    print (str(given_string))

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

