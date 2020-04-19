name1 = input('Enter the first name: ')             # input for the first name
usn1 = int(input('Enter the first USN: '))          # input for the first usn
name2 = input('Enter the second name: ')            # input for the second name
usn2 = int(input('Enter the second USN: '))         # input for the second usn
name3 = input('Enter the third name: ')             # input for the third name
usn3 = int(input('Enter the third USN: '))          # input for the third usn

d = {}                                              # creating an empty dictionary

mylist = [(name1, usn1), (name2, usn2), (name3, usn3)] # creating a list of name and usn pair

for name, usn in mylist:                            # 'for' loop to append the name and usn pair 
    d[usn] = name                                   #   to the creted dictionary
print(d)                                            # printing the dictionary  

for key, value in d.items():                        # printing the key value pairs line by line
    print(key, ':', value)