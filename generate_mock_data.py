import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import random


def generate_marketing_data(range_time = [datetime(2026, 9, 1, 0, 0), datetime(2026, 9, 30, 0, 0)]):

    # first we define the possible campaigns name
    campaigns_name = ["Promo_otoño_26", "Lanzamiento_App", "Retargeting", "Verano_25"]
    duration = range_time[1] - range_time[0]
    # We image data coming from 2 sources: Meta and Google Ads, both with diferent formats:
    # Meta:
    meta_c_names = ["date_start", "campaign_name", "spend_eur", "impressions", "link_clicks", "leads_generated"]
    meta_data = []

    for campaign in campaigns_name:
        for i in range(duration.days + 1):

            n_days = timedelta(days=i)
            impressions = np.random.randint(5000, 20001)
            link_clicks = np.round(impressions * np.random.uniform(0.01, 0.03))
            leads_generated = np.round(link_clicks * np.random.uniform(0.05, 0.15))
            spend_eur = link_clicks * np.random.uniform(0.1, 0.4)

            row = {
                "date_start":range_time[0] + n_days, 
                "campaign_name": campaign + "_FB",
                "spend_eur": spend_eur,
                "impressions": impressions,
                "link_clicks": link_clicks,
                "leads_generated": leads_generated
            }
            meta_data.append(row)

    # Google:
    google_c_names = ["Day", "Campaign", "Cost", "Impressions", "Clicks", "Conversions"]
    google_data = []

    for campaign in campaigns_name:
            for i in range(duration.days + 1):
    
                n_days = timedelta(days=i)
                impressions = np.random.randint(1000, 8001)
                clicks = np.round(impressions * np.random.uniform(0.05, 0.1))
                conversion = np.round(clicks * np.random.uniform(0.1, 0.25))
                cost = clicks * np.random.uniform(0.8, 2.5)
    
                row = {
                    "Day":range_time[0] + n_days, 
                    "Campaign": campaign + "_Search",
                    "Cost": cost,
                    "Impressions": impressions,
                    "Clicks": clicks,
                    "Conversion": conversion
                }
                google_data.append(row)


    df_meta = pd.DataFrame(meta_data)
    df_google = pd.DataFrame(google_data)

    df_meta.to_csv("data/meta_data", index=False)
    df_google.to_csv("data/google_data", index=False)



        
    