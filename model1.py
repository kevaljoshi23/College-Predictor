import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import pickle

df=pd.read_csv('pred.csv')
df = df.drop('Year',axis = 1)
df = df.drop('12th Division',axis = 1)

x = df.iloc[:,:-1]
y = df.iloc[:,-1]

from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import LabelEncoder
le= LabelEncoder()
y = le.fit_transform(y)

from sklearn.ensemble import RandomForestRegressor
rfr = RandomForestRegressor(n_estimators=50,random_state=42)

rfr.fit(x,y)

pickle.dump(rfr, open('model1.pkl','wb'))

model1 = pickle.load(open('model1.pkl','rb'))

c=model1.predict([[86,89,4563]])
l=int(c)
o=round(l)
if o==8:
    print("IIT BOMBAY")
if o==10:
    print("IIT DELHI")
if o==17:
    print("IIT KANPUR")
if o==18:
    print("IIT KHARAGPUR")
if o==12:
    print("IIT GUWAHATI")
if o==13:
    print("IIT HYDRABAD")
if o==32:
    print("Netaji Subhas IT")
if o==29:
    print("NIT TRICHY")
if o==14:
    print("IIT INDORE")
if o==2:
    print("BITS PILANI")
if o==23:
    print("JADAVPUR UNIVERSITY")
if o==37:
    print("VIT VELLORE")
if o==4:
    print("DTU Delhi")
if o==21:
    print("IIT ROPAR")
if o==19:
    print("IIT MANDI")
if o==7:
    print("IIIT HYDRABAD")
if o==30:
    print("NIT WARANGAL")
if o==22:
    print("IIT TIRUPATI")
if o==5:
    print("HBUT KANPUR")
if o==26:
    print("MNNIT ALLAHABAD")
if o==11:
    print("IIT GOA")
if o==28:
    print("MANIPAL IT")
if o==20:
    print("IIT PALAKKAD")
if o==0:
    print("AHEMEDABAD IT")
if o==33:
    print("SOA UNIVERSITY")
if o==34:
    print("SRM CHENNAI")
if o==9:
    print("IIT BHILLAI")
if o==15:
    print("IIT JAMMU")
if o==31:
    print("NMIMS")
if o==16:
    print("IIT JODHPUR")
if o==35:
    print("SSN college of ENGG")
if o==6:
    print("IIEST SHIBPUR")
if o==24:
    print("KLEF HYDRABAD")
if o==36:
    print("UNIVERSITY COLLEGE OF ENGG")
if o==1:
    print("BIT MESRA")
if o==25:
    print("MNIT JAIPUR")
if o==3:
    print("BMS COLLEGE OF ENGG")
if o==27:
    print("MSIT")