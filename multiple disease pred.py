# -*- coding: utf-8 -*-
"""
Created on Tue Aug  5 17:24:20 2025
@author: 91701
"""

import pickle
import streamlit as st
from streamlit_option_menu import option_menu

# Loading the saved models
diabetes_model = pickle.load(open('diabetes_trained_model.sav', 'rb'))
heart_model = pickle.load(open('heart_diease_model.sav', 'rb'))

# Sidebar navigation
with st.sidebar:
    selected = option_menu('Multiple Disease Prediction System',
                           ['Diabetes Prediction', 'Heart Disease Prediction'],
                           icons=['activity', 'heart'],
                           default_index=0)

# Diabetes prediction page
if selected == 'Diabetes Prediction':
    st.title('Diabetes Prediction using ML')

    # Input fields
    col1, col2, col3 = st.columns(3)

    with col1:
        Pregnancies = st.text_input('Number of Pregnancies')
    with col2:
        Glucose = st.text_input('Glucose level')
    with col3:
        BloodPressure = st.text_input('Blood Pressure value')
    with col1:
        SkinThickness = st.text_input('Skin Thickness value')
    with col2:
        Insulin = st.text_input('Insulin Levels value')
    with col3:
        BMI = st.text_input('Body Mass Index')
    with col1:
        DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function')
    with col2:
        Age = st.text_input('Age')

    diab_diagnosis = ''

    if st.button('Diabetes Test Result'):
        try:
            input_data = [[float(Pregnancies), float(Glucose), float(BloodPressure),
                           float(SkinThickness), float(Insulin), float(BMI),
                           float(DiabetesPedigreeFunction), float(Age)]]

            diab_prediction = diabetes_model.predict(input_data)

            if diab_prediction[0] == 1:
                diab_diagnosis = 'The person is Diabetic'
            else:
                diab_diagnosis = 'The person is not Diabetic'
            st.success(diab_diagnosis)
        except:
            st.error("Please enter valid numeric values for all fields.")

# Heart disease prediction page
if selected == 'Heart Disease Prediction':
    st.title('Heart Disease Prediction using ML')

    col1, col2, col3 = st.columns(3)

    with col1:
        age = st.text_input('Age of person')
    with col2:
        sex = st.text_input('Gender of person (0 = female, 1 = male)')
    with col3:
        cp = st.text_input('Chest Pain type (0-3)')
    with col1:
        trestbps = st.text_input('Resting blood pressure')
    with col2:
        chol = st.text_input('Serum cholesterol in mg/dl')
    with col3:
        fbs = st.text_input('Fasting blood sugar > 120 mg/dl (1 = true; 0 = false)')
    with col1:
        restecg = st.text_input('Resting electrocardiographic results (0-2)')
    with col2:
        thalach = st.text_input('Maximum heart rate achieved')
    with col3:
        exang = st.text_input('Exercise induced angina (1 = yes; 0 = no)')
    with col1:
        oldpeak = st.text_input('ST depression induced by exercise')
    with col2:
        slope = st.text_input('Slope of the peak exercise ST segment')
    with col3:
        ca = st.text_input('Number of major vessels (0-3) colored by fluoroscopy')
    with col1:
        thal = st.text_input('Thal (1 = normal; 2 = fixed defect; 3 = reversible defect)')

    heart_diagnosis = ''

    if st.button('Heart Disease Test Result'):
        try:
            input_data = [[float(age), float(sex), float(cp), float(trestbps), float(chol),
                           float(fbs), float(restecg), float(thalach), float(exang),
                           float(oldpeak), float(slope), float(ca), float(thal)]]

            heart_prediction = heart_model.predict(input_data)

            if heart_prediction[0] == 1:
                heart_diagnosis = 'The person does NOT have heart disease'
            else:
                heart_diagnosis = 'The person has heart disease'
            st.success(heart_diagnosis)
        except:
            st.error("Please enter valid numeric values for all fields.")

