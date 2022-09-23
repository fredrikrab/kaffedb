from helpFunctions import get_int_user_input, print_table, clear_terminal

""" 
TODO:
- Docstrings
- Login by typing email
- Handle invalid input
- Handle unexpected result of SQL query
"""

class User:
    
    def __init__(self, user_email=None):
        self.__user_email = None
        self.__name = None
        self.__country = None
        
        if user_email:
            self.login_with_email(user_email)

    def is_logged_in(self):
        return False if self.__user_email is None else True
    
    def get_name(self):
        return self.__name
    
    def get_country(self):
        return self.__country
    
    def get_email(self):
        return self.__user_email

    def login_with_email(self, dbi, email=None):
        if not email:
            # Ask user to type email
            pass
        
        sql = f"SELECT * FROM users WHERE user_email='{email}'"
        user = dbi.execute_with_row_factory(sql).fetchone()
        
        self.__user_email = user['user_email']
        self.__name = user['user_name']
        self.__country = user['user_country']

        
    
    def login_from_list(self, dbi, max_rows=10):
        sql = "SELECT user_name, user_email FROM users LIMIT 10;"
        user_lst = dbi.execute_with_row_factory(sql).fetchmany(max_rows)
        row_count = len(user_lst)
        print_table(user_lst, column_titles=['ID', 'Navn', 'Epost-adresse'], showindex=[i for i in range(1, row_count+1)])
        
        print("\n Velg bruker:", end="")
        selection=get_int_user_input(1, row_count)
        
        self.login_with_email(dbi, user_lst[selection-1]['user_email'])

    def userStatistics(self, dbi):
        clear_terminal()

        print(f"Select statistic\n\n" \
            "1. Antall kaffer smakt\n" \
            "2. Mest drukket kaffe\n" \
            "3. Mest likte kaffe\n")

        selection = input("Velg: ")


        if(selection == "1"):
            clear_terminal()
            print_table( 
                        dbi.execute('''SELECT COUNT (*)
                        FROM reviews
                        WHERE user_email=?;''', (self.get_email(),)),
                        ['Antall'])
        
        elif(selection == "2"):
            clear_terminal()
            print_table( 
                        dbi.execute('''SELECT coffee_name, COUNT (*)
                        FROM coffee NATURAL JOIN reviews
                        WHERE user_email=?
                        GROUP BY coffee_id
                        ORDER BY COUNT(*) DESC;''', (self.get_email(),)),
                        ['Kaffe navn', 'Antall drukket'])
        
        elif(selection == "3"):
            clear_terminal()
            print_table( 
                        dbi.execute('''SELECT coffee_name, MAX(rating)
                        FROM coffee NATURAL JOIN reviews
                        WHERE user_email=?
                        GROUP BY coffee_name
                        ORDER BY MAX(Rating) DESC;''', (self.get_email(),)),
                        ['Kaffe navn', 'Rating'])

