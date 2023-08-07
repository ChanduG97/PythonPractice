import os
#--> listdir() is used to show current active directory
#print(os.listdir())

#--> os.mkdir() is used to create new directory
#print(os.listdir())
#os.mkdir("C:\\Users\\navee\PycharmProjects\pythonProject\\venv\Files")

#--> to remove specific directory we use os.rmdir()
#os.rmdir("C:\\Users\\navee\PycharmProjects\pythonProject\\venv\Files")
#print(os.listdir())

#os.mkdir("C:\\Users\\navee\Desktop\\nikhil")

myfile = open("C:\\Users\\navee\Desktop\\nikhil\\text.txt","w+")
myfile.seek(0,0)
print("The content in the nikhil directory text.txt is :\n",myfile.read())
myfile.seek(0,0)
myfile.write("\n this command is ueed for write command")
print(myfile.read())
'''
# to chage directory we use os.chdir()
os.chdir("C:\\Users\\navee\Desktop\\nikhil")
print(os.listdir())


#--> printing present working directory
print(os.listdir())

#--> to remove files in directory we use os.remove()
os.remove("C:\\Users\\navee\Desktop\\nikhil\y.txt")

#--> Remove directory os.rmdir()
os.rmdir("C:\\Users\\navee\Desktop\\nikhil")

'''



