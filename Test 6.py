import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
import seaborn as sns

# Titel van de applicatie
st.title("Uitgebreide Geavanceerde Streamlit App - Data Analyse en Visualisaties")

# Sidebar voor navigatie
st.sidebar.title("Navigatie")
keuze = st.sidebar.radio("Kies een sectie", [
    "Home", "Data Upload", "Interactieve Visualisaties", "Kaart", 
    "Realtime Updates", "Data Transformaties", "Correlatiematrix"
])

# 1. Home sectie
if keuze == "Home":
    st.header("Welkom bij de Uitgebreide Geavanceerde Streamlit App!")
    st.write("""
        In deze uitgebreide app kun je de volgende onderdelen ontdekken:
        - Uploaden en analyseren van datasets.
        - Interactieve visualisaties met Plotly.
        - Dynamische kaarten, real-time grafieken, data-transformaties, en correlatiematrices.
    """)
    
    # Progressiebalk
    st.write("Hier is een voorbeeld van een voortgangsbalk:")
    progress = st.progress(0)
    for i in range(100):
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
        if len(kolommen) >= 2:
            x_as = st.selectbox("Kies X-as", kolommen)
            y_as = st.selectbox("Kies Y-as", kolommen)

            # Interactieve Plotly scatterplot
            fig = px.scatter(df, x=x_as, y=y_as, title=f'Scatterplot van {x_as} vs {y_as}')
            st.plotly_chart(fig)

# 3. Interactieve Visualisaties
elif keuze == "Interactieve Visualisaties":
    st.header("Geavanceerde grafieken en visualisaties")
    
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

    st.subheader("Boxplot met Plotly")
    # Willekeurige data voor boxplot
    data_box = pd.DataFrame({
        'categorie': np.random.choice(['Groep 1', 'Groep 2', 'Groep 3'], size=100),
        'waarden': np.random.randn(100) * 10 + 50
    })

    box_fig = px.box(data_box, x='categorie', y='waarden', title="Boxplot van Categorieën")
    st.plotly_chart(box_fig)

# 4. Kaart visualisatie
elif keuze == "Kaart":
    st.header("Interactieve kaart met extra functionaliteiten")
    
    # Willekeurige locaties genereren (latitude en longitude)
    locaties = pd.DataFrame({
        'lat': np.random.uniform(-90, 90, 100),
        'lon': np.random.uniform(-180, 180, 100)
    })

    # Extra filteroptie op basis van random gegenereerde data
    st.subheader("Filter locaties")
    min_lat = st.slider('Minimale breedtegraad', -90.0, 90.0, -90.0)
    max_lat = st.slider('Maximale breedtegraad', -90.0, 90.0, 90.0)
    gefilterde_locaties = locaties[(locaties['lat'] >= min_lat) & (locaties['lat'] <= max_lat)]

    st.map(gefilterde_locaties)

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

    # In plaats van wachten, tonen we de volledige grafiek in één keer
    for i in range(1, len(x_vals)+1):
        fig.data[0].x = x_vals[:i]
        fig.data[0].y = y_vals[:i]
        realtime_data.plotly_chart(fig)

# 6. Data Transformaties
elif keuze == "Data Transformaties":
    st.header("Data Transformaties")
    
    if uploaded_file is not None:
        st.write("Voer enkele basisdata-transformaties uit op de geüploade dataset.")

        # Normalisatie
        st.subheader("Normalisatie")
        kolom = st.selectbox("Kies een kolom om te normaliseren", df.columns)
        df['genormaliseerd'] = (df[kolom] - df[kolom].min()) / (df[kolom].max() - df[kolom].min())
        st.write(df[['genormaliseerd']].head())

        # Log-transformatie
        st.subheader("Log-transformatie")
        log_kolom = st.selectbox("Kies een kolom voor log-transformatie", df.columns)
        df['log_transformatie'] = np.log(df[log_kolom].replace(0, np.nan)).fillna(0)
        st.write(df[['log_transformatie']].head())

# 7. Correlatiematrix
elif keuze == "Correlatiematrix":
    st.header("Correlatiematrix")
    
    if uploaded_file is not None:
        st.write("Hier is de correlatiematrix van de geüploade dataset.")

        # Correlatiematrix berekenen
        corr_matrix = df.corr()

        # Correlatiematrix visualiseren met Seaborn
        st.write(sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', vmin=-1, vmax=1, cbar=True))
        st.pyplot()  # Om de Seaborn-plot te tonen
