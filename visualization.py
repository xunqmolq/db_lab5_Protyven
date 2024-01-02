import psycopg2
import matplotlib.pyplot as plt


username = 'protyven_labs'
password = '123'
database = 'labs-db'
host = 'localhost'
port = '5432'

query_1 = '''
SELECT review.stars AS grade, ramen.variety
FROM ramen NATURAL JOIN review
WHERE ramen.brand_name = 'Wei Wei';
'''

query_2 = '''
SELECT ramen.variety AS variety, review.stars AS grade
FROM ramen
NATURAL JOIN review
WHERE review.stars =(SELECT MAX(stars) FROM review);
'''

query_3 = '''
SELECT ramen.variety, brand.brand_name, review.stars
FROM ramen JOIN brand
ON ramen.brand_name = brand.brand_name
JOIN review
ON ramen.review_id = review.review_id
ORDER BY review.stars DESC;
'''

conn = psycopg2.connect(user=username, password=password, dbname=database, host=host, port=port)

with conn:
    figure, (bar_ax, pie_ax, graph_ax) = plt.subplots(1, 3, figsize=(20, 12))
    plt.subplots_adjust(wspace=1)
    cur = conn.cursor()

    cur.execute(query_3)
    grade = []
    variety = []
    brand = []
    for row in cur:
        variety.append(row[0])
        brand.append(row[1])
        grade.append(row[2])
    
    bar_ax.bar(variety, grade)
    bar_ax.set_xticklabels(variety, rotation=45, ha = 'right', fontsize = 5)
    bar_ax.set_xlabel('Різновид Рамену')
    bar_ax.set_ylabel('Оцінка')
    bar_ax.set_title('Різновиди Рамену за зменшенням оцінки')
    

    cur.execute(query_2)

    grade = []
    variety = []
    for row in cur:
        variety.append(row[0])
        grade.append(row[1])

    grade_1 = grade + ['']
    grade.append(5 - grade[0])
    pie_ax.pie(grade, labels = grade_1, colors = plt.cm.Set3.colors)
    pie_ax.text(-1.75, -2, variety[0])
    pie_ax.set_title ("Максимальна оцінка Рамену з 5")

    cur.execute(query_1)

    grade = []
    variety = []
    for row in cur:
        grade.append(row[0])
        variety.append(row[1])

    graph_ax.plot(variety, grade, marker ='o')
    graph_ax.set_xlabel('Різновид Рамену')
    graph_ax.set_ylabel('Оцінка')
    graph_ax.set_title('Оцінки Рамену бренду Wei Wei')
    
   
mng = plt.get_current_fig_manager()
mng.resize(1400, 600)

plt.show()