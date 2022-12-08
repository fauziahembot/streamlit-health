import pickle
import numpy as np
import streamlit as st

model = pickle.load(open('maternal-health.sav', 'rb'))

st.title('Prediksi Kesehatan Ibu Ketika Sedang Mengandung (Hamil)')

col1, col2 = st.columns(2)

with col1:
    Age = st.number_input('Umur')

with col2:
    SystolicBP = st.number_input('Nilai Tekanan Darah Yang Lebih Tinggi Dalam mmHg') 

with col1:
    DiastolicBP = st.number_input('Nilai Tekanan Darah Yang Lebih Rendah Dalam mmHg')

with col2:
    BS = st.number_input('Nilai Kadar Glukosa Dalam Darah Dalam mmol/L')

with col1:
    BodyTemp = st.number_input('Nilai Temperatur Badan')

with col2:
    HeartRate = st.number_input('Nilai Detak Jantung Dalam Keadaan Normal')

maternal_diagnosis = ''

if st.button('Prediksi Kesehatan Ibu'):
    maternal_prediction = model.predict([[Age, SystolicBP,  DiastolicBP, BS, BodyTemp, HeartRate]])

    if(maternal_prediction[0]==0):
        maternal_diagnosis = 'Tingkat Resiko Rendah'
    elif(maternal_prediction[0]==1):
        maternal_diagnosis = 'Tingkat Resiko Sedang'
    else:
        maternal_diagnosis = 'Tingkat Resiko Tinggi'

st.success(maternal_diagnosis)
