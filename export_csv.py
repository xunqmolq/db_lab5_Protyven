import csv
import psycopg2

username = 'protyven_labs'
password = '123'
database = 'labs-db'
host = 'localhost'
port = '5432'

conn = psycopg2.connect(user=username, password=password, dbname=database, host=host, port=port)

with conn:
    cur = conn.cursor()
    tables_name = ['brand', 'ramen', 'review']

    for table_name in tables_name:
        cur.execute(f'SELECT * FROM {table_name}')
        rows = cur.fetchall()

        columns = [desc[0] for desc in cur.description]

        with open(f'{table_name}.csv', 'w', newline='', encoding='utf-8') as csvfile:
            csv_writer = csv.writer(csvfile)

            csv_writer.writerow(columns)

            csv_writer.writerows(rows)