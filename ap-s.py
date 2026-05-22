import requests
import pandas as pd
import datetime as dt
import os

os.makedirs("data", exist_ok=True)

all_apps_ids = [
  
    "6502288185",
    "1060048474",
    "1387380275",
    "1496540793",
    "1225362709",
    "1467891225",
    "1630681705",
    "510164019",
    "1403342029",
    "942919872",
    "1179371472",
    "1610129795",
    "6499590549",
    "1210668838",
    "1579229899"
]

country = "jo"

all_data = []

for bank in all_apps_ids:
    url = f"https://itunes.apple.com/lookup?id={bank}&country={country}"
    data = requests.get(url).json()
    app_info = data["results"][0]

    all_data.append({
        "Store": "App Store",
        'Snapshot_Date': dt.datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        "app_id": app_info.get("bundleId"),
        "title": app_info.get("trackName"),
        "summary": app_info.get("trackCensoredName"),
        "rev_score": app_info.get("averageUserRating"),
        "num_of_ratings": app_info.get("userRatingCount"),
        "num_of_interactions": int(0),
        "installs": int(0),
        "realInstalls": int(0),
        "version": app_info.get("version"),
        "released": pd.to_datetime(app_info.get("releaseDate")).strftime("%B %#d, %Y"),
        "lastUpdatedOn": pd.to_datetime(app_info.get("currentVersionReleaseDate")).strftime("%B %#d, %Y"),
        "1_star_count": int(0),
        "2_star_count": int(0),
        "3_star_count": int(0),
        "4_star_count": int(0),
        "5_star_count": int(0)
    })

df = pd.DataFrame(all_data)

file_path = "data/Jordan_banks_Reviews_AppleStore.xlsx"
df.to_excel(file_path, index=False)

print("Saved:", file_path)
print("Files in data folder:", os.listdir("data"))
