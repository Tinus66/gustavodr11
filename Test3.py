import streamlit as st
import pandas as pd
import numpy as np
import altair as alt
import matplotlib.pyplot as plt
import time

# Titel van de applicatie
st.title("Geavanceerde Streamlit App - Data Analyse en Visualisaties")

# Sidebar voor navigatie
st.sidebar.title("Navigatie")
keuze = st.sidebar.radio("Kies een sectie", ["Home", "Data Upload", "Interactieve Visualisaties", "Kaart", "Realtime Updates"])

# 1. Home sectie
if keuze == "Home":
    st.header("Welkom bij de Geavanceerde Streamlit App!")
    st.write("""
        In deze app kun je geavanceerdere features testen zoals:
        - Uploaden en analyseren van datasets.
        - Interactieve visualisaties met Altair en Matplotlib.
        - Dynamische kaarten en real-time grafieken.
    """)
    
    # Progressiebalk
    st.write("Hier is een voorbeeld van een voortgangsbalk:")
    progress = st.progress(0)
    for i in range(100):
        time.sleep(0.01)
        progress.progress(i + 1)

# 2. Data Upload sectie
elif keuze == "Data Upload":
    st.header("Upload een CSV-bestand om data te visualiseren")

    uploaded_file = st.file_uploader("Kies een CSV-bestand", type="csv")
    
    if uploaded_file is not None:
        # Laden van de data
        df = pd.read_csv(uploaded_file)
        st.write("Hier is een voorbeeld van je data:")
        st.dataframe(df.head())

        # Basisstatistieken van de data
        st.write("Statistieken van de dataset:")
        st.write(df.describe())

        # Kolommen kiezen voor scatterplot
        st.write("Maak een scatterplot op basis van je data:")
        kolommen = df.columns.tolist()
        x_as = st.selectbox("Kies X-as", kolommen)
        y_as = st.selectbox("Kies Y-as", kolommen)

        # Interactieve Altair scatterplot
        scatter = alt.Chart(df).mark_circle(size=60).encode(
            x=x_as,
            y=y_as,
            tooltip=list(kolommen)
        ).interactive()

        st.altair_chart(scatter, use_container_width=True)

# 3. Interactieve Visualisaties
elif keuze == "Interactieve Visualisaties":
    st.header("Maak geavanceerde grafieken")
    
    # Willekeurige data genereren voor visualisaties
    data = pd.DataFrame({
        'categorie': ['A', 'B', 'C', 'D', 'E'],
        'waarden': np.random.randint(10, 100, size=5)
    })

    st.subheader("Bar chart met Altair")
    bar_chart = alt.Chart(data).mark_bar().encode(
        x='categorie',
        y='waarden',
        color='categorie'
    )
    st.altair_chart(bar_chart, use_container_width=True)

    st.subheader("Histogram met Matplotlib")
    # Willekeurige normaal verdeelde data
    data_hist = np.random.randn(1000)
    
    fig, ax = plt.subplots()
    ax.hist(data_hist, bins=30, color='skyblue', alpha=0.7)
    st.pyplot(fig)

# 4. Kaart visualisatie
elif keuze == "Kaart":
    st.header("Interactieve kaart met willekeurige punten")
    
    # Willekeurige locaties genereren (latitude en longitude)
    locaties = pd.DataFrame({
        'lat': np.random.uniform(-90, 90, 100),
        'lon': np.random.uniform(-180, 180, 100)
    })

    st.map(locaties)

# 5. Realtime Updates sectie
elif keuze == "Realtime Updates":
    st.header("Realtime data visualisatie")
    
    st.write("Hieronder is een voorbeeld van een live-updating grafiek.")
    
    realtime_data = st.empty()
    x_vals = np.arange(0, 100)
    y_vals = np.sin(x_vals)

    for i in range(1, 101):
        fig, ax = plt.subplots()
        ax.plot(x_vals[:i], y_vals[:i])
        realtime_data.pyplot(fig)
        time.sleep(0.1)
