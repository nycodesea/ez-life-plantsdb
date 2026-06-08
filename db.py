import sqlite3

DB = "weather.db"


def init_db():
    with sqlite3.connect(DB) as conn:
        conn.execute("""
            CREATE TABLE IF NOT EXISTS weather_history(
                date TEXT PRIMARY KEY,
                temp_max REAL,
                temp_min REAL,
                precipitation REAL,
                uv_index_max REAL
            )
        """)


def save_weather(df):
    with sqlite3.connect(DB) as conn:
        for _, row in df.iterrows():
            conn.execute(
                """
                INSERT OR REPLACE INTO weather_history
                (date, temp_max, temp_min, precipitation, uv_index_max)
                VALUES (?, ?, ?, ?, ?)
            """,
                (
                    row["date"],
                    float(row["temperature_2m_max"]),
                    float(row["temperature_2m_min"]),
                    float(row["precipitation_sum"]),
                    float(row["uv_index_max"]),
                ),
            )
