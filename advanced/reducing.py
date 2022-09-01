from functools import reduce
import operator

x = [2,3,1,3,4,5,1,2,3,4]

# multiply all values of x 

ans = reduce(operator.mul, x)
print(ans)

# same as
# ans = 1
# for i in x:
#     ans *= i
# print(ans)

ans2 = reduce(lambda i,j: i+i*j+i, x)
print(ans2)