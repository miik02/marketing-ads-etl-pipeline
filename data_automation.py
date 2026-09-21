import os
import pandas as pd
import numpy as np
from sqlalchemy import create_engine

def extract_data(data_path="data/"):
    """Extrae los datos crudos de los CSVs."""
    df_meta = pd.read_csv(os.path.join(data_path, "meta_data.csv"))
    df_google = pd.read_csv(os.path.join(data_path, "google_data.csv"))
    return df_meta, df_google

def transform_data(df_meta, df_google):
    """Limpia, estandariza y une los DataFrames."""
    meta_c_rename = {
        "date_start": "date", 
        "campaign_name": "campaign_name",
        "spend_eur": "spend",
        "impressions": "impressions",
        "link_clicks": "clicks",
        "leads_generated": "conversions"
    }

    google_c_rename = {
        "Day": "date", 
        "Campaign": "campaign_name",
        "Cost": "spend",
        "Impressions": "impressions",
        "Clicks": "clicks",
        "Conversion": "conversions"
    }

    df_meta.rename(columns=meta_c_rename, inplace=True)
    df_google.rename(columns=google_c_rename, inplace=True)

    df_meta["platform"] = "meta"
    df_google["platform"] = "google"

    # Concatenar
    df = pd.concat([df_meta, df_google], ignore_index=True)

    # Limpieza de nulos
    df["date"] = df["date"].replace("", np.nan)
    df.dropna(subset=["date"], inplace=True)
    
    df["campaign_name"] = df["campaign_name"].replace("", np.nan).fillna("Desconocida")
    df[["spend", "conversions", "clicks", "impressions"]] = df[["spend", "conversions", "clicks", "impressions"]].fillna(0)

    # Casteo de tipos
    column_types = {
        "campaign_name": "str",
        "spend": "float",
        "impressions": "int64",
        "clicks": "int64",
        "conversions": "int64"
    }
    df = df.astype(column_types)
    df["date"] = pd.to_datetime(df["date"])
    
    return df

def load_data(df):
    """Carga los datos limpios en la base de datos PostgreSQL en Supabase."""
    # Recuperamos la contraseña de las variables de entorno de GitHub Secrets
    db_password = os.getenv("DB_PASSWORD")
    
    if not db_password:
        raise ValueError("Error: No se ha encontrado la variable de entorno DB_PASSWORD.")

    # Construimos la URL de conexión de forma segura
    db_user = "postgres.bjerrtpbqmeeuacgyhrz"
    db_host = "aws-1-eu-west-1.pooler.supabase.com:5432"
    db_name = "postgres"
    
    connection_url = f"postgresql://{db_user}:{db_password}@{db_host}/{db_name}"
    
    engine = create_engine(connection_url)
    
    # Subimos los datos
    df.to_sql("ads_marketing", engine, if_exists="replace", index=False)
    print("✅ Datos cargados exitosamente en Supabase (tabla 'ads_marketing')")

def main():
    print("Iniciando proceso ETL...")
    df_meta, df_google = extract_data()
    df_clean = transform_data(df_meta, df_google)
    load_data(df_clean)
    print("🚀 Pipeline ETL finalizado con éxito.")

if __name__ == "__main__":
    main()