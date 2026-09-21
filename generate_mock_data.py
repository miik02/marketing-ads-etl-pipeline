import os
import pandas as pd
import numpy as np
from datetime import datetime, timedelta

def generate_marketing_data(range_time=None):
    """Genera datos simulados de Meta y Google Ads y los guarda en CSV."""
    if range_time is None:
        range_time = [datetime(2026, 9, 1, 0, 0), datetime(2026, 9, 30, 0, 0)]
        
    campaigns_name = ["Promo_otoño_26", "Lanzamiento_App", "Retargeting", "Verano_25"]
    duration = range_time[1] - range_time[0]
    
    meta_data = []
    google_data = []

    # Generación de datos de Meta
    for campaign in campaigns_name:
        for i in range(duration.days + 1):
            n_days = timedelta(days=i)
            impressions = np.random.randint(5000, 20001)
            link_clicks = np.round(impressions * np.random.uniform(0.01, 0.03))
            leads_generated = np.round(link_clicks * np.random.uniform(0.05, 0.15))
            spend_eur = link_clicks * np.random.uniform(0.1, 0.4)

            meta_data.append({
                "date_start": range_time[0] + n_days, 
                "campaign_name": f"{campaign}_FB",
                "spend_eur": spend_eur,
                "impressions": impressions,
                "link_clicks": link_clicks,
                "leads_generated": leads_generated
            })

    # Generación de datos de Google
    for campaign in campaigns_name:
        for i in range(duration.days + 1):
            n_days = timedelta(days=i)
            impressions = np.random.randint(1000, 8001)
            clicks = np.round(impressions * np.random.uniform(0.05, 0.1))
            conversion = np.round(clicks * np.random.uniform(0.1, 0.25))
            cost = clicks * np.random.uniform(0.8, 2.5)

            google_data.append({
                "Day": range_time[0] + n_days, 
                "Campaign": f"{campaign}_Search",
                "Cost": cost,
                "Impressions": impressions,
                "Clicks": clicks,
                "Conversion": conversion
            })

    # Crear directorio si no existe
    os.makedirs("data", exist_ok=True)

    # Guardar CSVs
    pd.DataFrame(meta_data).to_csv("data/meta_data.csv", index=False)
    pd.DataFrame(google_data).to_csv("data/google_data.csv", index=False)
    print("Datos simulados generados correctamente en la carpeta 'data/'")

if __name__ == "__main__":
    generate_marketing_data()