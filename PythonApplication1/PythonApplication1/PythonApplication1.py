import random
import numpy as np

h = int(input("How many rows is your quilt? "))
10
w = int(input("How many columns is your quilt? "))
10
total = (h * w)

p = int(input("Enter number of quilt block patterns: "))
10
mypatterns = dict((el,0) for el in range(p))


for item in mypatterns:
    pattern = item + 1
    mypatterns[item] = input('How many blocks of Pattern {P} do you have? '.format(P=pattern))

myquilt = [[0] * w for i in range(h)]
#print(np.matrix(myquilt))
	
	
	
	

def grid_maker(h, w):
    return [
        [str(random.randint(1, 100)) for _ in range(w)]
        for _ in range(h)
    ]
print ('\n'.join(' '.join(row) for row in grid_maker(h, w)))
