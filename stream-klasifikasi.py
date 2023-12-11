import pickle
import streamlit as st

# Model 
dt_model = pickle.load(open('kategori_tunggu.sav', 'rb'))

#Judul
st.title("Klasifikasi Waktu tunggu Pasien")

def map_shift(SHIFT):
    if SHIFT == 'MALAM':
        return 3
    elif SHIFT == 'SORE':
        return 2
    elif SHIFT == 'PAGI':
        return 1
    else:
        return 0

def map_jenis_pasien(JenisPasien):
    if JenisPasien == 'LAMA':
        return 2
    elif JenisPasien == 'BARU':
        return 1
    else:
        return 0

def map_jenis_pemeriksaan(JenisPemeriksaan):
    if JenisPemeriksaan == 'USG':
        return 3
    elif JenisPemeriksaan == 'RONTGEN':
        return 2
    elif JenisPemeriksaan == 'CT SCAN':
        return 1
    else:
        return 0
    
def map_detil_pemeriksaan(DetilPemeriksan):
    if  DetilPemeriksan == 'BOF':
        return 18
    elif DetilPemeriksan == 'STONO':
        return 17
    elif DetilPemeriksan == 'TVS':
        return 16
    elif DetilPemeriksan == 'COCCYGEUS':
        return 15
    elif DetilPemeriksan == 'WRIST':
        return 14
    elif DetilPemeriksan == 'KEPALA':
        return 13
    elif DetilPemeriksan == 'PELVIS':
        return 12
    elif DetilPemeriksan == 'PEDIS':
        return 11
    elif DetilPemeriksan == 'CRURIS':
        return 10
    elif DetilPemeriksan == 'LS':
        return 9
    elif DetilPemeriksan == 'KANDUNGAN':
        return 8
    elif DetilPemeriksan == 'THYROID':
        return 7
    elif DetilPemeriksan == 'ELBOW':
        return 6
    elif DetilPemeriksan == 'MANUS':
        return 5
    elif DetilPemeriksan == 'KONTROL HAMIL':
        return 4
    elif DetilPemeriksan == 'GENU':
        return 3
    elif DetilPemeriksan == 'THORAX':
        return 2
    elif DetilPemeriksan == 'ABD ATAS BAWAH':
        return 1
    else:
        return 0

# User Input 
pilihan_pemeriksaan = ["USG", "RONTGEN", "CT SCAN"]
JenisPemeriksaan = st.radio("Jenis Pemeriksaan", pilihan_pemeriksaan, index=None)

pilihan_shift = ["PAGI", "SORE", "MALAM"]
SHIFT = st.radio("Pilih Shift", pilihan_shift, index=None)

pilihan_jenis_pasien = ["BARU", "LAMA"]
JenisPasien = st.radio("Jenis Pasien", pilihan_jenis_pasien, index=None)

pilihan_detilPemeriksaan = ["ABD ATAS BAWAH", 'THORAX', 'GENU', 'KONTROL HAMIL', 'THORAX', 'MANUS', 'ELBOW', 'THYROID', 'KANDUNGAN', 'LS', 'CRURIS', 'PEDIS', 'PELVIS', 'KEPALA', 'WRIST', 'COCCYGEUS', 'TVS', 'STONO', 'BOF']
DetilPemeriksaan = st.radio('Pilihan Detil Pemeriksaan', pilihan_detilPemeriksaan, index=None)

# Map categorical values to numerical values
mapped_shift = map_shift(SHIFT)
mapped_jenis_pasien = map_jenis_pasien(JenisPasien)
mapped_jenis_pemeriksaan = map_jenis_pemeriksaan(JenisPemeriksaan)
mapped_detil_pemeriksaan = map_detil_pemeriksaan(DetilPemeriksaan)

if st.button("Submit", type="primary"):
    waktuTunggu_prediction = dt_model.predict([[mapped_jenis_pemeriksaan, mapped_jenis_pasien, mapped_shift, mapped_detil_pemeriksaan]])
    
    if(waktuTunggu_prediction[0] == 2) :
        waktuTunggu = 'Waktu Tunggu Lambat'
    elif(waktuTunggu_prediction[0] == 1) :
        waktuTunggu =  "Waktu Tunggu Normal"
    else  :
        waktuTunggu =  "Waktu Tunggu Cepat"
    st.success(waktuTunggu)