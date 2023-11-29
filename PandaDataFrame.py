import pandas as pd
import numpy as np
array1 = np.array(["Rama","Mohan","David","Jaffer","EKIP"])
array2 = np.array([36,45,50,38])#,[30,45,60,70]])
array3 = np.array([[100,200,300,400],[1000,2000,3000,5000]])#(2,2,4)--Shape
stDFObj = pd.DataFrame(array3,index=["row1","row2"],columns=["col1","col2","col3","col4"])#[array2,array3])#,index = ["St1","st2","St3","St4"],columns=["StName"])
print("The DataFrame created from string array :\n",stDFObj)
print("The element at col3 and row1 \n",stDFObj["col3"].loc["row2"])
print("The row1 is shown as  :\n",stDFObj.loc["row1"])
numArray = np.array([[1,2,3,4],[5,6,7,8]])
DFObj = pd.DataFrame(numArray,index = ["One","Two"],columns=["subj1","subj2","subj3","subj4"])
DFObj.index.name = "Serial No"
print("-"*50,"\nThe DF Object:\n",DFObj)

stDictionary = {"Subj1":"English","Subj2":"english","Subj3":"Maths"}
stDataFrame = pd.DataFrame(stDictionary,index=[1])
print(stDataFrame)
seriesObj1 = pd.Series([1,2,3],index=[100,200,2000])
seriesObj2 = pd.Series([100,200,2000],index=[1,2,4])
print("The series Obj1 is shown as :\n",seriesObj1)
seriesDF = pd.DataFrame(seriesObj1)
seriesDF1= pd.DataFrame(seriesObj1,columns=["Numbers"])
print("The series1 is shown in DataFrame is :\n",seriesDF1)
print("-"*50,"\n",seriesDF)
s2DataFrame = pd.DataFrame([seriesObj1,seriesObj2])
print("The two Series DataFrame :\n",s2DataFrame)