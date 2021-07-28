import streamlit as st
import pandas as pd
from datetime import timedelta
import s3fs


fs = s3fs.S3FileSystem(anon=False, key=st.secrets["key"], secret=st.secrets["secret"])

st.title('全台灣太陽能發電量預報（修正後）')

password = st.text_input("Enter a password", type="password")

    

data = pd.read_csv("s3://taipower-green-energy-data/aggregations/calibrated-aggregation.csv").iloc[:48*6].set_index('PeriodEnd')
data.index = pd.to_datetime(data.index) + timedelta(hours = 8)

# plot

if password == 'wr-taipower-temp-dashboard':
    st.line_chart(data)
else:
    st.write('密碼錯誤！')
