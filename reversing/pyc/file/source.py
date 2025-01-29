def flag():
    return 'FLAG{FLAG_IS_EDITED}'

def run():
    print("This code works in Python 3.8")
    print("Can you find the flag?")
    print("")
    print("")
    print("")
    win()

def win():
    a = 0.1
    b = 0.2
    c = 0.3
    if a + b == c:
        print(flag())
    else:
        print("Oops, this code doesn't seem to work. Why?")

run()
