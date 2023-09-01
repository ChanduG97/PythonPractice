class Node:
    stackData = None
    nextObjAddress = None
class Stack:
    def _init_(self,inputData):
        self.data = inputData
    def is_empty(self,nodeObj):
        return (nodeObj.nextObjAddress == None)
    def push(self, inputData):
        return self.data.append(inputData)
    def pop(self):
        if not self.is_empty():
            return self.data.pop()
        else:
            raise IndexError("stack is empty")
    def peek(self):
        if not self.is_empty():
            return self.data[-1]
        else:
            raise IndexError("stack is empty")
stack=Stack()
while(True):
    currObj = Stack(inputData)
    currObj.nextObjAddress = id(nextObj)
    nextObj = Stack(input)
    ObjAvailable = input("Enter Yes to Continue and No to break (Y/N)  :" )
    if(ObjAvailable.lower() == "y") :
        newObj = Stack(inputVal)
        nextObj.nextObjAddress = id(newObj)
    else:
        nextObj.nextObjAddress = None
        nextObj.nextObjAddress = None