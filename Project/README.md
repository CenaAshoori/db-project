# Connect `Django` Project to `PostgreSQL`

## 1 - Install `django`, `psycopg2`

```bash
pip install django
```
```bash
pip install psycopg2
```

After installing these requirements, you need to connect Django project to the new database.

## 2 - Create Database and Insert Data
  In `postgres` in query tools run this command:
```sql
DROP DATABASE IF EXISTS "Ashoori_97149068";
CREATE DATABASE "Ashoori_97149068"
    WITH 
    OWNER = postgres
    ENCODING = 'UTF8'
    LC_COLLATE = 'English_United States.1252'
    LC_CTYPE = 'English_United States.1252'
    TABLESPACE = pg_default
    CONNECTION LIMIT = -1;
```
and then with opening `"Query tools"` of `Ashoori_97149068`'s database run all the create and insert query in `+create_and_data.sql"`.

---
## 3 - Set `username` and `password` in **`setting.py`**
Into the ` config > setting.py` and to the ` DATABASE ` section, set the database config like this format:

**you need to change the `<<username>>` and `<<password>>` of this section to your own information**

```python

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'Ashoori_97149068',
        'OPTIONS': {
        'options': '-c search_path=public'
    },
        'USER': '<<username>>',
        'PASSWORD': '<<password>>',
        'HOST': 'localhost',
        'PORT': '',
    }
}

```
---
After doing above steps Django is connected to the database.

## 4- Adding requirement tables for `log in` to the `Django-admin`:
by running `migrate` command `django` automatically create its requirements table into database:
```python
python manage.py migrate
```
**Now** the Django’s requirement tables are created and we should create a **`superuser`**
to can `Log in` to the `Django admin`:
```
python manage.py createsuperuser
```
and fill the requirement with fake info. and then log in with that info. 

# Explain Queries
### All Queries Are in `all > admin.py`
1 - `SELECT` all Student that their `mark` >= 10:
```sql
Participated.objects.raw("""
                            SELECT stu_id
                            FROM participated 
                            WHERE mark >= 10
                            """
                            )
```

2 - `SELECT` all Student that their `mark` < 10:
```sql
Participated.objects.raw("""
                            SELECT stu_id
                            FROM participated 
                            WHERE mark < 10
                            """
                            )
```

3 - `SELECT` all Student that their `balance` > 70:
We should get `balance` from `Students` table so we should 
join `participated` and `students` to get access `balance`:
```sol
Participated.objects.raw("""
                            SELECT stu_id
                            FROM participated 
                            natural join students
                            WHERE balance > 70
                            """
                            )
```
4 - `UPDATE` Mark in `Participated` table:
```sql
with connection.cursor() as c:
            c.execute("""
            UPDATE participated
            SET mark = 9.99
            WHERE mark IS NOT NULL 
                AND mark < 10
            """)

```

5 - `UPDATE` Mark in `Participated` table:
```sql
with connection.cursor() as c:
            c.execute("""
            UPDATE participated
            SET mark = mark + 1
            WHERE mark BETWEEN 10 AND 19
            """)

```

 6 - `SELECT` username of `Students` table:
```python
def sql_username(self, obj):
        p = Students.objects.raw(f"""
        SELECT *
        FROM students
        Where stu_id = '{obj.stu_id}'
        limit 1
        """)[0]
        return f"{p.username}"
```

### In `admin.py` also you can see more similar example.

|Full Name|Student Number|
|---|---|
|Mohammad Hosein Ashoori|97149068|



