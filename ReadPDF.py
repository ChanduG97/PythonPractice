import FileDetails
#To read a binary file and print the content in the Binary file
readfile = open("Words.pdf","rb+")
content = readfile.read()
print("The content in the file is : ",content)
