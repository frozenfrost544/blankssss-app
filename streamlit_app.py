import streamlit as st

# Title of the application
st.title("SELAMAT DATANG DI PELAYANAN DESTINASI WISATA KOTA PALU")

# Instructions with a clickable link
st.write(
    "Silahkan klik link berwarna biru untuk melanjutkan: [Dokumentasi Streamlit](https://docs.streamlit.io/)."
)

# Set background image URL
background_image_url = "https://asset-2.tstatic.net/palu/foto/bank/images/Bundaran-Nol-KM-Kota-Palu.jpg"

# Custom CSS to set background image
st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: url("{background_image_url}");
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
        height: 100vh;
    }}
    </style>
    """,
    unsafe_allow_html=True
)

