from django.db import connection


def insert(table, kargs):
    with connection.cursor() as conn:
        conn.execute(f'''
            Insert into {table}
            {kargs}
        ''')


def update(table, kargs, where):
    with connection.cursor() as conn:
        conn.execute(f'''
            Update {table} 
            Set {kargs}
            where {where}
        ''')


def drop(table, kargs):
    with connection.cursor() as conn:
        conn.execute(f'''
            drop from {table} where {kargs}
        ''')


def select(table, kargs):
    with connection.cursor() as conn:
        result = conn.execute(f'''
            select * from {table} where {kargs}
        ''')
        return result
