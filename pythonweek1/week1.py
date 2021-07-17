#list comprehension

m = 5
n = 5

#example1

"""
cubes = []
for i in range(m+1):
	cubes.append(i**3)
print(cubes)
"""

#print([i**3 for i in range(m+1)])

#example2
#initialize 2d matrix data with multiples of 1st m natural numbers in each corresponding row


#print([[i * j for j in range(1, n+1)] for i in range(1, m+1)])


"""
l1 = []
for i in range(1, m+1):
	l2 = []
	for  j in range(1, n+1):
		l2.append(i * j)
	l1.append(l2)
		
#print(l1)

"""	


#==================================================

#iterators

"""

iter_list = iter(l1)
for i in range(5):
	print(next(iter_list))
"""


"""
iter_list = iter(l1)
for i in range(6):
	print(next(iter_list))

"""

#==================================================

#generators

#example1


"""
def square(num):
	for _ in range(1,num+1):
		yield(_**2)
print(sum(square(5)))

"""

#example 2



def odd():
    x = 1
    while True:
        yield x
        x += 2
limit = 100
for _ in odd():
    if _ < limit:
    	print(_,end=", ")
    else:
        break
