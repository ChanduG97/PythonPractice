#serialization
import json
f = open('sampledata.txt','w')
student = {'Name' :'Marif','City' : 'dubai','DOB' : 1997}
json.dump(student,f)
f.close()
