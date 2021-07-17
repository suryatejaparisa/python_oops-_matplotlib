class Paper:
    t_area = 0 #occupied area in the paper
    info = ""
    def __init__(self, area):
        self.area = area
        if self.area <0:
            try:
                raise Exception()
            except Exception as e:
                print(type(e))
                print("Paper should have positive area")
                return
        Paper.merge.has_been_called = False
    def status(info):
        Paper.info += info #gets the information about the items on the paper
    def __str__(self): #prints all the details about the paper
        return("Paper has free area "+str(self.area-Paper.t_area)+" out of "+str(self.area)+", and contains:\n"+Paper.info)
    def erase(self): #erases the paper area
        Paper.t_area = 0
        Paper.info = ""
    def merge(self, info=""):#merges polygons of similar sides
        Paper.merge.has_been_called = True
        Paper.info += info
        Polygon.update()

    def __add__(self, other): # adds the area of all the objects to paper area and calculates the free area in the paper
        Paper.t_area += other.area #overloading the plus operator
        free_area = self.area-Paper.t_area
        try:
            if free_area <0:
                raise Exception()
        except Exception as e:
            print(type(e))
            print("Paper does not have sufficient free area to fit the polygon")
        return(Paper(self.area))

class Polygon():
    trig = {}
    def __init__(self, numSides, area):
        self.numSides = numSides
        self.area = area
        if numSides in Polygon.trig: # creating trigger dict to find merging area values
            Polygon.trig[numSides] += self.area
        else:
            Polygon.trig[numSides] = self.area
        if Paper.merge.has_been_called == False :
            if numSides != 3:  #checks if polygon is a triangle or not
                p_str = "Polygon with "+str(numSides)+" sides and area "+str(area)+"\n"
            else:
                p_str = "Triangle with area "+str(area)+"\n"
            Paper.status(p_str)
    def update():
        p_str = ""
        for _ in Polygon.trig:
            p_str += "Polygon with "+str(_)+" sides and area "+str(Polygon.trig[_])+"\n"
            Paper.status(p_str)
class Triangle(Polygon):
    t_str = ""
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
        self.area = 0.5*s1*s2 #calculates the area of the triangle
        Triangle.t_str +="Triangle with area "+str(self.area)+"\n"
        Paper.status(Triangle.t_str)


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

"""
pap = Paper(200)
pap = pap + Polygon(10, 100)
pap = pap + Polygon(20, 50)
pap = pap + Triangle(3, 4, 5)
print(pap)
"""

"""
pap = Paper(200)
pap = pap + Polygon(3, 100)
print(pap)
"""
"""
pap = Paper(2000)
pap = pap + Polygon(10, 100)
pap = pap + Polygon(20, 50)
pap = pap + Polygon(10, 200)
pap = pap + Polygon(3,24)
pap = pap + Triangle(3, 4, 5)
print(pap)
pap.merge()
print(pap)
"""


pap = Paper(200)
pap = pap + Polygon(10, 100)
pap = pap + Polygon(20, 50)
pap = pap + Triangle(3, 4, 5)
print(pap)
pap.erase()
print(pap)

