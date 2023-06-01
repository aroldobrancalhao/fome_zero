#Libraries
import pandas as pd
import plotly.express as px
import streamlit as st
from PIL import Image
import folium
from streamlit_folium import folium_static
import inflection

st.set_page_config( page_title='Countries', page_icon='📈', layout='wide' )

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

selection_pais = st.sidebar.multiselect(
    'Escolha os Paises que Deseja visualizar os Restaurantes',
    ['Brazil', 'England', 'Qatar', 'South Africa', 'Canada', 'Australia', 'Philippines', 'Singapure', 'India', 'Indonesia', 'New Zeland', 'Sri Lanka', 'Sri Lanka', 'United States of America', 'United Arab Emirates'],
    default=['Brazil', 'England', 'Qatar', 'South Africa', 'Canada', 'Australia'])

linhas_selecionadas = df1['country_code'].isin(selection_pais)
df1 = df1.loc[linhas_selecionadas, :]

#filtro de pais
#linhas_selecionada = df1['****'].isin( selection_pais )
#df1 = df1.loc[linhas_selecionada, :]




st.write("# 🌎 Visão Países")



with st.container():
    st.markdown("###### Quantidade de Restaurantes Registrados por País")
    df_aux1 = df1[['country_code', 'restaurant_id']].groupby('country_code').count().sort_values('restaurant_id', ascending=False).reset_index()
    fig = px.bar(df_aux1,
       x='country_code',
       y='restaurant_id',
       color='country_code',
       labels={'country_code': 'Paises', 'restaurant_id': 'Quantidade de Restaurantes'},
        text='restaurant_id')
    fig.update_traces(texttemplate='%{text}', textposition='inside')  # Posiciona o texto dentro das barras
    st.plotly_chart(fig, use_container_width=True)
    
with st.container():
    st.markdown("###### Quantidade de Cidades Registrados por País")
    cidades = df1[['country_code', 'city']].drop_duplicates().groupby('country_code').count().sort_values('city', ascending=False).reset_index()
    fig = px.bar(cidades,
       x='country_code',
       y='city',
       color='country_code',
       labels={'country_code': 'Paises', 'restaurant_id': 'Quantidade de Cidades'},
        text='city')
    fig.update_traces(texttemplate='%{text}', textposition='inside')  # Posiciona o texto dentro das barras

    st.plotly_chart(fig, use_container_width=True)


with st.container():
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("###### Média de Avaliações feitas por País")
        avaliacao = df1[['country_code', 'votes']].drop_duplicates().groupby('country_code').mean().sort_values('votes', ascending=False).reset_index()
        fig = px.bar(avaliacao,
           x='country_code',
           y='votes',
           color='country_code',
           labels={'country_code': 'Paises', 'votes': 'Quantidade de Avaliações'},
            text='votes')
        fig.update_traces(texttemplate='%{text:.2f}', textposition='outside')  # Posiciona o texto dentro das barras
    
        st.plotly_chart(fig, use_container_width=True)

    with col2:
        st.write("###### Média de Preço de um prato para duas pessoas po País")
        avaliacao = df1[['country_code', 'average_cost_for_two']].drop_duplicates().groupby('country_code').mean().sort_values('average_cost_for_two', ascending=False).reset_index()
        fig = px.bar(avaliacao,
           x='country_code',
           y='average_cost_for_two',
           color='country_code',
           labels={'country_code': 'Paises', 'average_cost_for_two': 'Preço de prato para duas pessoas'},
            text='average_cost_for_two')
        fig.update_traces(texttemplate='%{text:.2f}', textposition='outside')  # Posiciona o texto dentro das barras
    
        st.plotly_chart(fig, use_container_width=True)


