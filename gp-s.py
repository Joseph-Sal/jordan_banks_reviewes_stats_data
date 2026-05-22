from google_play_scraper import app
import pandas as pd
import datetime as dt
import os

os.makedirs("data", exist_ok=True)

banks_ids = [
    "com.icsfs.jcb.retail",
    "com.ofss.fcdb.mobile.android.phone.BAE.launcher",
    "com.arabbank.arabimobilev2",
    "com.hbtf",
    "com.icsfs.ajib.test",
    "com.ubanquity.ahli_jo",
    "com.bankofjordan.mobileapp",
    "com.mob.jkb",
    "com.icsfs.mobile.rajhi",
    "com.capital.cbt",
    "com.a2a.android.cab",
    "com.blombank.eblom.jo",
    "com.fact.jib",
    "com.icsfs.safwa",
    "com.iiab.mobilebanking"
]

all_data = []

for bank in banks_ids:
    result = app(
        bank,
        lang='en',
        country='jo'
    )

    hist = result.get('histogram', [0, 0, 0, 0, 0])

    all_data.append({
        'Store': "Google Play Store",
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
        '1_star_count': hist[0],
        '2_star_count': hist[1],
        '3_star_count': hist[2],
        '4_star_count': hist[3],
        '5_star_count': hist[4],
    })

df = pd.DataFrame(all_data)

file_path = "data/Jordan_banks_Reviews_GooglePlay.xlsx"
df.to_excel(file_path, index=False)

print("Saved:", file_path)
print("Files in data folder:", os.listdir("data"))
