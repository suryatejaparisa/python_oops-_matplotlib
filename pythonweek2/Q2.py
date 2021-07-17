import matplotlib.pyplot as plt
class PieChart:
    def __init__(self, info):
        self.info = info
        try:
            if type(self.info) == dict:
                for _ in self.info.keys():
                    if type(_) != str:
                        raise Exception()
            if type(self.info) == set:
                if str not in self.info:
                    raise Exception()

        except Exception as e: #raises exception if any of keys is not string
            print(type(e))
            print("Label should be string")
            return
        try:
            for _ in self.info.values():
                if type(_) != int:
                    raise Exception() #raises exception if values is not a integer
                else:
                    if _ < 1:
                        raise Exception()  # raises exception if value is lessthan 1
        except Exception as e:
            print(type(e))
            print("Value should be a postive numeric")
            return
        self.label = self.info.keys()
        self.value = self.info.values()


    def __add__(self, other):
        if type(other) == tuple:
            if other[0] in self.info.keys():  #adding already existing type into piechart
                self.info[other[0]] += other[1]
            else:
                self.info[other[0]] = other[1] #adding new item into piechart
        if type(other) == PieChart: # checks whether adding object type is PieChart or not
            for _ in other.info.keys():
                if _ in self.info.keys(): #way to add other items if already added previuosly
                    other.info[_] += self.info[_]
            self.info.update(other.info)
        return self
    def __sub__(self, other):
        if other in self.info.keys():
            del self.info[other] #deleting the item types if already present and leaving as it is when new item is deleted
        else:
            pass
        return self
    def show(self):
        plt.pie(self.value, labels = self.label, autopct='%0.1f%%') #plotting pie chart
        plt.show()




#p = PieChart({1 : 23})

#p = PieChart({'Frog': '30'})

#p = PieChart({'Frog': -10})

p = PieChart({'Frogs': 10, 'Dog': 25})


p = PieChart({'Frogs': 10, 'Dog': 25})
p = p + ('Cat', 25)

"""
p = PieChart({'Frogs': 10, 'Dog': 25})
p = p + ('Dog', 25)
"""

"""
p = PieChart({'Frogs': 10, 'Dog': 20})
p = p + PieChart({'Frogs': 20, 'Cat': 10})
"""

"""
p = PieChart({'Frogs': 10, 'Dog': 20, 'Cat':30})
p = p - 'Frogs'
p = p - 'Lions'
"""
p.show()


