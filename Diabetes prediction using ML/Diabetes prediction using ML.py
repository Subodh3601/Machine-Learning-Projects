# -*- coding: utf-8 -*-
"""Untitled2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1zyRoCWvZzqCE9CXyZnA0T2N_r6DSDZO7

# understanding the problem statement
we need to make a ML model to predict a person has diabetes or not

## Importing the libraries and dataset
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn import svm
from sklearn.metrics import accuracy_score

diabetes_df = pd.read_csv('/content/diabetes.csv')

diabetes_df.head(2)

diabetes_df.shape

diabetes_df.info()

# statistics of data
diabetes_df.describe()

diabetes_df['Outcome'].value_counts()

"""# 0--> Non-diabetic
# 1--> Diabetic
"""

diabetes_df.groupby('Outcome').mean()

# seperating data and label
X = diabetes_df.drop(columns='Outcome', axis=1)
Y = diabetes_df['Outcome']

X.head(2)

print(X.shape,Y.shape)

# data standardisaton
scaler = StandardScaler()
X = scaler.fit_transform(X)

X

# train-test split
X_train, X_test, Y_train, Y_test = train_test_split(X,Y, train_size=0.2, stratify=Y, random_state=2)

print(X.shape, X_train.shape, X_test.shape,)
print(Y.shape, Y_train.shape, Y_test.shape,)

# Training the model

classifier = svm.SVC(kernel='linear')

classifier.fit(X_train,Y_train)

"""# Model evaluation"""

# Training Accuracy score
training_prediction = classifier.predict(X_train)
training_accuracy = accuracy_score(training_prediction, Y_train)
print('Training Accuracy : ',training_accuracy )

# Testing Accuracy score
testing_prediction = classifier.predict(X_test)
testing_accuracy = accuracy_score(testing_prediction, Y_test)
print('Testing Accuracy : ',testing_accuracy )

"""# Making prediction system"""

input_data=(6,148,72,35,0,33.6,0.627,50)

# changing the data type to numpy array
input_data_asarray = np.asarray(input_data)

# reshaping the data to predict as my prediction system require data in shape (1,8)
input_data_reshaped = input_data_asarray.reshape(1,-1)

# standardize the input data
std_data = scaler.transform(input_data_reshaped)

prediction = classifier.predict(std_data)
print(prediction)

if prediction[0]==1:
  print('Person is DIABETIC')
else:
  print('Person is NOT Diabetic')

input_data=(1,85,66,29,0,26.6,0.351,31)
input_data_asarray = np.asarray(input_data)
input_data_reshaped = input_data_asarray.reshape(1,-1)
std_data = scaler.transform(input_data_reshaped)
prediction = classifier.predict(std_data)
print(prediction)

if prediction[0]==1:
  print('Person is DIABETIC')
else:
  print('Person is NOT Diabetic')

