from dotenv import load_dotenv
import streamlit as st
import os
import requests
import json
load_dotenv()

token = os.environ.get('WAQI_TOKEN')

r = requests.get(f'https://api.waqi.info/feed/tbilisi/?token={token}')
st.metric('AQI', value=r.json()['data']['aqi'])
st.metric('IAQI', value=r.json()['data']['iaqi']['dew']['v'])
# st.write(r.json()['data']['iaqi'].items())
for k, val in r.json()['data']['iaqi'].items():
    # print(k, v['v'])
    st.metric(k, value=val['v'])
    # for p, i in v.items():
    #     print(p, i)
        # st.metric(label=v['v'], value=i)
    # st.metric(label=k, value=)
# st.json(r.json())
# st.write(r.json()['data']['dominentpol']['pm25'])


