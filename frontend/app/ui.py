import streamlit as st
import yfinance as yf
import pandas as pd
import altair as alt
import httpx

st.set_page_config(page_title="My wallet")
st.title("My wallet")

st.sidebar.image("https://cdn.pixabay.com/photo/2019/01/04/01/37/wallet-3912327_1280.jpg", width=100,
                channels='BGR', output_format='JPG')

st.sidebar.header("My wallet")


##Jewish calendar
with st.sidebar.expander("Jewish Calendar"):
    st.info(f"""
        Click [here](https://www.hebcal.com/hebcal?v=1&maj=on&min=on&nx=on&mf=on&ss=on&mod=on&o=on&i=on&year=2022&yt=G&lg=s&D=on&c=off&geo=none&zip=&city=&geonameid=&city-typeahead=&b=18&M=on&m=)
        for a Jewish calender to 2022.
        """)


##suitable siddur
df = pd.DataFrame({
    'nusach': ['mizrach', 'sfard', 'ashkenaz'],

    })

user_nusach = st.sidebar.selectbox(
            "Select a nusach", df['nusach'])
if user_nusach!=None:

    if user_nusach == 'sfard':
        st.image("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQGXWN1TK8UNiiy5tAn8_5EBhFvdqxouh1lQ-ZTPHt5_EaR_yYIBmHK5KssmnaC0F_jhEk&usqp=CAU", width=100,
                channels='BGR', output_format='JPG')
        st.write("""
        https://www.sefaria.org.il/Siddur_Sefard
        """)
    
    if user_nusach == 'mizrach':
        st.image("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTfmY2krADOUL1j5iPUePs7EMDQfdTk2O3J1w&usqp=CAU", width=100,
                    channels='BGR', output_format='JPG')
        st.write("""
        https://www.sefaria.org.il/Siddur_Edot_HaMizrach
        """)

    if user_nusach == 'ashkenaz':
        st.image("data:image/jpeg;base64,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", width=100,
                    channels='BGR', output_format='JPG')
        st.write("""
        https://www.sefaria.org.il/Siddur_Ashkenaz
        """)

##requests over httpx
backend_endpoint2="http://localhost:8888/"
r2=httpx.get(backend_endpoint2)
st.json(r2.json())

backend_endpoint = "https://httpbin.org/get"
r = httpx.get(backend_endpoint)
st.json(r.json())



