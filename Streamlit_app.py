import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# Configuration de la page
st.set_page_config(page_title="Analyse Zomato Bengaluru", layout="wide", page_icon="🍴")


# --- CHARGEMENT ET NETTOYAGE (Optimisé) ---
@st.cache_data
def load_and_clean_data():
    # Chargement
    df = pd.read_csv('data/zomato.csv')  # Assure-toi que le fichier est dans /data/

    # Nettoyage des notes (ex: '4.1/5' -> 4.1)
    def clean_rate(x):
        if isinstance(x, str):
            x = x.split('/')[0].strip()
            if x in ['NEW', '-']: return None
            return float(x)
        return x

    df['rate'] = df['rate'].apply(clean_rate)

    # Nettoyage des coûts
    df['approx_cost'] = df['approx_cost(for two people)'].astype(str).apply(lambda x: x.replace(',', ''))
    df['approx_cost'] = pd.to_numeric(df['approx_cost'], errors='coerce')

    # Suppression des doublons et valeurs nulles critiques
    df = df.drop_duplicates(subset=['name', 'address', 'location'])
    return df.dropna(subset=['rate', 'approx_cost', 'location'])


df = load_and_clean_data()

# --- BARRE LATÉRALE (Filtres interactifs) ---
st.sidebar.header("🔍 Filtres de Recherche")

# Filtre par Quartier (Location)
selected_locations = st.sidebar.multiselect(
    "Choisir les quartiers :",
    options=sorted(df['location'].unique()),
    default=sorted(df['location'].unique())[:5]
)

# Filtre par Type de Service
selected_types = st.sidebar.multiselect(
    "Type de restaurant :",
    options=df['listed_in(type)'].unique(),
    default=df['listed_in(type)'].unique()
)

# Filtre par Prix (Slider)
min_price, max_price = int(df['approx_cost'].min()), int(df['approx_cost'].max())
price_range = st.sidebar.slider("Gamme de prix (pour deux)", min_price, max_price, (min_price, 2000))

# Application des filtres
mask = (df['location'].isin(selected_locations)) & \
       (df['listed_in(type)'].isin(selected_types)) & \
       (df['approx_cost'].between(price_range[0], price_range[1]))
df_filtered = df[mask]

# --- CORPS DE L'APPLICATION ---
st.title("📊 Analyse Exploratoire : Restaurants de Bengaluru")
st.markdown(f"Analyse de **{len(df_filtered)}** restaurants filtrés sur un total de {len(df)}.")

# 1. Indicateurs Clés (KPIs)
col_a, col_b, col_c, col_d = st.columns(4)
col_a.metric("Note Moyenne", f"{df_filtered['rate'].mean():.2f} / 5")
col_b.metric("Coût Moyen (2 pers)", f"{df_filtered['approx_cost'].mean():.0f} ₹")
col_c.metric("Votes Totaux", f"{df_filtered['votes'].sum():,}")
col_d.metric("Quartiers", f"{df_filtered['location'].nunique()}")

st.divider()

# 2. Onglets d'Analyse Structurée
tab1, tab2, tab3 = st.tabs(["📍 Géographie & Densité", "💰 Prix vs Popularité", "🍜 Cuisines & Services"])

with tab1:
    st.subheader("Répartition Géographique des Restaurants")
    # Graphique comparatif entre quartiers [cite: 35]
    fig_geo = px.bar(
        df_filtered['location'].value_counts().reset_index(),
        x='count', y='location', orientation='h',
        title="Densité de restaurants par quartier",
        color='count', color_continuous_scale='Viridis'
    )
    st.plotly_chart(fig_geo, use_container_width=True)

with tab2:
    st.subheader("Analyse de la Popularité et des Prix")
    col1, col2 = st.columns(2)

    with col1:
        # Relation Prix vs Note
        fig_scatter = px.scatter(
            df_filtered, x='approx_cost', y='rate',
            size='votes', color='listed_in(type)',
            hover_name='name', title="Relation Coût vs Note (Taille = Votes)"
        )
        st.plotly_chart(fig_scatter, use_container_width=True)

    with col2:
        # Distribution des notes par type [cite: 30, 33]
        fig_box = px.box(
            df_filtered, x='listed_in(type)', y='rate',
            color='listed_in(type)', title="Distribution des Notes par Catégorie"
        )
        st.plotly_chart(fig_box, use_container_width=True)

with tab3:
    st.subheader("Exploration des Cuisines et Options")

    # Top 15 Cuisines [cite: 23]
    top_cuisines = df_filtered['cuisines'].str.split(', ').explode().value_counts().head(15).reset_index()
    fig_cuisines = px.pie(top_cuisines, values='count', names='cuisines', hole=0.4,
                          title="Top 15 Cuisines les plus représentées")
    st.plotly_chart(fig_cuisines, use_container_width=True)

    # Options de commande
    col_order, col_table = st.columns(2)
    with col_order:
        st.write("**Commande en ligne**")
        st.plotly_chart(px.pie(df_filtered, names='online_order'), use_container_width=True)
    with col_table:
        st.write("**Réservation de table**")
        st.plotly_chart(px.pie(df_filtered, names='book_table'), use_container_width=True)

# 3. Table de données brute (pour exploration manuelle)
if st.checkbox("Afficher les données filtrées"):
    st.dataframe(df_filtered[['name', 'location', 'rate', 'approx_cost', 'cuisines']])