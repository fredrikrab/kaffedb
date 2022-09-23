import sqlite3
db_file = '../kaffe.db'

class ConnectionCtrl:

    @staticmethod
    def execute(sql:str, obj=None):
        with sqlite3.connect(db_file) as con:
            return con.cursor().execute(sql, obj) if obj else con.cursor().execute(sql)
    
    @staticmethod
    def fetch_all(sql:str):
        with sqlite3.connect(db_file) as con:
            return con.cursor().execute(sql).fetchall()
    
    @staticmethod
    def fetch_row_factory(sql:str):
        # See https://docs.python.org/3/library/sqlite3.html#sqlite3.Row
        with sqlite3.connect(db_file) as con:
            con.row_factory = sqlite3.Row
            return con.cursor().execute(sql).fetchall()


    @staticmethod
    def commit():
        with sqlite3.connect(db_file) as con:
            return con.commit()

    @staticmethod
    def getMostTasted():
        with sqlite3.connect(db_file) as con:
            return (con.cursor().execute('''SELECT user_name, count(*)
                    FROM (SELECT DISTINCT user_email, coffee_id
                            FROM reviews
                            WHERE date_time >= datetime('now', 'start of year')
                         )
                    JOIN users USING(user_email)
                    GROUP BY user_email
                    ORDER BY count(*) DESC;''').fetchall()
                    )
    
    @staticmethod
    def getBestValue():
        with sqlite3.connect(db_file) as con:
            return(con.cursor().execute('''SELECT roastery_name, coffee_name, kilo_price_nok, AVG(rating)
                                 FROM (SELECT rating, coffee_id FROM reviews)
                                 JOIN coffee USING(coffee_id)
                                 GROUP BY coffee_id
                                 ORDER BY AVG(rating)/kilo_price_nok DESC;''').fetchall()
                    )

    @staticmethod
    def get_users():
        with sqlite3.connect(db_file) as con:
            return con.cursor().execute('select * from users').fetchall()

    
