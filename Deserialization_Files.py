#Deserialization
import json
f = open('sampledata.txt','r')
student = json.load(f)
print('The data read is : ',student,type(student))
f.close()