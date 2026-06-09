import os
import pandas as pd
import numpy as np
import csv
import glob
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn import preprocessing

def process(path,a1):
    data=pd.read_csv(path)
    print("Plates==",a1)
    X=data.drop(["class"],axis = 1) #droping out index from features too
    #X=X.rename(columns = lambda x:re.sub('[^A-Za-z0-9_]+', '', x))
    y=data["class"]

    l=[]
    #l.append("eswar")
    l.append(a1)
    
  
    
    #l.append(a11)
    
    
    
     
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    model2=KNeighborsClassifier(n_neighbors=7)
    X_test =pd.DataFrame([l])
    print("Testing data",X_test)
    model2.fit(X_train, y_train)
    y_pred = model2.predict(X_test)
    print("predicted")
    print(y_pred)
    result=""
    #treat=""
    if y_pred[0]==0:
        result="Normal"
        
    else:
        result="Thrombocytopenia"
       
        
    
    return result
#process("dataset.csv",152000)


