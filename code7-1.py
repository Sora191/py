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





v1 = [0,1,2,3]
v2 = [1,0,1,0]

print 'ratios =', getRatios(v1, v2)



ratios = [0.0, nan, 2.0, nan]
