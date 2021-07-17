class Polygon():
    def __init__(self, numSides, area): 
        self.numSides = numSides
        self.area = area
class Triangle(Polygon):	#inherited Polygon class
    def __str__(self):
        return("Triangle with area "+str(self.area))
    def __init__(self, *args):   #unpacking the passed values into *args
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
#t = Triangle(1, -2, 3)                
#t = Triangle(3, 2, 1)          
t = Triangle(3, 4, 5)
print(t)
