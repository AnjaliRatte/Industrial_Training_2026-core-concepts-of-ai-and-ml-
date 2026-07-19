import pandas as pd
from sklearn.metrics import accuracy_score

data = pd.read_csv("https://raw.githubusercontent.com/npradaschnor/Pima-Indians-Diabetes-Dataset/refs/heads/master/diabetes.csv")

# print(data.head())
# print(data.tail())
print(data.shape)
print(data.columns)
# print(data.dtypes)
# print(data.describe())

# print(data.isnull().sum())
# print(data.duplicated().sum())
# columns = ["Glucose", "BloodPressure", "SkinThickness", "Insulin", "BMI"]
#
# for col in columns:
#     print(col, (data[col] == 0).sum())
#
# for col in columns:
#     med = data[col].median()
#     data[col]=data[col].replace(0,med)
# print(data)
# for col in columns:
#     print(col, (data[col] == 0).sum())

# splitting dataset

import numpy as np

x = data.drop("Outcome",axis=1)
y = data["Outcome"]
indices = np.random.permutation(len(data))
x = x.iloc[indices]
y = y.iloc[indices]
split_index = int(len(data)*0.80)
x_train = x.iloc[:split_index]
y_train = y.iloc[:split_index]

x_test = x.iloc[split_index:]
y_test = y.iloc[split_index:]

# print(x_train.shape,y_train.shape)
# print(x_test.shape,y_test.shape)
#
# print(x_train.head(),y_train.head())
# print(x_test.head(),y_test.head())