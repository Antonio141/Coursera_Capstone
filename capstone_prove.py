import pandas as pd
import numpy as np
from sklearn import svm
from sklearn import metrics
from sklearn.model_selection import train_test_split

X = pd.read_csv('D:/personale/MACHINELEARNING/IBM/capstone/X.csv')

y = X['SEVERITYCODE']

X.drop('SEVERITYCODE', axis= 1, inplace= True)

X_train, X_test, y_train, y_test = train_test_split( X, y, test_size=0.2, random_state=4)

X_train= X_train.to_numpy()
X_test= X_test.to_numpy()
y_train= y_train.to_numpy()
y_test= y_test.to_numpy()

clf = svm.SVC(kernel='rbf')
clf.fit(X_train, y_train) 

yhat = clf.predict(X_test)

accuracy = metrics.accuracy_score(y_test, yhat)

print('SVM accuracy: ', accuracy)