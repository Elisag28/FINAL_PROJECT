import streamlit as st
import pickle
import pandas as pd

# load model
with open('../models/RandomForestClassifier_n-estimators_100_28.sav', 'rb') as file:
    model = pickle.load(file)

# mapping and lists
descent_mapping = {
    'Black': 0,
    'Hispanic/Latin/Mexican': 1,
    'White': 2,
    'Unknown': 3,
    'Other Asian': 4,
    'Other': 5,
    'Chinese': 6,
    'Filipino': 7,
    'Korean': 8,
    'American Indian/Alaskan Native': 9,
    'Vietnamese': 10,
    'Japanese': 11,
    'Cambodian': 12,
    'Asian Indian': 13,
    'Hawaiian': 14,
    'Pacific Islander': 15,
    'Guamanian': 16,
    'Samoan': 17,
    'Laotian': 18}

descent_keys_list = [
    'Black', 
    'Hispanic/Latin/Mexican', 
    'White', 
    'Unknown', 
    'Other Asian', 
    'Other', 
    'Chinese', 
    'Filipino', 
    'Korean', 
    'American Indian/Alaskan Native', 
    'Vietnamese', 
    'Japanese', 
    'Cambodian', 
    'Asian Indian', 
    'Hawaiian', 
    'Pacific Islander', 
    'Guamanian', 
    'Samoan', 
    'Laotian']

sex_mapping = {
    'Female': 0, 
    'Male': 1, 
    'X': 2}

status_mapping = {
    'AO': 'Adult Other',
    'IC': 'Invest Cont',
    'AA': 'Adult Arrest',
    'JA': 'Juv Arrest',
    'JO': 'Juv Other',
    'CC': 'UNK'
}


# front 
st.markdown('<style>h1 { color: brown; }</style>', unsafe_allow_html=True)

st.title('Predicción:')

time_occ = st.slider(
    'Hora de ocurrencia (hora militar):', 
    min_value= 1, 
    max_value=2359,
    step = 1,
    format='%04d'
    )

vict_age = st.slider(
    'Edad de la victima:', 
    min_value=..., 
    max_value=...
    )

vict_descent = st.selectbox(
    'Seleccione la etnia: de la victima:', descent_keys_list)

sex_n = st.selectbox(
    'Seleccione la etnia: de la victima:',
    ['Female', 'Male', 'X']
    )

# predict
if st.button('Realizar Predicción'):
    
    prediction = model.predict([[time_occ, vict_age, ]])

  
    st.write(f'Predicción: {prediction}')