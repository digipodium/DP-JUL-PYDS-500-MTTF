
import os

print('Current folder')
print(os.getcwd())
print(os.listdir())

print("C Drive content")
os.chdir('C:\\Program Files')
print(os.getcwd())
print(os.listdir())

address =r'C:\Program Files\Python\python.exe'
if os.path.exists(address):
    print('File exists')
else:
    print('File does not exist')