import streamlit as st
import joblib

#loading the model
model_nb = joblib.load('major-project 1')

st.title('MAJOR-PROJECT 1 CLASSIFIER')
ip = st.text_input('Enter your text :')
op = model_nb.predict([ip])
if st.button('PREDICT'):
st.title(op[0])
