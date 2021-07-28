import streamlit as st
import pandas as pd
from datetime import timedelta
import s3fs
from time import sleep

st.title('全台灣太陽能發電量預報（修正後）')

password = st.text_input("Enter a password", type="password")

data = pd.read_csv(st.secrets['url'])
data.PeriodEnd = pd.to_datetime(data.PeriodEnd) + timedelta(hours = 16)

# plot

st.title('未來168小時')

if password == st.secrets['password']:
    st.line_chart(data.set_index('PeriodEnd'))
else:
    st.write('密碼錯誤！')
    
st.title('未來48小時')

if password == 'wr-taipower-temp-dashboard':
    st.line_chart(data.iloc[:48*6].set_index('PeriodEnd'))
else:
    st.write('密碼錯誤！')
    