# Dashboard Interactivo de Ofertas de Empleo (Python & Streamlit)

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue.svg)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-App-red.svg)](https://streamlit.io/)
[![Pandas](https://img.shields.io/badge/Pandas-DataAnalysis-green.svg)](https://pandas.pydata.org/)

Aplicación web full-stack ligera desarrollada en Python que automatiza la extracción de ofertas de empleo mediante técnicas de **Web Scraping**, procesa y limpia los datos, y los presenta a través de un **dashboard interactivo** con métricas en tiempo real, gráficos analíticos avanzados, filtros dinámicos y capacidad de exportación.


## Características Principales

* **Web Scraping Automatizado:** Extracción de datos estructurados (puesto, empresa, ubicación, enlace) directamente desde fuentes web utilizando `BeautifulSoup`.
* **Procesamiento de Datos:** Limpieza, filtrado y estructuración de los datos mediante `Pandas`.
* **Interfaz Interactiva (Dashboard):** 
  * Vista inicial completa que muestra todas las ofertas de empleo por defecto.
  * Barra lateral con filtros avanzados:
    * Selección múltiple por ubicación.
    * Búsqueda avanzada de puestos con soporte para **múltiples palabras clave separadas por comas** (ej: `Engineer, Lead`).
  * KPIs y métricas clave en tiempo real.
  * Gráficos interactivos limpios (Top 5 empresas y Top 5 ubicaciones) construidos con `Plotly`.
* **Exportación de Datos:** Funcionalidad para descargar los datos filtrados directamente en formato CSV.
* **Enlaces Directos:** Acceso directo a las ofertas originales desde la propia tabla interactiva.


## Tecnologías Utilizadas

* **Python:** Lenguaje principal de programación.
* **BeautifulSoup4 & Requests:** Extracción y descarga de contenido web.
* **Pandas:** Manipulación y análisis de datos tabulares.
* **Streamlit:** Desarrollo de la interfaz gráfica y despliegue local de la app web.
* **Plotly:** Visualización de gráficos interactivos.


## Próximas Mejoras (Roadmap)
* Integración con APIs de ofertas de empleo reales (LinkedIn, InfoJobs, etc.).
* Despliegue en la nube gratuito con Streamlit Cloud.
* Análisis de sentimiento o categorización de tecnologías mediante IA.