x = [1,2,3,3,5,1,2,3,1,2]

x2 = list(map(lambda i: i**2, x))

x3 = tuple(map(lambda i: i**3, x)) # tuple with x cubes

print(x2)
print(x3)

y = ['apple','banana','cherry']
z = ['pie','shake','jam']

words = set(map(lambda a,b: a+'-'+b, y,z))
print(words)

# single line input with multiple values

numbers = list(map(int, input('enter 10 numbers:').split()))
print(numbers)