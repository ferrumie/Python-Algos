import pandas as pd
import numpy as np

import pickle as cPickle 

import scorecardpy as sc 



seed = 2432743
import os
os.environ['PYTHONHASHSEED'] = str(seed)

# modelData = pd.read_csv('modelData_train.csv')
print("********************")

# loanDetails = modelData[~modelData.index.isin([2,4,3,27,43])]

data_test = pd.read_csv('test_data.csv')
print(data_test.shape)



mlp = cPickle.load(open('model.pkl', 'rb'))
bins = cPickle.load(open("bins.pkl", "rb" ))



data_test_bined = sc.woebin_ply(data_test, bins) 
print(data_test_bined.to_dict())


# cols_when_model_builds = mlp.feature_names_in_
# print(cols_when_model_builds)
# data_test_bined = data_test_bined[cols_when_model_builds]


X = data_test_bined.loc[:,data_test_bined.columns != 'aatarget_class']


pred_prob = mlp.predict_proba(X)[:,1]
print(pred_prob)



