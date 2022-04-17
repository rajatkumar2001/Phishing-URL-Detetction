import streamlit as st
import pickle
import numpy as np
model=pickle.load(open('phishing.pkl','rb'))


st.title("Phishing site prediction")

inp=st.text_input('Enter the link')

if st.button('Predict phishing site'):
    result=model.predict([inp])
    if result=='good':
        st.title("This is NOT a Phishing site")
    else:
        st.title("This is a Phishing site")
