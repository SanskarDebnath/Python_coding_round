#wrong code
passw = input("enter the password\n")

if passw is 'Password':
    print("access granted")
else:
    print("Access denied")


#correct code
passw = input("enter the password\n")

if passw == 'Password':
    print("access granted")
else:
    print("Access denied")


"""
basic difference between is and equalto : is execute the statement will be true if the both side referencing the same memory and location while 
equal to checks if the passw contains any Password keyword (the exact synatax or not)
"""