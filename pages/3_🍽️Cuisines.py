#Libraries
import pandas as pd
import plotly.express as px
import streamlit as st
from PIL import Image
import folium
from streamlit_folium import folium_static
import inflection

st.set_page_config( page_title='Cuisines', page_icon='📈', layout='wide' )

# ==================================================== 
# Funções
# ==================================================== 

def clean_code( df1 ):
    title = lambda x: inflection.titleize(x)
    snakecase = lambda x: inflection.underscore(x)
    spaces = lambda x: x.replace(" ", "")
    cols_old = list(df1.columns)
    cols_old = list(map(title, cols_old))
    cols_old = list(map(spaces, cols_old))
    cols_new = list(map(snakecase, cols_old))
    df1.columns = cols_new
    
    COLORS = {
    "3F7E00": "darkgreen",
    "5BA829": "green",
    "9ACD32": "lightgreen",
    "CDD614": "orange",
    "FFBA00": "red",
    "CBCBC8": "darkred",
    "FF7800": "darkred",
    }
    
    COUNTRIES = {
    1: "India",
    14: "Australia",
    30: "Brazil",
    37: "Canada",
    94: "Indonesia",
    148: "New Zeland",
    162: "Philippines",
    166: "Qatar",
    184: "Singapure",
    189: "South Africa",
    191: "Sri Lanka",
    208: "Turkey",
    214: "United Arab Emirates",
    215: "England",
    216: "United States of America",
    }
    df1['country_code'] = df1['country_code'].replace(COUNTRIES)
    
    RANGE = {
        1: "cheap",
        2: "normal",
        3: "expensive",
        4: "gourmet"
        }
    df1['price_range'] = df1['price_range'].replace(RANGE)
    
    df1.drop_duplicates(inplace=True)
    df1.dropna(subset=['cuisines'], inplace=True)
    df1['cuisines'] = df1.loc[:, 'cuisines'].apply(lambda x: x.split(',')[0])
    df1 = df1.reset_index()
    return df1


# ==================================================== 
#                  import dataset
# ==================================================== 
df = pd.read_csv( 'dataset/zomato.csv' )
df1 = df.copy()

# ==================================================== 
#                  Limpando Dados                  
# ==================================================== 

df1 = clean_code( df ) 

# ==================================================== 
#                  BARRA LATERAL                    
# ==================================================== 

countries = st.sidebar.multiselect(
    'Escolha os Paises que Deseja visualizar os Restaurantes',
    ['Brazil', 'England', 'Qatar', 'South Africa', 'Canada', 'Australia', 'Philippines', 'Singapure', 'India', 'Indonesia', 'New Zeland', 'Sri Lanka', 'Sri Lanka', 'United States of America', 'United Arab Emirates'],
    default=['Brazil', 'England', 'Qatar', 'South Africa', 'Canada', 'Australia'])


top_n = st.sidebar.slider(
     'Selecione a quantidade de Restaurantes que deseja visualizar',
     value=int(10),
     min_value=int(1),
     max_value=int(20))

#filtro quantidade de restaurantes
#top_n = st.sidebar.slider("Selecione a quantidade de Restaurantes que deseja visualizar", 1, 20, 10)

cuisiness = st.sidebar.multiselect(
    'Escolha os Tipos de Culinária',
    list(df1['cuisines'].unique()),
     default=list(df1['cuisines'].unique()))

linhas_selecionadas = df1['country_code'].isin( countries )
df1 = df1.loc[linhas_selecionadas, :]

linhas_selecionadas2 = df1['cuisines'].isin( cuisiness )
df1 = df1.loc[linhas_selecionadas2, :]


#filtro de pais
#linhas_selecionada = df1['****'].isin( selection_pais )
#df1 = df1.loc[linhas_selecionada, :]



st.write("# 🍽️ Visão Tipos de Cusinhas!")

#st.write("## Melhores Restaurantes dos Principais tipos Culinários")

#==========================================
#       FUNÇÕES 
#==========================================

def top_cuisines():
    cuisines = {
        "Italian": "",
        "American": "",
        "Arabian": "",
        "Japanese": "",
        "Brazilian": ""
    }

    cols = [
        "restaurant_id",
        "restaurant_name",
        "country_code",
        "city",
        "cuisines",
        "average_cost_for_two",
        "currency",
        "aggregate_rating",
        "votes"
    ]

    for key in cuisines.keys():

        lines = df1["cuisines"] == key

        cuisines[key] = (
            df1.loc[lines, cols]
            .sort_values(["aggregate_rating", "restaurant_id"], ascending=[False, True])
            .iloc[0, :]
            .to_dict()
        )

    return cuisines


def write_metrics():

    cuisines = top_cuisines()

    italian, american, arabian, japonese, brazilian = st.columns(len(cuisines))

    with italian:
        st.metric(
            label=f'Italiana: {cuisines["Italian"]["restaurant_name"]}',
            value=f'{cuisines["Italian"]["aggregate_rating"]}/5.0',
            help=f"""
            País: {cuisines["Italian"]['country_code']}\n
            Cidade: {cuisines["Italian"]['city']}\n
            Média Prato para dois: {cuisines["Italian"]['average_cost_for_two']} ({cuisines["Italian"]['currency']})
            """,
        )

    with american:
        st.metric(
            label=f'Italiana: {cuisines["American"]["restaurant_name"]}',
            value=f'{cuisines["American"]["aggregate_rating"]}/5.0',
            help=f"""
            País: {cuisines["American"]['country_code']}\n
            Cidade: {cuisines["American"]['city']}\n
            Média Prato para dois: {cuisines["American"]['average_cost_for_two']} ({cuisines["American"]['currency']})
            """,
        )

    with arabian:
        st.metric(
            label=f'Italiana: {cuisines["Arabian"]["restaurant_name"]}',
            value=f'{cuisines["Arabian"]["aggregate_rating"]}/5.0',
            help=f"""
            País: {cuisines["Arabian"]['country_code']}\n
            Cidade: {cuisines["Arabian"]['city']}\n
            Média Prato para dois: {cuisines["Arabian"]['average_cost_for_two']} ({cuisines["Arabian"]['currency']})
            """,
        )

    with japonese:
        st.metric(
            label=f'Italiana: {cuisines["Japanese"]["restaurant_name"]}',
            value=f'{cuisines["Japanese"]["aggregate_rating"]}/5.0',
            help=f"""
            País: {cuisines["Japanese"]['country_code']}\n
            Cidade: {cuisines["Japanese"]['city']}\n
            Média Prato para dois: {cuisines["Japanese"]['average_cost_for_two']} ({cuisines["Japanese"]['currency']})
            """,
        )

    with brazilian:
        st.metric(
            label=f'Italiana: {cuisines["Brazilian"]["restaurant_name"]}',
            value=f'{cuisines["Brazilian"]["aggregate_rating"]}/5.0',
            help=f"""
            País: {cuisines["Brazilian"]['country_code']}\n
            Cidade: {cuisines["Brazilian"]['city']}\n
            Média Prato para dois: {cuisines["Brazilian"]['average_cost_for_two']} ({cuisines["Brazilian"]['currency']})
            """,
        )

    return None


def top_restaurants(countries, top_n):
    cols = [
        "restaurant_id",
        "restaurant_name",
        "country_code",
        "city",
        "cuisines",
        "average_cost_for_two",
        "aggregate_rating",
        "votes"
    ]

    lines = (df1["country_code"].isin(countries))

    dataframe = df1.loc[lines, cols].sort_values(
        ["aggregate_rating", "restaurant_id"], ascending=[False, True]
    )

    return dataframe.head(top_n)


def top_best_cuisines(countries, top_n):
    lines = df1["country_code"].isin(countries)

    grouped_df1 = (
        df1.loc[lines, ["aggregate_rating", "cuisines"]]
        .groupby("cuisines")
        .mean()
        .sort_values("aggregate_rating", ascending=False)
        .reset_index()
        .head(top_n)
    )

    fig = px.bar(
        grouped_df1.head(top_n),
        x="cuisines",
        y="aggregate_rating",
        text="aggregate_rating",
        text_auto=".2f",
        title=f"Top {top_n} Melhores Tipos de Culinárias",
        labels={
            "cuisines": "Tipo de Culinária",
            "aggregate_rating": "Média da Avaliação Média"
        },
    )

    return fig


def top_worst_cuisines(countries, top_n):
    lines = df1["country_code"].isin(countries)

    grouped_df1 = (
        df1.loc[lines, ["aggregate_rating", "cuisines"]]
        .groupby("cuisines")
        .mean()
        .sort_values("aggregate_rating")
        .reset_index()
        .head(top_n)
    )

    fig = px.bar(
        grouped_df1.head(top_n),
        x="cuisines",
        y="aggregate_rating",
        text="aggregate_rating",
        text_auto=".2f",
        title=f"Top {top_n} Piores Tipos de Culinárias",
        labels={
            "cuisines": "Tipo de Culinária",
            "aggregate_rating": "Média da Avaliação Média"
        },
    )

    return fig
#============================================
#       VISÃO CUISINES
#============================================

with st.container():
    df_restaurants = countries, top_n, cuisiness
    st.markdown(f"## Melhores Restaurantes dos Principais tipos Culinários")
    write_metrics()
#TABELA TOP 10            
    st.markdown(f"## Top {top_n} Restaurantes")
    df_aux = df1.loc[:, ['restaurant_id', 'restaurant_name', 'country_code', 'city', 'cuisines', 'average_cost_for_two', 'aggregate_rating','votes']].sort_values('aggregate_rating', ascending=False).head(top_n)
    st.dataframe(df_aux)

with st.container():
    col1, col2 = st.columns(2)
    
    with col1:
        fig = top_best_cuisines(countries, top_n)
        st.plotly_chart(fig, use_container_width=True)

    
    with col2:
        fig = top_worst_cuisines(countries, top_n)
        st.plotly_chart(fig, use_container_width=True)

#with st.container():
#            st.write('Top 20 restaurantes' ,unsafe_allow_html=True)
#            df_aux = df1.loc[:, ['restaurant_id','restaurant_name', 'country_code','city','cuisines','average_cost_for_two','aggregate_rating','votes']]
#            st.dataframe(df_aux)
