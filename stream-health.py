import pickle
import numpy as np
import streamlit as st

model = pickle.load(open('maternal-health.sav', 'rb'))

st.title('Prediksi Kesehatan Ibu Ketika Sedang Mengandung (Hamil)')

col1, col2 = st.columns(2)

with col1:
    Age = st.text_input('Masukan Umur')

with col2:
    SystolicBP = st.text_input('Masukan Nilai Tekanan Darah Yang Lebih Tinggi Dalam mmHg') 

with col1:
    DiastolicBP = st.text_input('Masukan Nilai Tekanan Darah Yang Lebih Rendah Dalam mmHg')

with col2:
    BS = st.number_input('Masukan Nilai Kadar Glukosa Dalam Darah Dalam mmol/L')

with col1:
    BodyTemp = st.text_input('Masukan Nilai Temperatur Badan')

with col2:
    HeartRate = st.text_input('Masukan Nilai Detak Jantung Dalam Keadaan Normal')

health_diagnosis = ''

if st.button('Prediksi Kesehatan Ibu'):
    health_prediction = model.predict([[Age, SystolicBP,  DiastolicBP, BS, BodyTemp, HeartRate]])

    if(health_prediction[0]==0):
        health_diagnosis = 'Tingkat Resiko Rendah'
    elif(health_prediction[0]==1):
        health_diagnosis = 'Tingkat Resiko Sedang'
    else:
        health_diagnosis = 'Tingkat Resiko Tinggi'

st.success(health_diagnosis)