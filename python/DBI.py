import sqlite3
from helpFunctions import clear_terminal, print_table


class DBI:
    """Implements the sqlite3 database interface
    """
    
    def __init__(self, db='../kaffe.db'):
        """Start by creating the SQLite database connection object
        """
        self.con = sqlite3.connect(db)

    
    def execute(self, query:str, object:dict=None, row_factory:bool=False):
        """Interface for sqlite3.Cursor.execute
        https://docs.python.org/3/library/sqlite3.html#sqlite3.Cursor.execute

        Args:
            query (str): Complete SQL statement, potentially with bound placeholders.
            object (dict, optional): Named style substititon of placeholders.

        Returns:
            sqlite3.Cursor: An sqlite3.Cursor instance.
            See documentation for attributes and methods
            https://docs.python.org/3/library/sqlite3.html#sqlite3.Cursor
        """
        if object:
            return self.con.cursor().execute(query, object)
        else:
            return self.con.cursor().execute(query)

    
    def execute_with_row_factory(self, query:str):
        """Similar as above while also setting: sqlite3.connection.row_factory = sqlite3.Row
        https://docs.python.org/3/library/sqlite3.html#sqlite3.Connection.row_factory

        Args:
            query (str): Complete SQL statements.

        Returns:
            sqlite3.Cursor: An sqlite3.Cursor instance.
        """
        with self.con as con:
            con.row_factory = sqlite3.Row
            return con.cursor().execute(query)
    
    
    def commit(self):
        """Commits the current transaction.

        Returns:
            _type_: _description_ #TODO
        """
        return self.con.commit()

    
    def close(self):
        """Close database connection.

        Returns:
            _type_: _description_ #TODO
        """
        return self.con.close()

    def validate(self, query, object):
        return len(list(self.con.execute(query, object)))


    def __del__(self):
        """Safe cleanup method for when object is garbage collected.
        """
        self.commit()
        self.close()


    def statistics(self):
        print(f"Select statistic\n\n" \
            "1. Top drinkers\n" \
            "2. Best value\n"
            "3. Most common bean type\n"
            "4. Total payment to farms\n"
            "5. Most common refinement method\n"
            "6. Mest poppulære kaffe\n"
            "7. Mest vellikte brennerier\n")

        selection = input("Select option: ")

        if(selection == "1"):
            clear_terminal()
            print_table( 
                        self.execute('''SELECT user_name, count(*)
                        FROM (SELECT DISTINCT user_email, coffee_id
                            FROM reviews
                            WHERE date_time >= datetime('now', 'start of year')
                            )
                        JOIN users USING(user_email)
                        GROUP BY user_email
                        ORDER BY count(*) DESC;''').fetchall(),
                        ["user_name", 'Count'],)
            return

        elif(selection == "2"):
            clear_terminal()
            print_table(
                        self.execute('''SELECT roastery_name, coffee_name, kilo_price_nok, AVG(rating)
                        FROM (SELECT rating, coffee_id FROM reviews)
                        JOIN coffee USING(coffee_id)
                        GROUP BY coffee_id
                        ORDER BY AVG(rating)/kilo_price_nok DESC;''').fetchall(),
                        ['Roastery name', 'Coffee name', 'Kilo price(NOK)', 'Rating'])
            return
    
        elif(selection == "3"):
            clear_terminal()
            print_table( 
                        self.execute('''SELECT bean_type, COUNT (*)
                        FROM batches NATURAL JOIN beans_in_batch NATURAL JOIN coffee_beans
                        GROUP BY bean_type
                        ORDER BY COUNT(*) DESC;'''),
                        ['Bean type', "Number of occurrences"])

        elif(selection == "4"):
            clear_terminal()
            print_table( 
                        self.execute('''SELECT farm_name, SUM(kilo_price_usd)
                        FROM batches NATURAL JOIN farms
                        GROUP BY farm_name
                        ORDER BY SUM(kilo_price_usd) DESC;'''),
                        ['Farm name', "Payment(USD)"])

        elif(selection == "5"):
            clear_terminal()
            print_table( 
                        self.execute('''SELECT refinement_name, COUNT(*)
                        FROM batches NATURAL JOIN refinement_methods
                        GROUP BY refinement_name
                        ORDER BY COUNT(*) DESC;'''),
                        ['Refinement method', "Count"])

        elif(selection == "6"):
            clear_terminal()
            print_table( 
                        self.execute('''SELECT coffee_name, AVG(rating)
                        FROM coffee NATURAL JOIN reviews
                        GROUP BY coffee_name
                        ORDER BY AVG(rating) DESC;'''),
                        ['Kaffe navn', "Gj.snitt rating"])

        
        elif(selection == "7"):
            clear_terminal()
            print_table( 
                        self.execute('''SELECT roastery_name, COALESCE((AVG(rating)/COUNT(DISTINCT coffee_name)), 0) as made
                        FROM coffee LEFT JOIN reviews USING(coffee_id)
                        GROUP BY roastery_name
                        ORDER BY made DESC;'''),
                        ['Brenneri navn', "Gj.snitt rating"])

        elif(selection == "q"):
            return
        else:
            self.statistics()
