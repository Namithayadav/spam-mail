# -*- coding: utf-8 -*-
"""
Created on Wed Feb  1 00:11:04 2023

@author: 
"""
import streamlit as st
import pickle
import database as db

model = pickle.load(open('model.sav','rb'))

st.title("Spam Mail Classifier ")

t = st.text_area("Enter the message")
input_msg=[t]
if st.button('Predict'):
    if len(t)==0:
        st.warning("Please enter text")
    else:
        result = model.predict(input_msg)
        if result[0] ==1 :
            st.success("This is a Spam message :loudspeaker:")
            db.insert_data(t,"Spam message")
        else:
            st.success("This is Not a Spam message")
            db.insert_data(t,"Not a Spam message")
link='For dataset check out [link](https://drive.google.com/file/d/1wNxeZqZVmsFMyCHTmqBEwz0iJr3gEHOc/view?usp=drivesdk)'
st.markdown(link,unsafe_allow_html=True)
