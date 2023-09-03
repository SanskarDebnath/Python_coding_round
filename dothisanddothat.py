def do_this():
    print("I am doing this")

def do_that():
    print ("i am doing that")

match input("do this or that\n"):
    case 'this':
        do_this()
    case 'that':
        do_that()
    case _:
        print("Invalid input")