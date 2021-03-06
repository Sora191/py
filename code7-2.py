#code7-2.py

def getRatios(vect1, vect2):
    """vect1とvect2を同じ長さのリストとする
       vect1[i]とvect2[i]を意味する値からなるリストを返す"""
    ratios = []
    if len(vect1) != len(vect2):
        raise ValueError('getRatios called with bad arguments')
    for index in range(len(vect1)):
        vect1Elem = vect1[index]
        vect2Elem = vect2[index]
        if (type(vect1Elem) not in (int, float))\
            or (type(vect2Elem) not in (int, float)):
                raise ValueError('getRatios called with bad arguments')
        if vect2Elem == 0.0:
            ratios.append(float('nan'))
        else:
            ratios.append(vect1Elem/vect2Elem)
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
