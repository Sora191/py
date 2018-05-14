#test1.py

numSuccesses = 191
numFailures = 0

succesFailureRatio = numSuccesses/float(numFailures)
print 'The success/failure ratio is', succesFailureRatio
print 'Now here'


Traceback (most recent call last):
  File "D:\pleiades\workspace\rinkou\src\test.py", line 6, in <module>
    succesFailureRatio = numSuccesses/float(numFailures)
ZeroDivisionError: float division by zero
