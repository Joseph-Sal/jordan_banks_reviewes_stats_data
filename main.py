# This code shows the app stats --Google Play Store.

from google_play_scraper import app
import pandas as pd
import datetime as dt
import os

banks_ids = [
    # JCB
    "com.icsfs.jcb.retail",
    # Etihad
    "com.ofss.fcdb.mobile.android.phone.BAE.launcher"

    # ---------------
    # complete the rest at work

]

all_data = []

for bank in banks_ids:
    result = app(
        bank,
        lang='en',
        country='jo'
    )

    # Convert selected fields into a pandas DataFrame
    all_data.append({
        'Store': str("Google Play Store"),
        'Snapshot_Date': dt.datetime.now(),
        'app_id': result.get('appId'),
        'title': result.get('title'),
        'summary': result.get('summary'),
        'rev_score': result.get('score'),
        'num_of_ratings': result.get('ratings'),
        'num_of_interactions': result.get('reviews'),
        'installs': result.get('installs'),
        'realInstalls': result.get('realInstalls'),
        'version': result.get('version'),
        'released': result.get('released'),
        'lastUpdatedOn': result.get('lastUpdatedOn'),
        '1_star_count': int(result.get('histogram')[-5]),
        '2_star_count': int(result.get('histogram')[-4]),
        '3_star_count': int(result.get('histogram')[-3]),
        '4_star_count': int(result.get('histogram')[-2]),
        '5_star_count': int(result.get('histogram')[-1]),
    })

df = pd.DataFrame(all_data)

os.makedirs("data", exist_ok=True)
df.to_excel("data/jordan_banks_google_play.xlsx", index=False)
# Save to Excel
df.to_excel("Jordan_banks_Reviews_Results -- Google Play Store apps --.xlsx", index=False)

print("Excel file saved successfully.")
