mydict = {1:"One","two":2,"Fruits":["Apple","Mango","Grape"],4:"Dairy products"}
print(mydict)
uDict = {1:"Food","Liquid":10,"Ndict":{1:2,2:3,3:4}}
print(uDict.items())
mykeys = uDict.keys()
#print("The keys represented as list and 3rd key is  : ",mykeys[2]) #--> RETURNS ERROR
mykeys = list(uDict.keys())
print("The keys represented as list and 3rd key is  : ",mykeys[2])
print(uDict.values())
concatDict ={**mydict, **uDict}
print(concatDict)
