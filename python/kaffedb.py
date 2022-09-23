import sqlite3

# Configuration
db_file = 'kaffe.db'
sql_script = '../sql/create_tables.sql'
sql_data = '../sql/insert_data.sql'
delete_old_db = True
populate = True

# Connect to db
con = sqlite3.connect(db_file)
cur = con.cursor()

# Generate tables from sql script
try:
    f = open(sql_script, 'r', encoding='utf8')
    cur.executescript(f.read())
    f.close()
except Exception as error:
    print(type(error), error)

# pre-populate db
if populate:
    try:
        f = open(sql_data, 'r', encoding='utf8')
        cur.executescript(f.read())
        f.close()
    except Exception as error:
        print(type(error), error)


# user writes to db
def entry(roastery, coffee_name, rating, note):
    cur.execute('''
        SELECT coffee_id
        FROM coffee
        WHERE roastery_fk = ? AND coffee_name = ?
        ''', (roastery,coffee_name,)
    )
    coffee_id = cur.fetchone()[0]

    cur.execute(
        '''
        INSERT INTO reviews (review_id, user_fk, coffee_fk, datetime, note, rating)
        VALUES(null, 'epost@server.no', ?, '2022-01-01', ?, ?);
        ''', (coffee_id, note, rating)
    )
    con.commit()

# Close db connection
con.close()
