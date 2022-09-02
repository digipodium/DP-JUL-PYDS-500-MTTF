
class Dog:

    age = 0
    weight = 0
    height = 0
    color = ''
    breed = ''
    gender = ''

    def bark(self):
        print('🐶bow'* 3)
    
    def wag(self):
        print('wags tails')

    def eat(self, food):
        print(f'dog {food} kha raha h')


tommy = Dog() # calling the constructor
tommy.age = 3
tommy.breed = 'street dog'
tommy.color = 'black'
tommy.gender = 'male'
tommy.height = 1
tommy.weight = 5

charlie = Dog()
charlie.age = 4
charlie.breed = 'bull dog'
charlie.color = 'gray'
charlie.gender = 'female'
charlie.height = 1.1
charlie.weight = 8

jimmy = Dog()
jimmy.age = 2
jimmy.breed = 'husky'
jimmy.color = 'black n white'
jimmy.gender = 'male'
jimmy.height = .8
jimmy.weight = 6

jimmy.bark()
jimmy.eat('fish')
charlie.eat('dog-food')
tommy.eat('bachhi hui roti')
tommy.eat('bachhi hui daal')
tommy.bark()
jimmy.bark()






