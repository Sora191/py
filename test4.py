

#test4.py

while True:
    val = raw_input('Enter an integer: ')
    try:
        val = int(val)
        print 'The square of the number you entered is ', val**2
        break
    except ValueError:
        print val, 'is not an integer'
        

Enter an integer: abc
abc is not an integer
Enter an integer: 1.91
1.91 is not an integer
Enter an integer: 10
The square of the number you entered is  100
