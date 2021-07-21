import pandas as pd
import numpy as np

from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import MinMaxScaler
import os


def match(user_id,sex,job,pets,interests,other_interests):
    data = pd.read_csv(os.path.join(os.getcwd(),"data.csv"))
    data = data.drop(columns=['username',
                     'status',
                     'drugs',
                     'orientation',
                     'drinks',
                     'bio',
                     'body_profile',
                     'language',
                     'location',
                     'location_preference',
                     'dropped_out',
                     'new_languages',
                     'smokes',
                     'age',
                     'height',
                     'education_level'])
    row = {"user_id":user_id,"sex":sex,"job":job,
           "pets":pets,"interests":interests,
           "other_interests": other_interests}
    data = data.append(row,ignore_index=True)
    data_categorical = data.select_dtypes('object')
    data_categorical = data_categorical.drop(columns=['user_id'])
    data_encoded = pd.DataFrame()
    labelencoder = LabelEncoder()
    for col in data_categorical:
        data_encoded['{}'.format(col)] = labelencoder.fit_transform(data_categorical['{}'.format(col)])
    '''
    data_encoded = pd.concat([data['age'],
                              data['height'],
                              data['education_level'],
                              data_encoded], axis=1)
    '''
    scaler = MinMaxScaler()
    data_encoded = pd.DataFrame(scaler.fit_transform(data_encoded),
                                columns= data_encoded.columns,
                                index= data_encoded.index)
    data_final = data_encoded
    data_corr = data_final.T.corr()
    data_corr = pd.DataFrame(scaler.fit_transform(data_corr),
                             columns= data_corr.columns,
                             index= data_corr.index)
    corr_arr = np.array(data_corr)
    final_mat = pd.DataFrame(corr_arr, columns=data['user_id'].tolist(), index=data['user_id'].tolist())
    final_mat = final_mat.mul(100)
    final_mat.index.name = 'user_id'
    final_mat.columns.name = 'user_id'
    value = []
    for index, row in final_mat.iterrows():
        value.append((row[user_id],index))
    value.sort(reverse=True)
    return value[1:6]
	
#match("fffe9999999999999999999","m","medical","dogs","music","read")