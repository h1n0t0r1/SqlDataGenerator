from datetime import date, timedelta
from random import randint
import csv
import psycopg2



start_date = date(1942, 1, 1)
end_date = date(2022, 1, 1)

all_dates = [start_date]

while start_date != end_date:
    start_date += timedelta(days=1)
    all_dates.append(start_date)

male_names = list(csv.reader(open('male_names.csv'), delimiter=','))
female_names = list(csv.reader(open('female_names.csv'), delimiter=','))
last_names = list(csv.reader(open('last_names.csv'), delimiter=','))


con = psycopg2.connect(
    host='localhost',
    database='losa',
    user='postgres',
    password='244466666'
)

cur = con.cursor()

for i in range(0, 10000):
    print(i)
    query = '''INSERT INTO people(first_name, last_name, birthday) VALUES '''
    for j in range(0, 10000):
        new_date = all_dates[randint(0, len(all_dates) - 1)].strftime('%Y-%m-%d')
        is_male = randint(0, 1)
        if is_male:
            first_name = male_names[randint(0, len(male_names) - 1)][1]
        else:
            first_name = female_names[randint(0, len(female_names) - 1)][1]

        last_name = last_names[randint(0, len(last_names) - 1)][1]

        output = f'''('{first_name}', '{last_name}', '{new_date}'),'''
        query += output
    query = query[:-1]
    cur.execute(query)
    con.commit()

con.close()
