val = int(input('>>Enter a number:'))
if val > 100:
    val = val/2
else:
    val = val*2
print('>>The result is:', val)

# true situation if condition else false situation
val = int(input('>>Enter a number:'))
val = val / 2 if val > 100 else val * 2
print('>>The result is:', val)

name = input("Enter ur name")
if name.isalpha():
    print("very good")
else:
    print("not good")   

    