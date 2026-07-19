import pandas as pd
from sklearn.metrics import accuracy_score

data = pd.read_csv("https://raw.githubusercontent.com/npradaschnor/Pima-Indians-Diabetes-Dataset/refs/heads/master/diabetes.csv")

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

from sklearn.svm import SVC
from sklearn.linear_model import LogisticRegression,SGDClassifier
from sklearn.metrics import accuracy_score
from sklearn.naive_bayes import GaussianNB
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn import svm

# logistic classification
lr = LogisticRegression(max_iter=1000)
lr.fit(x_train,y_train)
predict = lr.predict(x_test)
print("logistic regression : ",accuracy_score(y_test,predict))

# support vector classification
clf = SVC(max_iter=1000)
clf.fit(x_train, y_train)
prediction = clf.predict(x_test)
print("svc : ",accuracy_score(y_test,prediction))

# Stochastic gradient descent classifier
gc = SGDClassifier(max_iter=1000)
gc.fit(x_train,y_train)
prediction = gc.predict(x_test)
print("SGDC : ",accuracy_score(y_test,prediction))

# naive bayes classifier
nb = GaussianNB()
nb.fit(x_train,y_train)
prediction = nb.predict(x_test)
print("naive bayes : ",accuracy_score(y_test,prediction))

# knn
knn = KNeighborsClassifier()
knn.fit(x_train,y_train)
prediction=knn.predict(x_test)
print("knn : ",accuracy_score(y_test,prediction))

# decision tree classifier
dt = DecisionTreeClassifier()
dt.fit(x_train,y_train)
prediction=dt.predict(x_test)
print("decision tree : ",accuracy_score(y_test,prediction))

# random forest
rf = RandomForestClassifier()
rf.fit(x_train,y_train)
prediction=rf.predict(x_test)
print("random forest : ",accuracy_score(y_test,prediction))

# svm
svm = svm.SVC()
svm.fit(x_train,y_train)
prediction=svm.predict(x_test)
print("svm : ",accuracy_score(y_test,prediction))




