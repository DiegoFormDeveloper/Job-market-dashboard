import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="Dashboard de Ofertas de Empleo",
    page_icon="📊",
    layout="wide"
)

st.title("📊 Dashboard de Ofertas de Empleo")
st.write("Herramienta interactiva de analítica de datos cargada mediante Web Scraping.")

@st.cache_data
def cargar_datos():
    return pd.read_csv("ofertas_empleo.csv")

df = cargar_datos()


st.sidebar.header("🔍 Filtros")
ubicacion_seleccionada = st.sidebar.multiselect(
    "Filtrar por Ubicación:",
    options=df["Ubicacion"].unique(),
    default=[]
)

puesto_busqueda = st.sidebar.text_input("Buscar en el puesto:")


if ubicacion_seleccionada:
    df_filtrado = df[df["Ubicacion"].isin(ubicacion_seleccionada)]
else:
    df_filtrado = df.copy()


if puesto_busqueda:
    
    keywords = [kw.strip() for kw in puesto_busqueda.split(",") if kw.strip()]
    if keywords:
        
        pattern = "|".join(keywords)
        df_filtrado = df_filtrado[df_filtrado["Puesto"].str.contains(pattern, case=False, na=False, regex=True)]


st.markdown("---")
col1, col2, col3 = st.columns(3)
col1.metric("📌 Ofertas Mostradas", len(df_filtrado))
col2.metric("🏢 Empresas", df_filtrado["Empresa"].nunique())
col3.metric("📍 Ubicaciones", df_filtrado["Ubicacion"].nunique())
st.markdown("---")


col_graf1, col_graf2 = st.columns(2)

with col_graf1:
    st.subheader("🏢 Top 5 Empresas con más ofertas")
    top_empresas = df_filtrado["Empresa"].value_counts().head(5).reset_index()
    top_empresas.columns = ["Empresa", "Cantidad"]
    fig_empresas = px.bar(top_empresas, x="Cantidad", y="Empresa", orientation='h', color="Cantidad", color_continuous_scale="Viridis")
    st.plotly_chart(fig_empresas, use_container_width=True)

with col_graf2:
    st.subheader("📍 Top 5 Ubicaciones")
    top_ubicaciones = df_filtrado["Ubicacion"].value_counts().head(5).reset_index()
    top_ubicaciones.columns = ["Ubicacion", "Cantidad"]
    
    fig_ubicaciones = px.pie(
        top_ubicaciones, 
        values="Cantidad", 
        names="Ubicacion", 
        hole=0.4
    )
   
    fig_ubicaciones.update_layout(transition_duration=500)
    
    st.plotly_chart(fig_ubicaciones, use_container_width=True, key="grafica_ubicaciones")


st.subheader("📋 Listado de Ofertas")


st.dataframe(
    df_filtrado,
    column_config={
        "Enlace": st.column_config.LinkColumn("Enlace a la Oferta")
    },
    use_container_width=True
)


csv = df_filtrado.to_csv(index=False).encode('utf-8')
st.download_button(
    label="📥 Descargar datos filtrados (CSV)",
    data=csv,
    file_name='ofertas_filtradas.csv',
    mime='text/csv',
)