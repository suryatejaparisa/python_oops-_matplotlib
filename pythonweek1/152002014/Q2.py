class Polygon:
    def __init__(self, numSides, area):
        self.numSides = numSides	
        self.area = area
        try:
            if self.numSides < 3:	# raises exception if sides < 3
                raise Exception()
        except Exception as e:
            print(type(e))
            print("Number of sides should be atleast 3")
        try:
            if self.area<0:		# raises exception if area is negative
                raise Exception()
        except Exception as e:
            print(type(e))
            print("Polygon should have positive area")
        if (self.numSides >2 and self.area >-1) :	# prints only if polygon has valid sides and non-negative area
            print("Polygon with",self.numSides,"sides and area",self.area)


#p = Polygon(10, 23)
#print(p)
#p = Polygon(2, 23)
#print(p)
#p = Polygon(10, -1)
#print(p)
p = Polygon(2, -3)
print(p)
