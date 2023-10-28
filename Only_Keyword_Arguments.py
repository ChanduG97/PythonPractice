#only keyword arguments

def names(**kwargs):
    for key in kwargs.keys():
        print('key :',key,'has value',kwargs[key])
names(a=1,b=2,c=3,d=4,e=5,f=6)