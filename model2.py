import numpy as np
import pandas as pd
import pickle

data=pd.read_csv("Admission_Predict.csv")

x=data.iloc[:,1:8]
y=data.iloc[:,-1]

from sklearn.ensemble import RandomForestRegressor
reg=RandomForestRegressor(n_estimators=100,random_state=0)
reg.fit(x,y)

pickle.dump(reg, open('model2.pkl','wb'))

model2 = pickle.load(open('model2.pkl','rb'))

a=model2.predict([[300,118,4,4.5,4.5,9.65,1]])
print("Chances of admit is: ",a)