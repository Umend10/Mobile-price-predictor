import streamlit as st
import pandas as pd
import numpy as np
import pickle
import sklearn



pipe=pickle.load(open('pipemgb.pkl','rb'))
st.header('Mobile Price Predictor')

# select brand
brand_list=['Apple', 'Honor', 'Huawei', 'IQOO', 'Motorola', 'Nokia', 'OnePlus',
       'Oppo', 'Other', 'Poco', 'Realme', 'Samsung', 'Tecno', 'Vivo',
       'Xiaomi', 'ZTE']
brand=st.selectbox('Select Brand',brand_list)

#select OS
if brand=='Apple':
    OS=st.selectbox('Select OS',['iOS'])
else :
    OS=st.selectbox('Select OS',['iOS','Android'])

#select Rear Camera

rear_camera_list=['Dual', 'Quad', 'Single', 'Triple']
camera=st.selectbox("Select Rear Camera",rear_camera_list)

# ram and storage
col1,col2=st.columns(2)
with col1:
    # select Ram:
    ram_list=[ 1,  2,  3,  4,  6,  8, 12]
    ram=st.selectbox('Select Ram',ram_list)

with col2:
    #select storage
    storage_list=[ 16,  32,  64, 128, 256, 512]
    storage=st.selectbox('Select Storage',storage_list)

#processor and core
col1,col2=st.columns(2)
with col1:
    #processor 
    processor_list=['A Bionic', 'Dimensity', 'Helio', 'Other', 'Snapdragon']
    processor=st.selectbox('Select Processor Type',processor_list)

with col2:
    #core
    core_list=['Hexa Core', 'Octa Core', 'Quad Core']
    core=st.selectbox('Select Core',core_list)


# 5G and battery
col1,col2=st.columns(2)
with col1:
    g_list=['Yes','No']
    g=st.selectbox('Select 5G or not',g_list)
with col2:
    battery_list=['below 2800','2800 - 4500', 'above 4500']
    battery=st.selectbox('Select Battery type',battery_list)

dic={
    'company':[brand],
    'OS':[OS],
    'processor':[processor],
    'core':[core],
    '5G':[g],
    'rear_camera':[camera],
    'ram':[ram],
    'Storage':[storage],
    'battery':[battery]
}

data=pd.DataFrame(dic)

result=round(np.exp(pipe.predict(data)[0]))


#for button
button=st.button('Click')
if button:
    st.header('approx '+str(result))

    #for continious range
    if result<=15000:
        st.text(f'Note:- price may lie between {result-1000} to {result+1000}')
    elif result<25000:
        st.text(f'Note:- price may lie between {result-2000} to {result+2000}')
    elif result<50000:
        st.text(f'Note:- price may lie between {result-4000} to {result+4000}')
    else:
        st.text(f'Note:- price may lie between {result-4000} to {result+4000}')