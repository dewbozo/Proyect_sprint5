import pandas as pd
import plotly.express as px
import streamlit as st

car_data = pd.read_csv('vehicles_us.csv')

st.header('Analisis de datos de anuncios de autos a partir de datos de odometro') # encabezado 

build_histogram = st.checkbox('Construir histograma') # boton para crear hist
build_scatter = st.checkbox('Construir grafico de dispersion') # boton para crear scatter

if build_histogram: # si se seleccion la casilla
    st.write('Construyendo histograma para la columna odometro') # mensaje del boton

    fig = px.histogram(car_data, x="odometer") # crear un histograma
    st.plotly_chart(fig, use_container_width=True) # mostrar un gráfico Plotly interactivo

if build_scatter: # si se selecciona la casilla 
    st.write('Creacion de un grafico de dispersion para la columna odometro') # mensaje del boton

    fig = px.scatter(car_data, x="odometer", y="price") # crear diagrama de dispersion 
    st.plotly_chart(fig, use_container_width=True) # mostrar grafico 
 