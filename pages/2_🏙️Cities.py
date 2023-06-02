#Libraries
import pandas as pd
import plotly.express as px
import streamlit as st
from PIL import Image
import folium
from streamlit_folium import folium_static
import inflection

st.set_page_config( page_title='Cities', page_icon='📈', layout='wide' )

# ==================================================== 
# Funções
# ====================================================

def type_cuisine( df1 ):
    # Contar a quantidade de tipos culinários distintos por cidade
    df_city_cuisine = df1.groupby('city')['cuisines'].nunique().reset_index()
    df_city_cuisine.columns = ['city', 'Tipos Culinários Distintos']
    
    # Mapear os nomes dos países com base no country_code
    df_paises = df1.loc[:, ['city', 'country_code']].drop_duplicates()
    
    # Unir os DataFrames de cidade e país
    df_city_cuisine = df_city_cuisine.merge(df_paises, on='city', how='left')
    
    # Selecionar as 10 cidades com a maioria dos tipos culinários distintos
    df_top_cities = df_city_cuisine.nlargest(10, 'Tipos Culinários Distintos')
    
    # Criação do gráfico
    fig = px.bar(df_top_cities, 
                 x='city', 
                 y='Tipos Culinários Distintos', 
                 color='country_code',
                 labels={'city': 'Cidade', 'Tipos Culinários Distintos': 'Tipos Culinários Distintos'},
                 text='Tipos Culinários Distintos')
    
    # Adicionar legenda por país
    df_paises = df_paises.set_index('city').loc[df_top_cities['city'], 'country_code'].reset_index()
    fig.update_layout(legend_title_text='País', legend=dict(x=1.0, y=1.0, orientation='v', title_font=dict(size=12)))
    
    # Atualizar as configurações das barras
    fig.update_traces(texttemplate='%{text}', textposition='inside')
    return fig

def media_avaliacao( df1, par_1, par_2 ):
    # Filtrar restaurantes com média de avaliação acima de 4
    if par_1 == '<':
        # Filtrar restaurantes com média de avaliação abaixo do valor
        df_filtered = df1[df1['aggregate_rating'] < par_2]
    elif par_1 == '>':
        # Filtrar restaurantes com média de avaliação acima do valor
        df_filtered = df1[df1['aggregate_rating'] > par_2]
    else:
        return None  # Sinal inválido, retorna None ou levanta uma exceção
    
    # Contar a quantidade de restaurantes por cidade
    df_city_restaurants = df_filtered['city'].value_counts().reset_index()
    df_city_restaurants.columns = ['city', 'Quantidade de Restaurantes']
    
    # Selecionar as 7 primeiras cidades com mais restaurantes
    df_top_cities = df_city_restaurants.nlargest(7, 'Quantidade de Restaurantes')
    
    # Mapear os nomes dos países com base no country_code
    df_paises = df1.loc[:, ['city', 'country_code']].drop_duplicates()
    df_paises['country_name'] = df_paises['country_code'].map(COUNTRIES)
    
    # Criação do gráfico
    fig = px.bar(df_top_cities, 
                 x='city', 
                 y='Quantidade de Restaurantes', 
                 color=df_paises.set_index('city').loc[df_top_cities['city'], 'country_code'],
                 text='Quantidade de Restaurantes')  # Adiciona os valores nas barras
    
    fig.update_traces(texttemplate='%{text:.2f}', textposition='inside')  # Posiciona o texto dentro das barras
    return fig

def melhor_city( df1 ):
    df_city_restaurants = df1['city'].value_counts().nlargest(10)  # Contar o número de restaurantes por cidade e selecionar as top 10 cidades

    # Mapear os nomes dos países com base no country_code
    df_paises = df1.loc[:, ['city', 'country_code']].drop_duplicates()
    df_paises['country_name'] = df_paises['country_code'].map(COUNTRIES)
    
    # Criação do gráfico
    fig = px.bar(df_city_restaurants, 
                 x=df_city_restaurants.index, 
                 y=df_city_restaurants.values, 
                 color=df_paises.set_index('city').loc[df_city_restaurants.index, 'country_code'],
                 text=df_city_restaurants.values)  # Adiciona os valores nas barras
    
    fig.update_layout(xaxis_title='Cidade', yaxis_title='Quantidade de Restaurantes', legend_title='País')
    
    fig.update_traces(texttemplate='%{text:.2f}', textposition='inside')  # Exibe os valores fora das barras
    return fig

# ==================================================== 
#                  import dataset
# ==================================================== 
df = pd.read_csv( 'dataset/zomato.csv' )
df1 = df.copy()

# ==================================================== 
#                  Limpando Dados                  
# ==================================================== 

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


# ==================================================== 
#                  BARRA LATERAL                    
# ==================================================== 

countries = st.sidebar.multiselect(
    'Escolha os Paises que Deseja visualizar os Restaurantes',
    ['Brazil', 'England', 'Qatar', 'South Africa', 'Canada', 'Australia', 'Philippines', 'Singapure', 'India', 'Indonesia', 'New Zeland', 'Sri Lanka', 'Sri Lanka', 'United States of America', 'United Arab Emirates'],
    default=['Brazil', 'England', 'Qatar', 'South Africa', 'Canada', 'Australia'])


linhas_selecionadas = df1['country_code'].isin(countries)
df1 = df1.loc[linhas_selecionadas, :]

st.write("# 🏙️ Visão Cidades")

# ==================================================== 
#                  lAYOUT NO STREAMLIT                    
# ==================================================== 

with st.container():
    st.subheader("Top 10 Cidades com mais Restaurantes na Base de Dados")
    fig = melhor_city( df1 )
    st.plotly_chart(fig, use_container_width=True)


with st.container():
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("###### Top 7 Cidades com Restaurantes com média de avaliação acima de 4")
        fig = media_avaliacao( df1, '>', 4.0  )
        # Mostrar o gráfico no Streamlit
        st.plotly_chart(fig, use_container_width=True)
                
        
    
    with col2:
        st.write("###### Top 7 Cidades com Restaurantes com média de avaliação abaixo de 2.5")
        fig = media_avaliacao( df1, '<', 2.5 )
        # Mostrar o gráfico no Streamlit
        st.plotly_chart(fig, use_container_width=True)
        
with st.container():
    st.subheader("Top 10 Cidades mais Restaurantes com tipos culinários distintos")
    fig = type_cuisine( df1 )    
    # Mostrar o gráfico no Streamlit
    st.plotly_chart(fig, use_container_width=True)
    
