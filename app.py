import pandas as pd

from sklearn.svm import SVC
from sklearn.model_selection import train_test_split

import pickle
import streamlit as st

nama_file = 'registrasi.xlsx'
dataset = pd.read_excel(nama_file)
print(dataset)

# Mengubah data menjad bentuk numerik
dataset['SHIFT'].replace({'':0, 'PAGI':1, 'SORE':2, 'MALAM':3}, inplace=True)
dataset['Jenis Pasien'].replace({'':0, 'BARU':1, 'LAMA':2}, inplace=True)
dataset['Jenis Pemeriksaan'].replace({'':0, 'USG':1, 'RONTGEN':2, 'CT SCAN':3}, inplace=True)
dataset['Detil Pemeriksaan'].replace({'':0, 'ABD ATAS BAWAH':1, 'THORAX':2, 'GENU':3, 'KONTROL HAMIL':4, 'THORAX':5, 'MANUS':6, 'ELBOW':7, 'THYROID':8, 'KANDUNGAN':9, 'LS':10, 'CRURIS':11, 'PEDIS':12, 'PELVIS':13, 'KEPALA':14, 'WRIST':15, 'COCCYGEUS':16, 'TVS':17, 'STONO':18, 'BOF':19}, inplace=True)
dataset['Jenis Pembayaran'].replace({'':0, 'IKS':1, 'UMUM':2, 'KES':3}, inplace=True)

# Create a Pandas Series with interval data.
series = pd.Series(dataset['Waktu Tunggu '])

# Convert the interval data to ordinal data using the pd.cut() function with 3 bins.
ordinal_data = pd.cut(series, bins=[3, 21, 33, 59], labels=[0, 1, 2])
# Print the ordinal data.
print(ordinal_data)

dataset = dataset.assign(Range_Waktu_tunggu=ordinal_data)
print(dataset)

X= dataset[['Jenis Pemeriksaan', 'SHIFT', 'Jenis Pasien', 'Detil Pemeriksaan']]
y = dataset['Range_Waktu_tunggu']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

svm_model = SVC(random_state=0)
svm_model.fit(X_train, y_train)

filename = 'kategori_tunggu.sav'
y_prediction_svm = svm_model.predict(X_test)

pickle.dump(svm_model, open(filename, 'wb'))