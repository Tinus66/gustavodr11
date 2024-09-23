import streamlit as st
import pandas as pd
import numpy as np

# Titel van de applicatie
st.title("Mijn Eerste Streamlit App!")

# 1. Tekstinvoer
naam = st.text_input("Wat is jouw naam?")

# 2. Keuzemenu (Dropdown)
favoriete_fruit = st.selectbox(
    "Wat is je favoriete fruit?",
    ("Appel", "Banaan", "Aardbei", "Druif")
)

# 3. Slider voor getalinput
leeftijd = st.slider("Hoe oud ben je?", 0, 100, 25)

# 4. Checkbox
wil_je_tabel_zien = st.checkbox("Wil je een willekeurige tabel zien?")

# 5. Knop
if st.button("Klik hier als je klaar bent"):
    st.write(f"Hallo {naam}! Je favoriete fruit is {favoriete_fruit} en je bent {leeftijd} jaar oud.")
    
# 6. Conditie om een tabel te laten zien
if wil_je_tabel_zien:
    data = pd.DataFrame(
        np.random.randn(10, 5),
        columns=('Kolom 1', 'Kolom 2', 'Kolom 3', 'Kolom 4', 'Kolom 5')
    )
    st.write("Hier is een willekeurige tabel:")
    st.dataframe(data)

# 7. Interactieve grafiek
st.write("Hieronder een eenvoudige grafiek:")
chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=['a', 'b', 'c']
)
st.line_chart(chart_data)
