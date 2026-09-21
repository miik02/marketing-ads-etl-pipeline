# 📊 End-to-End Marketing Data Pipeline & Executive Dashboard

## 📝 Project Description
This project is an end-to-end **Data Engineering and Business Intelligence** solution designed to automate the ingestion, cleaning, and visualization of digital marketing campaign performance data (Google Ads and Meta Ads). 

The main goal is to eliminate manual Excel consolidation through an automated cloud-based ETL pipeline, delivering actionable insights via an interactive dashboard focused on executive decision-making.

<img width="783" height="754" alt="image" src="https://github.com/user-attachments/assets/6ffec451-8d73-4496-9e76-f9c74e1cd8e7" />


## 🏗️ Architecture & Technologies
*   **Language:** Python 3.10
*   **Data Manipulation:** Pandas, NumPy
*   **Data Warehouse:** PostgreSQL (hosted on Supabase)
*   **ORM / Connection:** SQLAlchemy, Psycopg2-binary
*   **Orchestration / CI/CD:** GitHub Actions (Cron Jobs)
*   **Business Intelligence (BI):** Looker Studio
*   **Security:** GitHub Secrets (Environment variable management)

## ⚙️ Pipeline Flow (ETL)
The data lifecycle follows a daily automated process:

1.  **Data Simulation (Mocking):** The `generate_mock_data.py` script programmatically generates realistic datasets mimicking Meta and Google Ads exports, managing logical distributions of spend, impressions, and conversions.
2.  **Extract:** Reading the generated raw files.
3.  **Transform:** 
    *   Harmonization of disparate schemas (column renaming and mapping between platforms).
    *   Null value handling and data imputation.
    *   Data type normalization (`datetime`, `float`, `int64`).
    *   Concatenation into a single master *DataFrame*.
4.  **Load:** Insertion of the clean data into the Supabase PostgreSQL relational database using `SQLAlchemy` and a Connection Pooler (Session Mode) to ensure connection stability.
5.  **Automation:** A GitHub Actions workflow runs the complete pipeline unattended every day at 04:00 AM UTC, ensuring fresh data is ready first thing in the morning.

## 📈 Visualization & Data Storytelling
The final deliverable is an interactive Looker Studio dashboard designed under advanced visual analytics principles:
*   **Z-Pattern Layout:** Visual hierarchy prioritizing global KPIs in the top-left area.
*   **Dual Axes:** Complex time-series charts to correlate spend versus performance (conversions) across different numerical scales.
*   **Heatmaps:** Granular tables with conditional formatting to quickly identify high-impact campaigns (Top Performers).

## 🔐 Security & Best Practices
*   **Zero Exposed Credentials:** Database connection is dynamically handled using environment variables retrieved from *GitHub Secrets*.
*   **Modularity:** Code refactored into single-purpose functions to facilitate maintenance and scalability.
*   **Network Resolution:** Configuration of specific ports and Session Pooling to overcome IPv6 connectivity limitations in legacy BI tools (JDBC).

## 📂 Repository Structure
```text
├── .github/workflows/
│   └── etl_diario.yml          # GitHub Actions engine configuration
├── data_automation.py          # Main ETL pipeline script
├── generate_mock_data.py       # Synthetic data generator
├── requirements.txt            # Python environment dependencies
└── README.md
```

---



# 📊 End-to-End Marketing Data Pipeline & Executive Dashboard

## 📝 Descripción del Proyecto
Este proyecto es una solución integral de **Data Engineering y Business Intelligence** diseñada para automatizar la ingesta, limpieza y visualización de datos de rendimiento de campañas de marketing digital (Google Ads y Meta Ads). 

El objetivo es eliminar el trabajo manual de consolidación de excels mediante un pipeline ETL automatizado en la nube, entregando los insights a través de un panel de control interactivo enfocado en la toma de decisiones ejecutivas.

## 🏗️ Arquitectura y Tecnologías
*   **Lenguaje:** Python 3.10
*   **Data Manipulation:** Pandas, NumPy
*   **Data Warehouse:** PostgreSQL (alojado en Supabase)
*   **ORM / Conexión:** SQLAlchemy, Psycopg2-binary
*   **Orquestación / CI/CD:** GitHub Actions (Cron Jobs)
*   **Business Intelligence (BI):** Looker Studio
*   **Seguridad:** GitHub Secrets (Gestión de variables de entorno)

## ⚙️ Flujo del Pipeline (ETL)
El ciclo de vida del dato sigue un proceso automatizado diario:

1.  **Simulación de Datos (Mocking):** El script `generate_mock_data.py` genera programáticamente conjuntos de datos realistas imitando las exportaciones de Meta y Google Ads, gestionando distribuciones lógicas de gasto, impresiones y conversiones.
2.  **Extracción (Extract):** Lectura de los archivos crudos generados.
3.  **Transformación (Transform):** 
    *   Armonización de esquemas dispares (renombrado y mapeo de columnas entre plataformas).
    *   Tratamiento de valores nulos e imputación de datos.
    *   Normalización de tipos de datos (`datetime`, `float`, `int64`).
    *   Concatenación en un único *DataFrame* maestro.
4.  **Carga (Load):** Inserción de los datos limpios en la base de datos relacional PostgreSQL de Supabase utilizando `SQLAlchemy` y un *Connection Pooler* (Modo Sesión) para garantizar la estabilidad de la conexión.
5.  **Automatización:** Un *workflow* en GitHub Actions ejecuta el pipeline completo de manera desatendida todos los días a las 04:00 AM UTC, asegurando que los datos estén listos a primera hora de la mañana.

## 📈 Visualización y Data Storytelling
El producto final es un dashboard interactivo en Looker Studio diseñado bajo principios de analítica visual avanzada:
*   **Patrón de Lectura en Z:** Jerarquía visual que prioriza los KPIs globales en la zona superior izquierda.
*   **Ejes Duales:** Gráficos temporales complejos para correlacionar gasto versus rendimiento (conversiones) en distintas escalas numéricas.
*   **Mapas de Calor:** Tablas granulares con formato condicional para identificar rápidamente las campañas de mayor impacto (Top Performers).

## 🔐 Seguridad y Mejores Prácticas
*   **Cero Credenciales Expuestas:** La conexión a la base de datos se realiza dinámicamente mediante variables de entorno recuperadas de *GitHub Secrets*.
*   **Modularidad:** Código refactorizado en funciones de propósito único para facilitar el mantenimiento y escalabilidad.
*   **Resolución de Redes:** Configuración de puertos específicos y *Session Pooling* para superar limitaciones de conectividad IPv6 en herramientas de BI heredadas (JDBC).

## 📂 Estructura del Repositorio
```text
├── .github/workflows/
│   └── etl_diario.yml          # Configuración del motor de GitHub Actions
├── data_automation.py          # Script principal del pipeline ETL
├── generate_mock_data.py       # Generador de datos sintéticos
├── requirements.txt            # Dependencias del entorno de Python
└── README.md
