import psycopg2

# conn = psycopg2.connect('dbname=zayandb')
conn = psycopg2.connect('dbname=example2')

cur = conn.cursor()

cur.execute('DROP TABLE IF EXISTS table1')

cur.execute('''
    CREATE TABLE table1 (
        id INTEGER PRIMARY KEY,
        description VARCHAR NOT NULL,
        completed BOOLEAN NOT NULL DEFAULT False
    );
''')

cur.execute('INSERT INTO table1 (id, description, completed) VALUES (1, \'this is the first recored\', true);')

cur.execute('INSERT INTO table1 (id, description) VALUES (2, \'this is the second recored\');')

cur.execute('INSERT INTO table1 (id, description, completed) VALUES (%s, %s, %s);', (3, 'this is the third recored', True))

insertQuery = 'INSERT INTO table1 (id, description, completed) VALUES (%(id)s, %(description)s, %(completed)s);'
data = {
    'id': 4,
    'description': 'this is the forth recored',
    'completed': False
}

cur.execute(insertQuery, data)

insertQuery2 = 'INSERT INTO table1 (id, description, completed) VALUES (%(id)s, %(desc)s, %(comp)s);'
data2 = {
    'id': 5,
    'desc': 'this is the fifth recored',
    'comp': False
}

cur.execute(insertQuery2, data2)

cur.execute('INSERT INTO table1 (id, description, completed) VALUES (%s, %s, %s);', (6, 'this is the sixth recored', True))

cur.execute('SELECT * FROM table1;')

conn.commit()

result1 = cur.fetchone()
print('fetchone', result1)

result2 = cur.fetchmany(2)
print('fetchmany', result2)

result = cur.fetchall()
print('fetchall', result)

cur.close()
conn.close()