#Libraries
import pandas as pd
import plotly.express as px
import streamlit as st
from PIL import Image
import folium
from streamlit_folium import folium_static
import inflection
from folium.plugins import MarkerCluster

st.set_page_config( page_title='Main Page', page_icon='📈', layout='wide' )

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
# Funções
# ==================================================== 

def mapa(df1):
        data_plot = df1.loc[:, ['restaurant_id', 'latitude', 'longitude' ]].groupby( ['restaurant_id'] ).median().reset_index()
        # Criar o mapa
        map_ = folium.Map(zoom_start=11)
        
        # Criar um cluster de marcadores
        marker_cluster = MarkerCluster().add_to(map_)
        
        # Adicionar marcadores individuais ao cluster
        for index, row in df1.iterrows():
            folium.Marker(
                location=[row['latitude'], row['longitude']],
                popup=row['restaurant_id'],
                icon=folium.Icon(color='blue', icon='cloud')
            ).add_to(marker_cluster)
        # Exibir o mapa no Streamlit
        folium_static(map_, width=1024, height=600)
        return None
        


# ==================================================== 
#                  BARRA LATERAL                    
# ==================================================== 

#image_path = '/comunidade_ds/repos/ftc/projeto/'
image = Image.open( 'teste.jpg' )
st.sidebar.image(image, width=50)

st.sidebar.markdown('# Fome Zero')

countries = st.sidebar.multiselect(
    'Escolha os Paises que Deseja visualizar os Restaurantes',
    ['Brazil', 'England', 'Qatar', 'South Africa', 'Canada', 'Australia', 'Philippines', 'Singapure', 'India', 'Indonesia', 'New Zeland', 'Sri Lanka', 'Sri Lanka', 'United States of America', 'United Arab Emirates'],
    default=['Brazil', 'England', 'Qatar', 'South Africa', 'Canada', 'Australia'])


linhas_selecionadas = df1['country_code'].isin(countries)
df1 = df1.loc[linhas_selecionadas, :]

@st.cache_data
def convert_df(df1):
    # IMPORTANT: Cache the conversion to prevent computation on every rerun
    return df1.to_csv().encode('utf-8')


csv = convert_df(df1)

st.sidebar.markdown("## Dados Tratados")
st.sidebar.download_button(
    label="Download",
    data=csv,
    file_name='data.csv',
    mime='text/csv'
)


# ==================================================== 
#                  lAYOUT NO STREAMLIT                    
# ==================================================== 

st.write("# Fome Zero!")

st.write("## O Melhor lugar para encontrar seu mais novo restaurante favorito!")

st.write("### Temos as seguintes marcas dentro da nossa plataforma:")

with st.container():
    col1, col2, col3, col4, col5 = st.columns(5, gap='small')
    
    with col1:
        st.write("###### Restaurantes Cadastrados")
        st.header(df1['restaurant_id'].nunique())
    
    with col2:
        st.write("###### Países Cadastrados")
        st.header(df1['country_code'].nunique())
    
    with col3:
        st.write("###### Cidades Cadastrados")
        st.header(df1['city'].nunique())
    
    with col4:
        st.write("###### Avaliações na Plataforma")
        st.header(df1['votes'].sum())
    
    with col5:
        st.write("###### Tipos de Culinárias Oferecidas")
        st.header(df1['cuisines'].nunique())

with st. container():
   map_ = mapa( df1 )
        


