name = 'sanskar'

if name == 'bob' or 'Sam' or 'mike':
    print ("Access Granted")
else:
    print("access denied")


#actually python see this like this (name == 'bob') or ('sam') or ('mike') if name =='bob' return false then it will see the or part and here it is a string
#but python see it is a empty string and return True value so the if statement executed

"""

how to  fix this

"""

name = 'sanskar'
if name == ['bob' or 'sam' or 'mike']:
    print("Access granted")
else:
    print("Access denied")