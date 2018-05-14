#test1.py

numSuccesses = 191
numFailures = 191

try:
    successFailureRatio = numSuccesses/float(numFailures)
    print 'The success/failure ratio is ', successFailureRatio
except ZeroDivisionError:
    print 'No filures so the success/failure ratio is undefined.'
print 'Now here'


The success/failure ratio is  1.0
Now here
