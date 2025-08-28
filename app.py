import streamlit as st
from PIL import Image

st.title(" Hola buenas tardes, alguien sabe como llegar a loquendo city ")

st.header ("Hola alguno sabe programar C++")

image = Image.open('Waltuh.jpg')

st.image(image, caption = 'Waltuh')


texto = st.text_input('Escribe algo', 'Este es mi texto')
