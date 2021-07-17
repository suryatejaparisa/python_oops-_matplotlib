class Paper:
    def __init__(self, area):
        self.area = area
        if self.area <0:
            try:
                raise Exception()
            except Exception as e:
                print(type(e))
                print("Paper should have positive area")
                return
    def __add__(self, other):
        self.area -= other.area
        try:
            if self.area <0:
                raise Exception()
        except Exception as e:
            print(type(e))
            print("Paper does not have sufficient free area to fit the polygon")
        print("Paper has free area out of",self.area," and contains:") 
        return(Paper(self.area))

class Polygon():
    def __init__(self, numSides, area):
        self.numSides = numSides
        self.area = area
class Triangle(Polygon):
    def __init__(self, *args):
        s1, s2, s3 = args
        try:
            if (s1<1 or s1<1 or s3<1):
                raise Exception()
        except Exception as e1:
            print(type(e1))
            print("Triangle should have postive side-lengths")
            return
        try:
            if ( (s1 >= s2+s3) or (s2 >= s1+s3) or (s3 >= s1+s2) ):
                raise Exception()
        except Exception as e2:
            print(type(e2)) 
            print("Side-lengths do not form a triangle")
            return
        self.area = 0.5*s1*s2
        print("Triangle with area",self.area)


#pap = Paper(-1)

"""
pap = Paper(200)
p = Polygon(10, 100)
pap = pap + p
pap = pap + Polygon(5, 45)
print(type(pap).__name__)
"""
"""
pap = Paper(200)
p1 = Polygon(10, 100)
p2 = Polygon(20, 150)
pap = (pap + p1) + p2
"""

pap = Paper(200)
pap = pap + Polygon(10, 100)
pap = pap + Polygon(20, 50)
pap = pap + Triangle(3, 4, 5)
print(pap)
#don't forget to submit report
