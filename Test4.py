import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
import time

# Titel van de applicatie
st.title("Geavanceerde Streamlit App - Data Analyse en Visualisaties (met Plotly)")

# Sidebar voor navigatie
st.sidebar.title("Navigatie")
keuze = st.sidebar.radio("Kies een sectie", ["Home", "Data Upload", "Interactieve Visualisaties", "Kaart", "Realtime Updates"])

# 1. Home sectie
if keuze == "Home":
    st.header("Welkom bij de Geavanceerde Streamlit App!")
    st.write("""
        In deze app kun je geavanceerdere features testen zoals:
        - Uploaden en analyseren van datasets.
        - Interactieve visualisaties met Plotly.
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

        # Interactieve Plotly scatterplot
        fig = px.scatter(df, x=x_as, y=y_as, title=f'Scatterplot van {x_as} vs {y_as}')
        st.plotly_chart(fig)

# 3. Interactieve Visualisaties
elif keuze == "Interactieve Visualisaties":
    st.header("Maak geavanceerde grafieken")
    
    # Willekeurige data genereren voor visualisaties
    data = pd.DataFrame({
        'categorie': ['A', 'B', 'C', 'D', 'E'],
        'waarden': np.random.randint(10, 100, size=5)
    })

    st.subheader("Bar chart met Plotly")
    bar_fig = px.bar(data, x='categorie', y='waarden', title="Bar Chart van Willekeurige Categorieën")
    st.plotly_chart(bar_fig)

    st.subheader("Histogram met Plotly")
    # Willekeurige normaal verdeelde data
    data_hist = np.random.randn(1000)
    
    hist_fig = px.histogram(data_hist, nbins=30, title="Histogram van Willekeurige Data")
    st.plotly_chart(hist_fig)

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
    
    # Realtime data visualisatie met Plotly
    x_vals = np.arange(0, 100)
    y_vals = np.sin(x_vals)

    realtime_data = st.empty()

    fig = go.Figure()
    fig.add_trace(go.Scatter(x=[], y=[], mode='lines', name='Sinusgolf'))

    for i in range(1, len(x_vals)+1):
        fig.data[0].x = x_vals[:i]
        fig.data[0].y = y_vals[:i]
        realtime_data.plotly_chart(fig)
        time.sleep(0.1)
