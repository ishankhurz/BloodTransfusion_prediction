# -*- coding: utf-8 -*-
"""
Created on Wed Jul 05 20:53:35 2017

@author: admin
"""

import pandas as pd
#import numpy as np
#from sklearn.svm import SVC
from sklearn import tree
#from sklearn.decomposition import PCA

training = pd.read_csv('C:/Users/admin/Documents/train_bt.csv')
#training.ix[:,1]=10*training.ix[:,1]
training["Monthly Frequency"] = training["Number of Donations"]/training["Months since First Donation" ]
cols = [ "Months since Last Donation", "Number of Donations", "Months since First Donation","Monthly Frequency"]
x = training[cols]
y = training["Made Donation in March 2007"]
#clf = SVC(kernel='rbf',C=1.0,shrinking=True)
#clf.fit(x,y)
#pca = PCA().fit(x)
#print(pca.explained_variance_ratio_)
clf = tree.DecisionTreeClassifier().fit(x,y)
b = clf.score(x,y)
print ("Accuracy of the classifier is: %f" %a)