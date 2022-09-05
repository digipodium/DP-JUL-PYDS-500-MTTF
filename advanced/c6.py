'''
wap to create a class Movie
that have properties like
- title
- rating
- year
then create a contructor and 
a function to display the info.
Also create 5 Movie object, store them in a list
then sort them by rating.
Easy peasy!
'''

class Movie:
    def __init__(self, title, rating, year):
        self.title = title
        self.rating = rating
        self.year = year

    def info(self):
        print(f'{self.title}({self.year}) -> {self.rating}')

    # > overloaded
    def __gt__(self, other):
        if self.rating > other.rating:
            return True
        else:
            return False

    def __lt__(self, other):
        if self.rating < other.rating:
            return True
        else:
            return False

    def __repr__(self):
        return self.title

m = Movie('Jab Tak Hain Jaan', 4.8, 2013)
m2 = Movie('Liger', 1, 2022)

print(m > m2)
print(m2 > m)

movies = [m, m2]
movies.sort()
print(movies)