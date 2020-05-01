#!/usr/bin/python

""" 
    This is the code to accompany the Lesson 2 (SVM) mini-project.

    Use a SVM to identify emails from the Enron corpus by their authors:    
    Sara has label 0
    Chris has label 1
"""
    
import sys
from time import time
sys.path.append("../tools/")
from email_preprocess import preprocess


### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()

from sklearn import svm 


#########################################################
### your code goes here ###
#print('shinking dataset')
#features_train = features_train[:len(features_train)/100]
#labels_train = labels_train[:len(labels_train)/100]
#print('Done!')

print('Starting SVM...')
clf = svm.SVC(kernel='rbf',C=10000, gamma='auto')
clf.fit(features_train, labels_train)
pred = clf.predict(features_test)
print('SVM Done!')

print('10th: ' + str(pred[10]))
print('26th: ' + str(pred[26]))
print('50th: ' + str(pred[50]))
print('Accuracy: ' + str(clf.score(features_test,labels_test)))
print('Number of Chris Emails: ' + str(list(pred).count(1)))
#########################################################