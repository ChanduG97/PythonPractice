import pandas as pd
seriesObj = pd.Series([1,2,2],index=["One","Two","Three"])
print(seriesObj)
listSeriesObj = pd.Series({1:1,2:2},index=["one","Two"])
print(listSeriesObj)
seriesObj.name = "numberSeries"
seriesObj.index.name="SL.No"
seriesObj["One"]= 1000
print(seriesObj[::-1])

