import pandas as pd
import plotly.express as px
import streamlit as st

car_data = pd.read_csv('/Users/rocio/OneDrive/Escritorio/Coding/Proyect_sprint5/vehicles_us.csv') # leer los datos

hist_button = st.button('Construir histograma') # crear un botón

st.header('Histograma de datos de anuncios de venta de coches')
        
if hist_button: # al hacer clic en el botón
    
    st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches') # escribir un mensaje

    fig = px.histogram(car_data, x="odometer") # crear un histograma

    st.plotly_chart(fig, use_container_width=True) # mostrar un gráfico Plotly interactivo