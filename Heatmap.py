!pip install pandas
import pandas as pd
myDf=pd.read_csv('B.csv')
myDf.head()
myOrd1=myDf['Day']
myOrd2=myDf['Coin']
myCrossTable=pd.crosstab(myOrd1,myOrd2)
myCrossTable
up=myCrossTable
up
up.style.background_gradient(cmap='YlOrRd')
import seaborn as sns
sns.heatmap(up,annot=True,cmap='YlOrRd')
