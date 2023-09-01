import os
new_file = open("C:\\Users\\navee\PycharmProjects\pythonProject\\venv\\Words.pdf","rb")
print("Current working directory:", os.getcwd())
print("Active directory:", os.path.abspath(os.curdir))
output_file = open("C:\\Users\\navee\PycharmProjects\pythonProject\\venv\outputfile.pdf","ab+")

new_file.close()
