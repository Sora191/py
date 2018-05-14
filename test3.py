
#test3.py

val = int(raw_input('Enter an integer: '))
print 'The square of the number you entered is ', val**2



Enter an integer: abc
Traceback (most recent call last):
  File "D:\pleiades\workspace\rinkou\src\test.py", line 9, in <module>
    val = int(raw_input('Enter an integer: '))
ValueError: invalid literal for int() with base 10: 'abc'


Enter an integer: 5
The square of the number you entered is  25
