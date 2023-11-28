import pandas as pd
import numpy as np
array1 = np.array(["Rama","Mohan","David","Jaffer","EKIP"])
array2 = np.array([36,45,50,38])#,[30,45,60,70]])
array3 = np.array([[100,200,300,400],[1000,2000,3000,5000]])
stDFObj = pd.DataFrame([array2,array3])#,index = ["St1","st2","St3","St4"],columns=["StName"])
print("The DataFrame created from string array :\n",stDFObj)
numArray = np.array([[1,2,3,4],[5,6,7,8]])
DFObj = pd.DataFrame(numArray,index = ["One","Two"],columns=["subj1","subj2","subj3","subj4"])
DFObj.index.name = "Serial No"
print("The DF Object:\n",DFObj)

stDictionary = {"Subj1":"English","Subj2":"english","Subj3":"Maths"}
stDataFrame = pd.DataFrame(stDictionary,index=[1])
print(stDataFrame)
seriesObj1 = pd.Series([1,2,2],index=[1,2,3])
seriesObj2 = pd.Series([100,200,2000],index=[1,2,4])
seriesDF = pd.DataFrame(seriesObj1)
print(seriesDF)
s2DataFrame = pd.DataFrame([seriesObj1,seriesObj2])
print(s2DataFrame)
