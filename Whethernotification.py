import requests
from plyer import notification

geo_url = "https://geocoding-api.open-meteo.com/v1/search"

geo_params = {"name": "London", "count": 1}

geo_res = requests.get(geo_url, params=geo_params).json()