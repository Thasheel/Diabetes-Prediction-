import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import matplotlib.pyplot as plt
import seaborn as sn
dataset=pd.read_csv("diabetes.csv")
dataset.head(10)


# Pairplot 
sns.pairplot(data = dataset, hue = 'Outcome')
plt.show()
# to show heatmap
sns.heatmap(dataset.corr(), annot = True)
plt.show()

#Logistic regression
y = dataset_new['Outcome']
X = dataset_new.drop('Outcome', axis=1)
from sklearn.model_selection import train_test_split
X_train, X_test, Y_train, Y_test = train_test_split(X, y, test_size = 0.20, random_state = 42, stratify = dataset_new['Outcome'] )
from sklearn.linear_model import LogisticRegression
model = LogisticRegression()
model.fit(X_train, Y_train)
y_predict = model.predict(X_test)
y_predict

#Example: Let's check whether the person have diabetes or not using some random values

y_predict = model.predict([[1,148,72,35,79.799,33.6,0.627,50]])
print(y_predict)
if y_predict==1:
    print("Diabetic") 
else:
    print("Non Diabetic")