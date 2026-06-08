import sqlite3

DB = "weather.db"


def show_data():
    with sqlite3.connect(DB) as conn:
        cursor = conn.cursor()
        cursor.execute("""
            SELECT * FROM weather_history  ORDER BY date
        """)
        columns = [description[0] for description in cursor.description]
        rows = cursor.fetchall()

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
