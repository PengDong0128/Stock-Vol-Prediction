
# coding: utf-8

# # Stock Volatility Prediction (Models)
# ### in this project , I will predict stock volatility by using 
# ### GARCH model
# ### Linear model
# ### non-linear model

# In[10]:

import pandas as pd
import numpy as np
from arch import arch_model 
from sklearn.metrics import r2_score
from stock_data_reader import StockDataReader
from keras.models import Sequential
from keras.layers import Dense,LSTM
from keras.losses import mean_squared_error
from sklearn.ensemble import RandomForestRegressor
reader = StockDataReader('7az7vgtTPxiyj2Ncsc-H')


# ## Construct dataset
# ### Construct dataset for models

# In[3]:

# Create a dataframe for a simple linear regression, this part is only for the spark sample
# yesterday's vol, yesterday's return
def linear_data(ticker,window,thresh_date,export=False):
    reader.initialize_data(ticker,'2005-01-01','2016-12-31')
    dat = reader.price_table
    dat = (dat.set_index(dat['date'])).drop(['date','adj_volume'],axis=1)
    dat['return'] = (np.log(dat['adj_close'])-np.log((dat['adj_close']).shift(1)))*100

    sigma_column_name = str(window)+'dayvar'
    dat[sigma_column_name]= dat['return'].rolling(window,center=False).var()
    if export==True:
        return dat
    dat_yesterday = dat[['return',sigma_column_name]].shift(1)
    dat_yesterday_column_name = [x+'_yesterday' for x in list(dat_yesterday.columns)]
    dat_yesterday.columns = dat_yesterday_column_name
    data_linear = (pd.concat([dat,dat_yesterday],
                            axis=1)).drop(['adj_close','return'],axis=1)
    return data_linear[thresh_date:]


# In[4]:

# Create dataset for other high-dimension models
def get_data(ticker,time_window,sigma_window,thresh_date):
    dat=linear_data(ticker,sigma_window,'Null',True)
    sigma_column_name = str(sigma_window)+'dayvar'
    dat_shift = dat[['return',sigma_column_name]]
    columns = list(dat_shift.columns)
    dat_copy = dat.copy()
    for day in range(1,time_window+1):
        dat_tmp = dat_shift.shift(day)
        dat_tmp.columns = [name+'_'+str(day)+'daybefore' for name in columns]
        dat_copy = pd.concat([dat_copy,dat_tmp],axis=1)
    data_rnn = (dat_copy.drop(['adj_close','return'],axis=1))[thresh_date:]
    return data_rnn


# In[5]:

class data_split(object):
    """this class is for train-validation-testing split"""
    def __init__(self):
        print('return form: y_train,x_train,(y_vali,x_vail),y_test,x_test')
        pass
    def train_test_split(self,dat,split_date):
        """I didn't put a validation set here because:
        1: there is no need to tune hyper parameter
        2: dataset is small ,I want to use more data
        """
        train = dat[:split_date]
        test  = dat[split_date:]
        return train.iloc[:,0],train.iloc[:,1:],test.iloc[:,0],test.iloc[:,1:]
    def train_validate_test_split(self,dat,split1,split2):
        train = dat[:split1]
        validate = dat[split1:split2]
        test = dat[split2:]
        return train.iloc[:,0],train.iloc[:,1:],validate.iloc[:,0],validate.iloc[:,1:],test.iloc[:,0],test.iloc[:,1:]


# In[6]:

split = data_split()


# ### GARCH(1,1) model

# In[7]:

def garch(ticker,p_=1,q_=1):
    reader.initialize_data('AAPL','2006-01-01','2016-12-31')
    price_dat = reader.price_table
    ret = (np.log(price_dat['adj_close'])-np.log((price_dat['adj_close']).shift(1)))*100
    price_dat['returns']=ret
    price_dat = (price_dat.set_index(price_dat['date']))['returns']
    train_garch = price_dat['2009-01-01':'2016-01-01']
    am = arch_model(train_garch, vol='Garch', p=p_, o=0, q=q_, dist='Normal')
    res = am.fit(update_freq=5)
    w = res.params['omega']
    a = res.params['alpha[1]']
    b = res.params['beta[1]']
    dat_test=linear_data(ticker,21,'2006-01-01','2016-12-31')
    for i in range(1,501):# here i created 500 paths for random walks, for every path I calculated the predicted var, then take average of them
        dat_test['predict_var_%d'%(i)]=(a*((np.random.randn(len(dat_test)))**2)+b)*dat_test['21dayvar_yesterday']
    predict = (dat_test.iloc[:,3:]).mean(axis=1)
    r2 = r2_score(dat_test['21dayvar'],predict)
    return r2


# ### Random Forest

# In[8]:

def rf(ticker,window_=10):
    from sklearn.ensemble import RandomForestRegressor
    rf = RandomForestRegressor(max_depth=5)
    dat_rf = get_data(ticker,window_,21,'2009-01-01')
    y_train,x_train,y_test,x_test = split.train_test_split(dat_rf,'2016-01-01')
    rf.fit(x_train,y_train)
    r2 = rf.score(x_test,y_test)
    return r2


# ### Run RNN

# In[48]:

def rnn(ticker,window_=10):
    dat_rf = get_data(ticker,window_,21,'2009-01-01')
    y_train,x_train,y_test,x_test = split.train_test_split(dat_rf,'2016-01-01')
    xtr = np.array(x_train)
    ytr = np.array(y_train)
    xte = np.array(x_test)
    yte = np.array(y_test)
    xtr_shape = xtr.shape
    xte_shape = xte.shape
    xtr = xtr.reshape(xtr_shape[0],window_,2)
    xte = xte.reshape(xte_shape[0],window_,2)
    from keras.models import Sequential
    from keras.layers import Dense,LSTM
    from keras.losses import mean_squared_error
    lstm = Sequential()
    lstm.add(LSTM(32,input_shape = (window_,2)))
    lstm.add(Dense(32,activation = 'relu'))
    lstm.add(Dense(16,activation = 'relu'))
    lstm.add(Dense(1,activation='relu'))
    lstm.compile(loss = mean_squared_error,optimizer='adam')
    lstm.fit(xtr,ytr,batch_size=15,epochs=10)
    lstm_result = lstm.predict(xte,batch_size=1).reshape(yte.shape[0],)
    r2_lstm = r2_score(yte,lstm_result)
    return r2_lstm

