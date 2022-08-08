name = input("What is ur name=>")

print(name)
print(f"length: {len(name)}")

cl_name = name.strip() # remove leading and trailing whitespace or chars

print(cl_name)
print(f"length: {len(cl_name)}")

secret_msg = '000000000000000000OLA0000000000000'
print(secret_msg.strip('0'))
print(secret_msg.lstrip('0'))
print(secret_msg.rstrip('0'))

crap_msg='''
    
    hey brother
   
'''
clean_msg = crap_msg.strip()
print(crap_msg)
print(clean_msg)
print(f'{len(crap_msg)} --> {len(clean_msg)}')