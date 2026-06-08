import sqlite3

DB = "plants.db"


def init_db():
    with sqlite3.connect(DB) as conn:
        conn.execute("""
            CREATE TABLE IF NOT EXISTS plants_data(
                id INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                scientific_name TEXT,
                temp_max REAL,
                temp_min REAL,
                grow_pattern TEXT,
                water_amount REAL,
                fertilizer TEXT,
                plant TEXT,
                harvest TEXT
            )
        """)


def save_plants(plants_dict):
    with sqlite3.connect(DB) as conn:
        columns = ", ".join(plants_dict.keys())
        placeholders = ", ".join([f":{key}" for key in plants_dict.keys()])
        query = f"INSERT INTO plants_data ({columns}) VALUES ({placeholders})"
        conn.execute(query, plants_dict)


def check_input(input_data):
    if input_data == "":
        return False
    return True


def Input_plants_data():
    name = input("Input name (*text): ")
    scientific_name = input("Scientific_name (text): ")
    temp_max = input("Temperture Max (float): ")
    if check_input(temp_max):
        temp_max = float(temp_max)
    else:
        temp_max = None
    temp_min = input("Temperture min (float): ")
    if check_input(temp_min):
        temp_min = float(temp_min)
    else:
        temp_min = None
    grow_pattern = input("Growing pattern (text):")
    water_amount = input("Watering amount (float): ")
    if check_input(water_amount):
        water_amount = float(water_amount)
    else:
        water_amount = None
    fertilizer = input("Fertilizer (text): ")
    plant = input("When Plants (text): ")
    harvest = input("When Harvest (text): ")

    plants_dict = {}
    plants_dict["name"] = name
    plants_dict["scientific_name"] = scientific_name
    plants_dict["temp_max"] = temp_max
    plants_dict["temp_min"] = temp_min
    plants_dict["grow_pattern"] = grow_pattern
    plants_dict["water_amount"] = water_amount
    plants_dict["fertilizer"] = fertilizer
    plants_dict["plant"] = plant
    plants_dict["harvest"] = harvest
    return plants_dict


def show_data():
    with sqlite3.connect(DB) as conn:
        cursor = conn.cursor()

        cursor.execute("""
            SELECT * FROM plants_data ORDER BY name
        """)
        columns = [description[0] for description in cursor.description]
        rows = cursor.fetchall()
        if not rows:
            print("No data found.")
            return
        # max width for each column
        col_widths = [
            max(len(str(row[i])) for row in rows + [columns])
            for i in range(len(columns))
        ]

        # header
        header = " | ".join(
            f"{col:<{width}}" for col, width in zip(columns, col_widths)
        )
        print(header)
        print("-" * len(header))

        # data rows
        for row in rows:
            print(
                " | ".join(
                    f"{str(item):<{width}}" for item, width in zip(row, col_widths)
                )
            )


if __name__ == "__main__":
    show_data()
