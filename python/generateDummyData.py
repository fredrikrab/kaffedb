import os
import sqlite3
from enum import Enum
from mimesis import Datetime, Field, Schema, random
from mimesis.locales import Locale

class GenerateData:
    def __init__(self):
        self.__db_file = 'kaffe.db'
        self.__sql_create_tables = './sql/create_tables.sql'
        self.__con = sqlite3.connect(self.__db_file)
        self.__cur = self.__con.cursor()
        self.__field = Field(Locale.NO)
        self.__datetime = Datetime(Locale.NO).datetime
    
    def __insert(self, sql, obj=None):
        try:
            self.__cur.execute(sql, obj) if obj else self.__cur.execute(sql)
        except sqlite3.IntegrityError as e:
            if str(e).startswith('UNIQUE constraint failed:'):
                pass
            else:
                print(e)
    
    def __sql_select_random(self, column, table):
        return f"SELECT {column} FROM {table} LIMIT 1 OFFSET ABS(RANDOM()) % MAX((SELECT COUNT(*) FROM {table}), 1)"
    
    def __insert_static_data(self):
        self.__cur.execute("INSERT INTO coffee_beans VALUES('arabica')")
        self.__cur.execute("INSERT INTO coffee_beans VALUES('robusta')")
        self.__cur.execute("INSERT INTO coffee_beans VALUES('liberica')")
    
    def __populate_users(self, rows=30):   
        fields = Schema(
        schema=lambda: {
            "user_email": self.__field("email"),   # can set unique=True; gives uglier addresses, conflicts appears unlikely
            "password": self.__field("password"),
            "user_name": self.__field("full_name"),
            "user_country": self.__field("country")}
        )
        sql =  "INSERT INTO users VALUES(:user_email, :password, :user_name, :user_country);"
        for f in fields.iterator(rows):
            self.__insert(sql, f)
        
    def __populate_farms(self, rows=10):
        fields = Schema(
        schema=lambda: {
            "farm_name": self.__field("company"),
            "elevation": self.__field("integer_number", start=0, end=4000),
            "farm_country": self.__field("country"),
            "region": self.__field("city")}
        )
        sql = "INSERT INTO farms VALUES(:farm_name, :elevation, :farm_country, :region);"
        for f in fields.iterator(rows):
            self.__insert(sql, f)
        
        sql = f'''
        INSERT INTO farm_cultivate_beans VALUES(
            ({self.__sql_select_random('farm_name', 'farms')}),
            ({self.__sql_select_random('bean_type', 'coffee_beans')})
        );
        '''
        for f in range(rows*4):
            self.__insert(sql)

    def __populate_roasteries(self, rows=20):
        fields = Schema(
            schema=lambda: {
                "roastery_name": self.__field("company")}
        )
        sql = "INSERT INTO roasteries VALUES(:roastery_name);"
        for f in fields.iterator(rows):
            self.__insert(sql, f)
    
    def __populate_refinement_methods(self, rows=5):
        fields = Schema(
            schema=lambda: {
                "refinement_name": self.__field("spices"),
                "refinement_description": self.__field("sentence")}
        )
        sql = "INSERT INTO refinement_methods VALUES(:refinement_name, :refinement_description);"
        for f in fields.iterator(rows):
            self.__insert(sql, f)

    def __populate_batches(self, rows=100):
        fields = Schema(
            schema=lambda: {
                "coffee_id": self.__field("increment"),
                "harvest_year": self.__field("year", minimum=2015, maximum=2022),
                "kilo_price_usd": self.__field("float_number", start=1, end=15, precision=2)}
        )
        sql = f'''INSERT INTO batches VALUES(
                    null, :coffee_id,
                    ({self.__sql_select_random('roastery_name', 'roasteries')}),
                    ({self.__sql_select_random('farm_name', 'farms')}),
                    ({self.__sql_select_random('refinement_name', 'refinement_methods')}),
                    :harvest_year, :kilo_price_usd
                );'''
        for f in fields.iterator(rows):
            self.__insert(sql, f)
    
    def __populate_coffees(self, rows=100):
        class roast_degree(Enum):
            dark = "mørk",
            medium = "middels",
            light = "lys",

        fields = Schema(
            schema=lambda: {
                "coffee_id": self.__field("increment"),
                "coffee_name": self.__field("fruit") + " " + self.__field("spices"),
                "coffee_description": self.__field("sentence"),
                "kilo_price_nok": self.__field("float_number", start=100, end=1000, precision=2),
                "roast_degree": str(random.get_random_item(roast_degree).value[0]),
                "roast_date": self.__datetime(start=2015, end=2022)}
        )
        sql = f'''INSERT INTO coffee VALUES(
                    null, :coffee_name, :coffee_description, :kilo_price_nok,
                    :roast_degree, :roast_date, ({self.__sql_select_random('roastery_name', 'roasteries')})
            );'''
        for f in fields.iterator(rows):
            self.__insert(sql, f)

    def __populate_reviews(self, rows=1000):
        fields = Schema(
            schema=lambda: {
                "review_id": self.__field("increment"),
                "date_time": self.__datetime(start=2015, end=2022),
                "rating": self.__field("integer_number", start=0, end=10),
                "note": self.__field("sentence")}
        )
        sql = f'''INSERT INTO reviews VALUES(
                    null,
                    ({self.__sql_select_random('user_email', 'users')}),
                    ({self.__sql_select_random('coffee_id', 'coffee')}),
                    :date_time, :rating, :note
            );'''
        for f in fields.iterator(rows):
            self.__insert(sql, f)
    
    def delete_current_db(self):
        if os.path.exists(self.__db_file):
            os.remove(self.__db_file)
    
    def create_empty_db(self):
        with open(self.__sql_create_tables) as f, sqlite3.connect(self.__db_file) as con:
            con.cursor().executescript(f.read())
        self.__con = sqlite3.connect(self.__db_file)
        self.__cur = self.__con.cursor()
    
    def populate_db(self):
        self.__insert_static_data()
        self.__populate_users(rows=500)
        self.__populate_farms(rows=150)
        self.__populate_roasteries(rows=300)
        self.__populate_refinement_methods(rows=50)
        self.__populate_batches(rows=5000)
        self.__populate_coffees(rows=5000)
        self.__populate_reviews(rows=20000)
        self.__con.commit()