from django.core.management.base import BaseCommand
import sqlite3
import csv
import os

from api_yamdb.settings import BASE_DIR

PATH_DIR = os.path.join(BASE_DIR, 'static/data')

PATH_TO_BD = '../api_yamdb/db.sqlite3'

CONFORMITY = {
    'category': 'reviews_category',
    'comments': 'reviews_comment',
    'genre': 'reviews_genre',
    'title_genre': 'reviews_title_genre',
    'review': 'reviews_review',
    'titles': 'reviews_title',
    'users': 'user_user'
}


class Command(BaseCommand):
    help = 'Data import...........'

    def handle(self, *args, **options):
        con = sqlite3.connect(PATH_TO_BD)
        cur = con.cursor()

        for file in os.listdir(PATH_DIR):
            PATH_TO_FILE = os.path.join(PATH_DIR, file)
            table_name = CONFORMITY[os.path.splitext(os.path.basename(file))[0]]

            with open(PATH_TO_FILE, 'r', encoding='utf-8') as f_open_csv:
                rows = csv.DictReader(f_open_csv)

                for row in rows:
                    columns = ', '.join(row.keys())
                    placeholders = ', '.join('?' * len(row))
                    sql = 'INSERT INTO {} ({}) VALUES ({})'.format(table_name, columns, placeholders)
                    values = [int(x) if x.isnumeric() else x for x in row.values()]
                    cur.execute(sql, values)

        con.commit()
        con.close()
        print()
        print()
        print('The data from .csv-files are imported.')
        print('======================================')
        print()
