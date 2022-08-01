name = "Vijay Deenanath Chauhan"
# firstname
firstname = name[:5]
print(firstname)
lastname = name[-7:]
print(lastname)
middlename = name[6:-8]
print(middlename)
even_index = name[::2]
print(even_index)
odd_index = name[1::2]
print(odd_index)    
# reversing a sequence with slicing
reversed_name = name[::-1]
print(reversed_name)
print(name[:]) # wont affect
print(name[::-1][:7][::-1])