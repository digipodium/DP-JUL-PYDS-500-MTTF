class Fruit:
    color = 'red'
    taste = 'sweet'

class Veg:
    size = 'small'
    age = 'fresh'

class GM(Fruit, Veg):
    name = 'GM-122'

g = GM()

print(g.name)
print(g.color)
print(g.taste)
print(g.size)
print(g.age)

