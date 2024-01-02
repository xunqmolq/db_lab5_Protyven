import csv
import psycopg2
from psycopg2 import sql

conn = psycopg2.connect(
    host = 'localhost',
    database='labs-db',
    user="protyven_labs",
    password="123"
)


cursor = conn.cursor()


csv_file_path = 'ramen-ratings.csv'


create_brand_table = """
CREATE TABLE IF NOT EXISTS brand (
    Brand_name VARCHAR NOT NULL,
    PRIMARY KEY (Brand_name)
);
"""

create_review_table = """
CREATE TABLE IF NOT EXISTS review (
    Stars FLOAT NOT NULL,
    Review_id INT NOT NULL,
    PRIMARY KEY (Review_id)
);
"""

create_ramen_table = """
CREATE TABLE IF NOT EXISTS ramen (
    Variety VARCHAR NOT NULL,
    Style VARCHAR NOT NULL,
    Country VARCHAR NOT NULL,
    Review_id INT NOT NULL,
    Brand_name VARCHAR NOT NULL,
    PRIMARY KEY (Variety),
    FOREIGN KEY (Review_id) REFERENCES Review(Review_id),
    FOREIGN KEY (Brand_name) REFERENCES Brand(Brand_name)
);
"""

cursor.execute(create_brand_table)
cursor.execute(create_review_table)
cursor.execute(create_ramen_table)

with open(csv_file_path, 'r', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    i = 0
    for row in reader:
        if i < 25:
            i += 1
            continue
        elif i >= 30:
            break
        brand_name = row['Brand']
        stars = float(row['Stars'])
        review_number = int(row['Review #'])
        variety = row['Variety']
        style = row['Style']
        country = row['Country']

        cursor.execute(sql.SQL("INSERT INTO brand (brand_name) VALUES ({}) ON CONFLICT (brand_name) DO NOTHING;").format(sql.Literal(brand_name)))
        cursor.execute(sql.SQL("INSERT INTO review (stars, review_id) VALUES ({}, {});").format(sql.Literal(stars), sql.Literal(review_number)))


        cursor.execute(sql.SQL("SELECT brand_name FROM brand WHERE brand_name = {};").format(sql.Literal(brand_name)))
        brand_id = cursor.fetchone()[0]

        cursor.execute(sql.SQL("INSERT INTO ramen (variety, style, country, review_id, brand_name) VALUES ({}, {}, {}, {}, {});").format(
            sql.Literal(variety), sql.Literal(style), sql.Literal(country), sql.Literal(review_number), sql.Literal(brand_id)
        ))
        i += 1

conn.commit()

cursor.close()
conn.close()