from helpFunctions import clear_terminal, get_int_user_input, print_table
from DBI import DBI
dbi = DBI()

class Search:
    menu = {
        "Kaffetyper" : ["Navn", "Beskrivelse", "Brenningsgrad"],
        "Smaksnotat": ["Rating", "Notat", "Dato"],
        "Brenneri": ["Navn"],
        "Gård": ["Navn", "Land", "Region", "Høyde"],
        "Kaffebønne": ["Type"],
        "Foredlingsmetode": ["Navn", "Beskrivelse"]
    }
    main_menu = {"Meny": list(menu.keys())}
    db = {
        "Kaffetyper" : "coffee",
        "Smaksnotat": "reviews",
        "Brenneri": "roasteries",
        "Gård": "farms",
        "Kaffebønne": "coffee_beans",
        "Foredlingsmetode": "refinement_methods"
    }
    
    def __init__(self):
        self.__sql = "SELECT roastery_name, coffee_name FROM "
        self.__selection = {}
        self.__completed = False
        
        
    def print_overview(self):
        """Prints a table with all possible search/filter criterias.
        """
        
        clear_terminal()
        print("Du kan velge blant følgende søkekriterier:\n\n")
        print_table(self.menu, column_titles="keys", tablefmt="presto")
        
        
    def print_options(self, option_dictionary):
        """ User makes a selection for which table/column the search should be performed in.
        """
        
        row_count = len(list(option_dictionary.values())[0])
        print_table(option_dictionary, column_titles="keys", showindex=[i for i in range(1, row_count+1)], tablefmt="presto")
        
        print("\nValg: ", end="")
        selection = get_int_user_input(1, row_count)
        
        return selection
    
    
    def search_menu(self):
        self.print_overview()
        
        # Select table
        print("\nFørst velg hovedmeny\n\n")
        selection = self.print_options(self.main_menu)
        table = self.main_menu["Meny"][selection-1]
        
        self.print_overview()
        
        # Select column
        print("\nVelg søkefelt\n\n")
        options_dictionary = { table : self.menu[table]}
        selection = self.print_options(options_dictionary)
        column = options_dictionary[table][selection-1]
        
        self.__selection[table] = column

        if table == list(self.menu.keys())[0]:
            self.filter_by_coffee(table, column)
            
        elif table == list(self.menu.keys())[1]:
            self.filter_by_review(table, column)
        
        elif table == list(self.menu.keys())[2]:
            self.filter_by_roastery(table, column)
        
        elif table == list(self.menu.keys())[3]:
            self.filter_by_farm(table, column)
        
        elif table == list(self.menu.keys())[4]:
            self.filter_by_coffee_bean(table, column)
        
        elif table == list(self.menu.keys())[5]:
            self.filter_by_refinement_method(table, column)


    def print_matching_coffees(self, query_result, column_titles=['Brenneri', 'Kaffe']):
        print_table(query_result, column_titles=column_titles)


    def string_query(self, sql, row_count=10):
        return dbi.execute_with_row_factory(sql).fetchmany(row_count)
    
    
    def extend_search(self):
        print("Ønsker du å utvide søket?\n\n" \
            "1. Nei, avslutt.\n" \
            "2. Ja, slå dette søket sammen med et annet (UNION)\n" \
            "3. Ja, kombiner dette søket med et annet (INTERSECT)\n\n")
        
        print("\nValg: ", end="")
        selection = get_int_user_input(1, 3)
        
        if selection == 1:
            self.__completed = True
            return
        if selection == 2:
            self.__sql += " UNION SELECT roastery_name, coffee_name FROM "
            self.search_menu()
        if selection == 3:
            self.__sql += "INTERSECT SELECT roastery_name, coffee_name FROM "
            self.search_menu()
    
    def filter_by_coffee(self, table, column):
        col = {
            "Navn":"coffee_name",
            "Beskrivelse":"coffee_description",
            "Brenningsgrad":"roast_degree"
        }
        
        print("\nFlere søkeord kan adskilles med komma (og mellomrom). Skriv NOT foran ord du vil utelukke.\n")
        keyword = input(f"{column}: ")
        
        if "," in keyword:
            self.__sql += f"""{self.db[table]} WHERE {col[column]} LIKE '%{keyword.split(",")[0]}%'"""
            for word in keyword.split(", ")[1:]:
                self.__sql += f" OR {col[column]} LIKE '%{word}%'"
        else:
            self.__sql += f"{self.db[table]} WHERE {col[column]} LIKE '%{keyword}%'"
        
        result = self.string_query(self.__sql)
        self.print_matching_coffees(result)
        self.extend_search()

    def filter_by_review(self, table, column):
        col = {
            "Rating":"rating",
            "Notat":"note",
            "Dato":"date_time"
        }
        
        #TODO: Rating and date
        print("\nFlere søkeord kan adskilles med komma (og mellomrom). Skriv NOT foran ord du vil utelukke.\n")
        keyword = input(f"{column}: ")
        
        if "," in keyword:
            table_sql = f"""(SELECT coffee_id FROM {self.db[table]} WHERE {col[column]} LIKE '%{keyword.split(", ")[0]}%'"""
            for word in keyword.split(", ")[1:]:
                table_sql += f" OR {col[column]} LIKE '%{word}%'"
            table_sql += ")"
        else:
            table_sql = f"(SELECT coffee_id FROM {self.db[table]} WHERE {col[column]} LIKE '%{keyword}%')"
            
        self.__sql += f"{table_sql} NATURAL JOIN coffee"
        result = self.string_query(self.__sql)
        self.print_matching_coffees(result)
        self.extend_search()
        
    def filter_by_roastery(self, table, column):
        col = {
            "Navn":"roastery_name"
        }
        
        print("\nFlere søkeord kan adskilles med komma (og mellomrom). Skriv NOT foran ord du vil utelukke.\n")
        keyword = input(f"{column}: ")
        
        if "," in keyword:
            self.__sql += f"""coffee WHERE {col[column]} LIKE '%{keyword.split(",")[0]}%'"""
            for word in keyword.split(", ")[1:]:
                self.__sql += f" OR {col[column]} LIKE '%{word}%'"
        else:
            self.__sql += f"coffee WHERE {col[column]} LIKE '%{keyword}%'"
        
        self.__sql += f"coffee WHERE {col[column]} LIKE '%{keyword}%'"
        result = self.string_query(self.__sql)
        self.print_matching_coffees(result)
        self.extend_search()
    
    def filter_by_farm(self, table, column):
        col = {
            "Navn":"farm_name",
            "Land":"farm_country",
            "Region":"region",
            "Høyde":"elevation"
        }
        
        #TODO: Elevation
        print("\nFlere søkeord kan adskilles med komma (og mellomrom). Skriv NOT foran ord du vil utelukke.\n")
        keyword = input(f"{column}: ")
        
        if "," in keyword:
            table_sql = f"""(SELECT farm_name FROM {self.db[table]} WHERE {col[column]} LIKE '%{keyword.split(", ")[0]}%'"""
            for word in keyword.split(", ")[1:]:
                table_sql += f" OR {col[column]} LIKE '%{word}%'"
            table_sql += ")"
        else:
            table_sql = f"(SELECT farm_name FROM {self.db[table]} WHERE {col[column]} LIKE '%{keyword}%')"
        
        self.__sql += f"{table_sql} NATURAL JOIN batches NATURAL JOIN coffee"
        result = self.string_query(self.__sql)
        self.print_matching_coffees(result)
        self.extend_search()
        
    def filter_by_coffee_bean(self, table, column):
        col = {
            "Type":"bean_type"
        }
        
        print("\nFlere søkeord kan adskilles med komma (og mellomrom). Skriv NOT foran ord du vil utelukke.\n")
        keyword = input(f"{column}: ")
        
        if "," in keyword:
            table_sql = f"""(SELECT bean_type FROM {self.db[table]} WHERE {col[column]} LIKE '%{keyword.split(", ")[0]}%'"""
            for word in keyword.split(", ")[1:]:
                table_sql += f" OR {col[column]} LIKE '%{word}%'"
            table_sql += ")"
        else:
            table_sql = f"(SELECT bean_type FROM {self.db[table]} WHERE {col[column]} LIKE '%{keyword}%')"
        
        self.__sql += f"{table_sql} NATURAL JOIN beans_in_batch NATURAL JOIN batches NATURAL JOIN coffee"
        result = self.string_query(self.__sql)
        self.print_matching_coffees(result)
        self.extend_search()
    
    def filter_by_refinement_method(self, table, column):
        col = {
            "Navn":"refinement_name",
            "Beskrivelse":"refinement_description"
        }
        
        print("\nFlere søkeord kan adskilles med komma (og mellomrom). Skriv NOT foran ord du vil utelukke.\n")
        keyword = input(f"{column}: ")
        
        if "," in keyword:
            table_sql = f"""(SELECT refinement_name FROM {self.db[table]} WHERE {col[column]} LIKE '%{keyword.split(", ")[0]}%'"""
            for word in keyword.split(", ")[1:]:
                table_sql += f" OR {col[column]} LIKE '%{word}%'"
            table_sql += ")"
        else:
            table_sql = f"(SELECT refinement_name FROM {self.db[table]} WHERE {col[column]} LIKE '%{keyword}%')"
        
        self.__sql += f"{table_sql} NATURAL JOIN batches NATURAL JOIN coffee"
        result = self.string_query(self.__sql)
        self.print_matching_coffees(result)
        self.extend_search()
