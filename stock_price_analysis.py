import numpy as np;
from pandas import DataFrame,read_csv;
import pandas as pd;
import csv;
from sklearn.svm import SVR;
import matplotlib.pyplot as plt
'''
axis_bank.csv
0:Date 1:Price 2:Open 3:High 4:Low 5:Vol 6:Change in Percentage
Total 21 values with 7 columns
df=pd.read_csv(file,dtype=str);
df=df.values;
print(df.dtype);
date=df[:,[0]].astype('str');
date=date.split('-')[0];
price=df[:,[1]].astype('float');
'''
dates = [];
prices = [];
def get_data(filename):
    with open(filename,'r') as csvfile:
        csvFileReader = csv.reader(csvfile);
        next(csvFileReader);
        for row in csvFileReader:
            dates.append(int(row[0].split('-')[0]));
            prices.append(float(row[1]));
    return;

def predict_prices(dates,prices,x):
    dates=np.reshape(dates,(len(dates),1));
    #prices=np.reshape(prices,(len(prices),1));
    #print("shape of dates = ",str(np.shape(dates)));
    svr_lin=SVR(kernel='linear',C=1e3);
    svr_poly=SVR(kernel='poly',C=1e3,degree=2);
    svr_rbf=SVR(kernel='rbf',C=1e3,gamma=0.1);

    svr_lin.fit(dates,prices);
    svr_poly.fit(dates,prices);
    svr_rbf.fit(dates,prices);

    plt.scatter(dates,prices,color='black',label='Data');

    plt.plot(dates,svr_rbf.predict(dates),color='red',label='RBF model');
    plt.plot(dates,svr_lin.predict(dates),color='green',label='Linear model');
    plt.plot(dates,svr_poly.predict(dates),color='blue',label='Polynomial model');
    plt.xlabel('Date');
    plt.ylabel('Price');
    plt.title('Support Vector Regression');
    plt.legend();
    plt.show();
    
    return svr_rbf.predict(x)[0],svr_lin.predict(x)[0],svr_poly.predict(x)[0];

file_name='axis_bank.csv';
get_data(file_name);
predicted_price = predict_prices(dates,prices,22);
print(predicted_price);
    


