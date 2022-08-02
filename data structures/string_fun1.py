name = "Something serious is Not HaPPening"

# formatting function
print(name)
print( name.upper() )
print( name.lower() )
print( name.capitalize() )
print( name.title() )
print( name.swapcase() )
print( name.casefold() )

word = "python"

# left align
print( word.ljust(80) )
# right align
print( word.rjust(80) )
# center align
print( word.center(80) )

# fillchar examples
print( word.ljust(80,'-') )
print( word.rjust(80,'$') )
print( word.center(80,'~') )

# printing a formatted table of 3 
print('-'*40)
for i in range(1,21):
    r = 3 ** i
    print(3,'x',str(i).rjust(2),'=',r)