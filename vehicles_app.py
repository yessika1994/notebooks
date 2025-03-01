import pandas as pd
import plotly.express as px
import streamlit as st
car_data = pd.read_csv('vehicles_us.csv') # leer los datos
hist_button = st.button('Construir histograma') # crear un botón
scatter_button = st.button('Construir gráfico de dispersión') # crear un botón
show_histogram = st.checkbox('Mostrar histograma')
show_scatter = st.checkbox('Mostrar gráfico de dispersión')

        
if hist_button or show_histogram: # al hacer clic en el botón
            # escribir un mensaje
    st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
            
            # crear un histograma
    fig = px.histogram(car_data, x="odometer")
        
            # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)
    
if scatter_button or show_scatter: # al hacer clic en el botón
            # escribir un mensaje
    st.write('Creación de un grafico de dispersión para el conjunto de datos de anuncios de venta de coches')
            
            # crear un grafico de dispersión
    fig = px.scatter(car_data, x="year", y="price")
        
            # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)