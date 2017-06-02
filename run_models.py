
# coding: utf-8

# In[1]:

from models import *
from sklearn.ensemble import RandomForestRegressor
from keras.models import Sequential
from keras.layers import Dense, LSTM
from keras.losses import mean_squared_error


# In[2]:

with open('sp500_list.txt','r') as f:
    splist = f.read().splitlines()


# In[ ]:

lis_success=[]
lis_fail=[]
result_df = pd.DataFrame({'garch':[],
                          'random forest':[],
                          'RNN':[]})

for ticker in splist:
    try:
        rnn_count=0
        r2_garch = garch(ticker)
        r2_rf = rf(ticker)
        r2_rnn = rnn(ticker)
        while((r2_rnn<0) and rnn_count<3):
            r2_rnn = rnn(ticker)
        result_df = result_df.append({'garch':r2_garch,'random forest':r2_rf,'RNN':r2_rnn},ignore_index=True)
        lis_success.append(ticker)
    except:
        lis_fail.append(ticker)

success = pd.DataFrame({'success':lis_success})
fail  = pd.DataFrame({'fail':lis_fail})
success.to_csv('sucess_list.csv')
fail.to_csv('fail_list.csv')
result_df.to_csv('result.csv')
