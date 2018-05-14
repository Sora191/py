
#test6.py

def readVal(valType, requestMsg, errorMsg):
    while True:
        val = raw_input(requestMsg + ' ')
        try:
            val = valType(val)
            return val
        except ValueError:
            print val, errorMsg

readVal(int, 'Enter an integer: ', 'is not an integer')


Enter an integer:  abc
abc is not an integer
Enter an integer:  1.91
1.91 is not an integer
Enter an integer:  5
