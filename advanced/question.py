num = '123'
out = 'one hundred twenty three'
elm = list(num)
num_map = {
    1: 'one',
    2: 'two',
    3: 'three',
    4: 'four',
    5: 'five',
    6: 'six',
    7: 'seven'    
}
print(elm)
unit_val = num_map.get((int(elm[-1])))
print(unit_val)