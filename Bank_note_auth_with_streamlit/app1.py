# -*- coding: utf-8 -*-
"""
Created on Tue Jul  6 11:22:08 2021

@author: Abhishek
"""

#import numpy as np
import pickle
#import pandas as pd
import streamlit as st 
import webbrowser
#from PIL import Image



pickle_in = open("classifier.pkl","rb")
classifier=pickle.load(pickle_in)

def welcome():
    return "Welcome All"

def predict_note_authentication(variance,skewness,curtosis,entropy):   
    prediction=classifier.predict([[variance,skewness,curtosis,entropy]])
    print(prediction)
    return prediction

url='www.linkedin.com/in/abhishek-ravindran-226909180'
url1='https://github.com/Abhishekravindran/End-To-End-Data-Science-Projects'

def main():
    st.title("Bank Authenticator")
    html_temp = """
    <div style="background-color:blue;padding:10px">
    <h2 style="color:black;text-align:center;">Streamlit Bank Authenticator ML App </h2>
    </div>
    """
    st.markdown(html_temp,unsafe_allow_html=True)
    variance = st.text_input("Variance","Type Here")
    skewness = st.text_input("skewness","Type Here")
    curtosis = st.text_input("curtosis","Type Here")
    entropy = st.text_input("entropy","Type Here")
    result=""
    if st.button("Predict"):
        result=predict_note_authentication(variance,skewness,curtosis,entropy)
    st.success('The output is {}'.format(result))
    if st.button("About"):
        if st.button("linked_in-profile"):
            webbrowser.open_new_tab(url)
        if st.button("github-profile"):
            webbrowser.open_new_tab(url1)
        st.text("Lets Learn")
        st.text("Built with Streamlit")

if __name__=='__main__':
    main()
    
    
    