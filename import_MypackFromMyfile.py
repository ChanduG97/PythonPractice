### 2.Write a Python program that searches for a file, obtains its size and reports the size in bytes/ KB/ MB as appropriate


import mypack.myfile as mf

filename = input('Enter the file name :')

print('The size of file is ',mf.file_size(filename))