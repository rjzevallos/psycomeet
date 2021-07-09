import pandas as pd
import numpy as np

from nltk import FreqDist
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords
from nltk.collocations import BigramAssocMeasures, BigramCollocationFinder
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import MinMaxScaler

from sklearn.decomposition import PCA

def get_top_5(data):
    value = []
    for i in data:
        value.append(i)
	return value

def match(user_id):
	data = pd.read_csv("data.csv")
	data = data.drop(columns='username')
	data_categorical = data.select_dtypes('object')
	data_categorical = data_categorical.drop(columns=['user_id', 'status', 'drugs', 'orientation', 'drinks', 'bio', 'location', 'location_preference', 'dropped_out', 'smokes'])
	data_encoded = pd.DataFrame()
	labelencoder = LabelEncoder()
	
	for col in data_categorical:
		data_encoded['{}'.format(col)] = labelencoder.fit_transform(data_categorical['{}'.format(col)])
	
	data_encoded = pd.concat([data['age'],data['height'],data['education_level'],data_encoded],
                        axis=1)
	
	scaler = MinMaxScaler()
	data_encoded = pd.DataFrame(scaler.fit_transform(data_encoded),
                            columns= data_encoded.columns,
                            index= data_encoded.index)
	
	data_final = data_encoded
	pca = PCA()
	data_pca = pca.fit_transform(data_final)
	total_variance = pca.explained_variance_ratio_.cumsum()
	n_for_95 = len(total_variance[total_variance>=.95])
	n_to_reach_95 = data_final.shape[0] - n_for_95
	
	data_corr = data_final.T.corr()
	data_corr = pd.DataFrame(scaler.fit_transform(data_corr),
                            columns= data_corr.columns,
                            index= data_corr.index)
	
	corr_arr = np.array(data_corr)
	final_mat = pd.DataFrame(corr_arr, columns=data['user_id'].tolist(), index=data['user_id'].tolist())
	final_mat = final_mat.mul(100)
	
	final_mat.index.name = 'user_id'
	final_mat.columns.name = 'user_id'
	
	return got_top_5(final_mat[user_id])
	
	
match("fffe3100")