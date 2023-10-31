# Directory Operations
import os
print('The current working directory is :\n')
print(os.getcwd())
print('\nList contents of Directory...\n')
print(os.listdir())
print('\nCreate mydir')
os.mkdir('mydir')
print('\nThe updated list of directories...\n')
print(os.listdir())