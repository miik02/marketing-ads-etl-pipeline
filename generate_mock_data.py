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

    for campaign in campaigns_name:
        for i in range(duration.days + 1):

            n_days = timedelta(days=i)
            impressions = np.random.randint(5000, 20001)
            link_clicks = impressions * np.random.uniform(0.01, 0.03)
            leads_generated = impressions * np.random.uniform(0.05, 0.15)
            spend_eur = link_clicks * np.random.uniform(0.1, 0.4)

            row = {
                "date_start":range_time[0] + n_days, 
                "campaign_name": campaign,
                "spend_eur": spend_eur,
                "impressions": impressions,
                "link_clicks": link_clicks,
                "leads_generated": leads_generated
            }


    # Google: