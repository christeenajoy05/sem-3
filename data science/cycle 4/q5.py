import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
print("Register No: SJC22MCA-2020 \nName: Christeena Joy \nBatch: S3 MCA \n**************************\n")
student=pd.read_csv('student_scores.csv')
print(student.head())
student.describe()
student.info()


Xax=student.iloc[:,0]
Yax=student.iloc[:,1]
plt.scatter(Xax,Yax)
plt.xlabel("No of hours")
plt.ylabel("Score")
plt.title("Student scores")
plt.show()
X=student.iloc[:,:-1]
y=student.iloc[:,1]
print('X_values')
print(X)
print('Y_values')
print(y)


X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2)
print(X_train)
from sklearn.linear_model import LinearRegression
regressor=LinearRegression()
regressor.fit(X_train,y_train)
print('INTERCEPT=',regressor.intercept_)
print("COEFFICIENT= ",regressor.coef_)
y_pred=regressor.predict(X_test)
for (i,j) in zip(y_test,y_pred):
 if( i != j):
        print("Actual value: ",i,"Predicted value: ",j)
print("Number of mislabelled points from test data set :",(y_test!=y_pred).sum())

from sklearn import metrics
print("Mean absolute error: ",metrics.mean_absolute_error(y_test,y_pred))
print("Mean squared error: ",metrics.mean_squared_error(y_test,y_pred))
import numpy as np
print("Root Mean squared error: ",np.sqrt(metrics.mean_squared_error(y_test,y_pred)))