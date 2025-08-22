import pandas as pd
import psycopg2

# --- CONFIG ---
csv_path = 'data/processed/san_diego_housing_metrics.csv'

conn_info = {
    "dbname": "housing_data",
    "user": "postgres",  # Change if different
    "password": "",      # If Postgres.app doesn't use a password
    "host": "localhost",
    "port": "5432"
}

table_name = "san_diego_housing"

# --- Load the CSV ---
df = pd.read_csv(csv_path)
print(f"✅ Loaded CSV: {df.shape}")

# --- Connect to PostgreSQL ---
try:
    conn = psycopg2.connect(**conn_info)
    cur = conn.cursor()
    print("✅ Connected to PostgreSQL")

    # --- Create table (if it doesn't exist) ---
    cur.execute(f"""
        DROP TABLE IF EXISTS {table_name};
        CREATE TABLE {table_name} (
            date DATE,
            median_price INTEGER,
            inventory INTEGER,
            homes_sold INTEGER
        );
    """)
    conn.commit()
    print("✅ Table created")

    # --- Insert data row-by-row ---
    for _, row in df.iterrows():
        cur.execute(f"""
            INSERT INTO {table_name} (date, median_price, inventory, homes_sold)
            VALUES (%s, %s, %s, %s)
        """, (
            row['date'],
            int(row['median_price']) if pd.notnull(row['median_price']) else None,
            int(row['inventory']) if pd.notnull(row['inventory']) else None,
            int(row['homes_sold']) if pd.notnull(row['homes_sold']) else None
        ))

    conn.commit()
    print(f"✅ Inserted {df.shape[0]} rows into '{table_name}'")

except Exception as e:
    print("❌ Error:", e)

finally:
    if conn:
        cur.close()
        conn.close()
        print("✅ Connection closed")
