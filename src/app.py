import streamlit as st
import pickle
import pandas as pd

# load model
with open('../models/RandomForestClassifier_n-estimators_100_28.sav', 'rb') as file:
    model = pickle.load(file)

# mapping


st.title('Predicción:')

feature1 = st.slider('Feature 1', min_value=..., max_value=...)
feature2 = st.slider('Feature 2', min_value=..., max_value=...)


# Realiza la predicción con el modelo
if st.button('Realizar Predicción'):
    
    prediction = model.predict([[feature1, feature2, ...]])

  
    st.write(f'Predicción: {prediction}')