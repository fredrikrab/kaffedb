from datetime import datetime
from helpFunctions import clear_terminal, get_int_user_input, print_table


class CreateReview:
    """Lets the user create a single coffee review and submits it to the database.
    """
    def __init__(self, user_email='default@email.com', date_time = datetime.now()):
        """Set initial values.
        Args:
            user_email (str, optional): Email address of user. Defaults to 'default@email.com'.
            date_time (datetime, optional): Time of tasting. Defaults to datetime.now().
        """
        self.__user_email = user_email
        self.__coffee_id = None
        self.__coffee_name = None
        self.__roastery = None
        self.__date_time = date_time
        self.__rating = None
        self.__note = None
        self.__completed = False

    
    def print_overview(self):
        clear_terminal()
        print("Post kaffesmaking\n\n" \
            f"{'Kaffe': <8} {'<not set>' if self.__coffee_name==None else self.__coffee_name} {'' if self.__roastery==None else 'by ' + self.__roastery}\n" \
            f"{'Rating': <8} {'<not set>' if self.__rating==None else self.__rating}\n" \
            f"{'Notat': <8} {'<not set>' if self.__note==None else self.__note} \n")
    
    
    def select_coffee(self, dbi, row_count=10):
        """User selects which coffee to review.

        Args:
            dbi (DBI): Active instance of database interface
            row_count (int, optional): Max number of coffees to list. Defaults to 10.
        """
        
        sql = "SELECT coffee_id, roastery_name, coffee_name FROM coffee LIMIT 10;"
        coffee_lst = dbi.execute_with_row_factory(sql).fetchmany(row_count)
        print_table(coffee_lst, column_titles=['ID', 'Brenneri', 'Kaffe'])

        print("\nVelg kaffe:", end="")
        selection = get_int_user_input(1, row_count)
        self.__coffee_id = coffee_lst[selection-1]['coffee_id']
        self.__coffee_name = coffee_lst[selection-1]['coffee_name']
        self.__roastery = coffee_lst[selection-1]['roastery_name']


    def set_rating(self):
        """User provides rating of coffee.
        """
        print("Rating:", end="")
        self.__rating = get_int_user_input(0, 10)


    def write_note(self):
        """User writes optional note.
        """
        note = input("Smaksnotat: ")
        self.__note = note
    
    
    def edit_review(self, dbi):
        """Menu to let user edit any part of the review before posting it.

        Args:
            dbi (DBI): Active instance of database interface
        """
        self.print_overview()
        print("Hva vil du endre?\n\n" \
            "1. Kaffetype\n" \
            "2. Rating\n" \
            "3. Smaksnotat\n")
        
        print("Valg:", end="")        
        user_input = get_int_user_input(1, 3)
        
        if user_input == 1: self.select_coffee(dbi)
        if user_input == 2: self.set_rating()
        if user_input == 3: self.write_note()
    
    
    def post_review(self, dbi):
        """Post review to database.

        Args:
            dbi (DBI): Instance of our database interface
        """
        sql = "INSERT INTO reviews VALUES(null, :user_email, :coffee_id, :date_time, :rating, :note);"
        obj = {"user_email": self.__user_email,
               "coffee_id": self.__coffee_id,
               "date_time": self.__date_time,
               "rating": self.__rating,
               "note": self.__note}
        dbi.execute(sql, obj)
        dbi.commit()
        
        self.__completed = True
        # print(obj)  # useful for debugging
        print("Suksess!")

    
    def confirm_review(self, dbi):
        """Menu asking user to confirm or edit review before posting it.

        Args:
            dbi (DBI): Active instance of database interface
        """
        self.print_overview()
        print("1. Post kaffesmaking\n" \
            "2. Gjør en endring\n" \
            "3. Avbryt\n")
        
        print("Valg:", end="")        
        user_input = get_int_user_input(1,3)
        
        if user_input == 1: self.post_review(dbi)
        if user_input == 2: self.edit_review(dbi)
        if user_input == 3: quit
    
    
    def is_completed(self):
        """Helper function which enables menu options to loop until the review is finished.

        Returns:
            bool: True if review is completed, False otherwise.
        """
        return self.__completed
