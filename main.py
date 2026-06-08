import openmeteo_requests
import pandas as pd
import requests_cache
from retry_requests import retry
from db import init_db, save_weather
from show import show_data

cache_session = requests_cache.CachedSession(".cache", expire_after=3600)
retry_session = retry(cache_session, retries=5, backoff_factor=0.2)
openmeteo = openmeteo_requests.Client(session=retry_session)

url = "https://api.open-meteo.com/v1/forecast"

params = {
    "latitude": 35.6895,
    "longitude": 139.6917,
    "daily": [
        "temperature_2m_max",
        "temperature_2m_min",
        "precipitation_sum",
        "uv_index_max",
    ],
    "timezone": "Asia/Tokyo",
    "past_days": 7,
    "forecast_days": 0,
}

responses = openmeteo.weather_api(url, params=params)
response = responses[0]

daily = response.Daily()

daily_dataframe = pd.DataFrame(
    {
        "date": pd.date_range(
            start=pd.to_datetime(daily.Time(), unit="s", utc=True),
            end=pd.to_datetime(daily.TimeEnd(), unit="s", utc=True),
            freq=pd.Timedelta(seconds=daily.Interval()),
            inclusive="left",
        )
        .tz_convert(response.Timezone().decode())
        .strftime("%Y-%m-%d"),
        "temperature_2m_max": daily.Variables(0).ValuesAsNumpy(),
        "temperature_2m_min": daily.Variables(1).ValuesAsNumpy(),
        "precipitation_sum": daily.Variables(2).ValuesAsNumpy(),
        "uv_index_max": daily.Variables(3).ValuesAsNumpy(),
    }
)

init_db()
save_weather(daily_dataframe)

print("saved\n\nTable: weather_history")

show_data()
