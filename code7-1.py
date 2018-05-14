#code7-1.py

def getRatios(vect1, vect2):
    ratios = []
    for index in range(len(vect1)):
        try:
            ratios.append(vect1[index]/float(vect2[index]))
        except ZeroDivisionError:
            ratios.append(float('nan'))
        except:
            raise ValueError('getRatios called with bad arguments')
    return ratios



try:
    print getRatios([1.0,2.0,7.0,6.0], [1.0,2.0,0.0,3.0])
    print getRatios([],[])
    print getRatios([1.0,2.0], [3.0])
except ValueError, msg:
    print msg


[1.0, 1.0, nan, 2.0]
[]
getRatios called with bad arguments
