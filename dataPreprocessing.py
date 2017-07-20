import numpy as np 
import matplotlib.pyplot as plt 
import pandas as pd 

from sklearn.cross_validation import train_test_split


dataset = pd.read_csv('Data.csv')

x = dataset.iloc[:,:-1].values
y = dataset.iloc[:, len(x)-1].values

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.2, random_state = 0)
