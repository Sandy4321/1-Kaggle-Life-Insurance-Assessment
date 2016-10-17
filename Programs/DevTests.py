"""
Kaggle
Prudential Life Insurance project
File Used for various development tests
by Yannick SCHINI
"""

#import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
#from sklearn import svm

train_data = pd.read_csv('train.csv')
train_data.set_index('Id', inplace=True)
for i in range(1, 48):
    name = 'Medical_Keyword_' + str(i)
    del train_data[name]
y = train_data['Response']
del train_data['Response']
#print train_data.head()
#print y.head()

#plt.plot(train_data['Product_Info_1'])
#plt.show()

print list(set(train_data['Product_Info_2']))

"""
# Get list of categorical inputs (to split them into binary columns)
categorical_data_list = []
categorical_data = "Product_Info_1, Product_Info_2, Product_Info_3, Product_Info_5, Product_Info_6, Product_Info_7, Employment_Info_2, Employment_Info_3, Employment_Info_5, InsuredInfo_1, InsuredInfo_2, InsuredInfo_3, InsuredInfo_4, InsuredInfo_5, InsuredInfo_6, InsuredInfo_7, Insurance_History_1, Insurance_History_2, Insurance_History_3, Insurance_History_4, Insurance_History_7, Insurance_History_8, Insurance_History_9, Family_Hist_1, Medical_History_2, Medical_History_3, Medical_History_4, Medical_History_5, Medical_History_6, Medical_History_7, Medical_History_8, Medical_History_9, Medical_History_11, Medical_History_12, Medical_History_13, Medical_History_14, Medical_History_16, Medical_History_17, Medical_History_18, Medical_History_19, Medical_History_20, Medical_History_21, Medical_History_22, Medical_History_23, Medical_History_25, Medical_History_26, Medical_History_27, Medical_History_28, Medical_History_29, Medical_History_30, Medical_History_31, Medical_History_33, Medical_History_34, Medical_History_35, Medical_History_36, Medical_History_37, Medical_History_38, Medical_History_39, Medical_History_40, Medical_History_41"
for category in categorical_data.split():
    category = category.replace(',','')
    categorical_data_list.append(category)
#print categorical_data_list

# Get list of continuous inputs (to be bagged and split into binary columns)
continuous_data_list = []
continuous_data = "Product_Info_4, Ins_Age, Ht, Wt, BMI, Employment_Info_1, Employment_Info_4, Employment_Info_6, Insurance_History_5, Family_Hist_2, Family_Hist_3, Family_Hist_4, Family_Hist_5"
for category in continuous_data.split():
    category = category.replace(',','')
    continuous_data_list.append(category)
#print continuous_data_list

# Get list of discrete inputs (to be bagged and split into binary columns)
discrete_data_list = []
discrete_data = "Medical_History_1, Medical_History_10, Medical_History_15, Medical_History_24, Medical_History_32"
for category in discrete_data.split():
    category = category.replace(',','')
    discrete_data_list.append(category)
#print discrete_data_list
"""
