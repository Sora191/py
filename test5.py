#test5.py

def readInt():
    while True:
        val = raw_input('Enter an integer: ')
        try:
            val = int(val)
            return val
        except ValueError:
            print val, 'is not an integer'

readInt()


Enter an integer: abc
abc is not an integer
Enter an integer: 1.91
1.91 is not an integer
Enter an integer: 5
