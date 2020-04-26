# problem 5.3 : Processing Skewed Names

bad_chars = ['%','!', '+', '23','6576']

given_string = "%Harry !Potter, !+Steven Rogers23, Peter6576"
for i in bad_chars : 
    given_string = given_string.replace(i, '') 
    
    print (str(given_string))