# fixing c1 using constructor

class Dog:
    def __init__(self, color, breed, gender, age, h=1, w=5):
        print('Dog created')
        self.color = color
        self.breed = breed
        self.gender = gender
        self.age = age
        self.height = h
        self.weight = w
    def bark(self, sound='bow'):
        print(sound * 5)
    def upd_weight(self, new_w):
        self.weight = new_w  
    
tommy = Dog('red','german sheperd', 'male', 5)

charlie = Dog('black','bull dog','female',1, .5, 3)

tommy.bark()
tommy.upd_weight(6)

print(tommy.age, tommy.weight, tommy.breed)



