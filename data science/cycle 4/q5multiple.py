import pandas as pd
import numpy as np

import matplotlib.pyplot as plt
print("Register No: SJC22MCA-2020 \nName: Christeena Joy \nBatch: S3 MCA \n**************************\n")
advertising=pd.read_csv('Company_data.csv')
advertising.head()
advertising.describe()
advertising.info()

print("Feature values: ")
X=advertising.iloc[:,:-1]
print(X)
print("Target variable values: ")
y=advertising.iloc[:,-1]
print(y)
from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.3)
from sklearn.linear_model import LinearRegression
regressor=LinearRegression()
regressor.fit(X_train,y_train)
print("Intercept is: ")
print(regressor.intercept_)
print("Coefficients are: ")
print(regressor.coef_)
y_pred=regressor.predict(X_test)
for(i,j) in zip(y_test,y_pred):
    if i!=j:
        print("Actual value :",i,"Predicted value: ",j)
print("Number of mislabelled points from test data set: ",(y_test!= y_pred).sum())

from sklearn import metrics
print("Mean Absolute error: ",metrics.mean_absolute_error(y_test,y_pred))
print("Mean Squared error: ",metrics.mean_squared_error(y_test,y_pred))
print("Root Mean Squared error: ",np.sqrt(metrics.mean_squared_error(y_test,y_pred)))
