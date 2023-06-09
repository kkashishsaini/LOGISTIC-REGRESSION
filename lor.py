# -*- coding: utf-8 -*-
"""LOR.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1lgHUlOOgJsSeD2Jk4jjsqn0-E06U4Ney
"""

import numpy as np 
import pandas as pd 
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
a = pd.read_csv("/content/Iris (1).csv")
print(a)
feature_columns = ['SepalLengthCm', 'SepalWidthCm', 'PetalLengthCm','PetalWidthCm']
X = a[feature_columns].values
Y = a['Species'].values

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.3)

lr = LogisticRegression(C=100.0, multi_class='ovr')
lr.fit(X_train, Y_train)

Y_predict = lr.predict(X_test)
print(metrics.accuracy_score(Y_test, Y_predict)*100)

a=a[a['Species'] != 'Iris-setosa']
print(a)
feature_columns = ['SepalLengthCm', 'SepalWidthCm', 'PetalLengthCm','PetalWidthCm']
X = a[feature_columns].values
Y = a['Species'].values

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.3)

lr = LogisticRegression(C=100.0, multi_class='ovr')
lr.fit(X_train, Y_train)

Y_predict = lr.predict(X_test)
print(metrics.accuracy_score(Y_test, Y_predict)*100)