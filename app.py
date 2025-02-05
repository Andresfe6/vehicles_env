import streamlit as st
import pandas as pd
import plotly.express as px

# Cargar el archivo CSV en un DataFrame
df = pd.read_csv('C:/Users/Laptop/Proyectos/vehicles_env/vehicles_us.csv')

# Crear un encabezado para la aplicación
st.header("Análisis de vehículos - Visualización de gráficos")

# Mostrar un resumen de los datos
st.write("Vista previa de los datos:", df.head())

# Crear un botón para generar el histograma
hist_button = st.button('Construir histograma')

# Al hacer clic en el botón, crear y mostrar el histograma
if hist_button:
    st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
    
    # Crear el histograma
    fig_hist = px.histogram(df, x='odometer', title="Histograma de Odometer")
    
    # Mostrar el gráfico interactivo
    st.plotly_chart(fig_hist, use_container_width=True)

# Casillas de verificación para seleccionar el gráfico a mostrar
show_histogram = st.checkbox('Mostrar Histograma')
show_scatter_plot = st.checkbox('Mostrar Diagrama de Dispersión')

# Generar un histograma si la casilla está marcada
if show_histogram:
    st.write('Histograma de Odometer:')
    fig_hist = px.histogram(df, x='odometer', title="Histograma de Odometer")
    st.plotly_chart(fig_hist)  # Mostrar el gráfico en Streamlit

# Generar un gráfico de dispersión si la casilla está marcada
if show_scatter_plot:
    st.write('Diagrama de Dispersión entre Odometer y Precio:')
    fig_scatter = px.scatter(df, x='odometer', y='price', title="Relación entre Odometer y Precio")
    st.plotly_chart(fig_scatter)  # Mostrar el gráfico en Streamlit
