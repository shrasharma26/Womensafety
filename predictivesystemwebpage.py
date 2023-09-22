# -*- coding: utf-8 -*-
"""
Created on Fri Sep 22 11:32:09 2023

@author: Shraddha Sharma
"""

import numpy as np
import pickle
import streamlit as st
loaded_model=pickle.load(open("C:/Users/Shraddha Sharma/Downloads/trained_model.sav",'rb'))

def dia_prediction(input_data):

    input_data_as_numpy_array = np.asarray(input_data)


    input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)


    prediction =loaded_model.predict(input_data_reshaped)
    print(prediction)

    if (prediction[0] == 0):
      return 'YOU ARE IN SAFE ZONE'
    else:
      return 'YOU ARE NOT IN SAFE ZONE'
  
    
def main():
    st.title('PREDICTION  WEB  PAGE')
    Pregnancies=st.text_input('Enter Gate No')
    Glucose=st.text_input('Enter Zone')
    BloodPressure = st.text_input('Approx No of peoples')
    SkinThickness=st.text_input('Approx No of peoples optional')
    Insulin=st.text_input('Enter the approx distance in meters')
    BMI=st.text_input('Body Mass Index')
    DiabetesPedigreeFunction=st.text_input(' DiabetesPedigreeFunction value')
    Age=st.text_input('Age')
    
    dia=''
    if st.button('Test Result'):
        dia=dia_prediction([Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age])
        
    st.success(dia)
    
    
if __name__ == '__main__':
    main()
    