from Search import Search
from StatisticsCtrl import statistics
from User import User
from Search import Search
from CreateReview import CreateReview
from helpFunctions import clear_terminal
from DBI import DBI


def main_menu(user, dbi):
    clear_terminal()
    print("Hovedmeny\n\n" \
        "1. Lag ny kaffe anmeldelse\n" \
        "2. Infromasjons søk\n" \
        "3. Statistikk\n" \
        "q. Bytt bruker\n")

    selection = input("Velg: ")

    if selection == "1":
        review = CreateReview(user_email=user.get_email())
        review.print_overview()
        review.select_coffee(dbi)
        
        review.print_overview()
        review.set_rating()
        
        review.print_overview()
        review.write_note()
        
        while not review.is_completed():
            review.confirm_review(dbi)
        
        del review

    elif selection == "2":
        search = Search()
        
        search.search_menu()
    elif selection == "3":
        dbi.statistics()
    elif selection == "q":
        user = User.login()
        main_menu(user)
    else:
        main_menu(user)


def main():
    dbi = DBI()
    user = User()
    user.login_from_list(dbi)
    main_menu(user, dbi)


if __name__ == "__main__":
    main()
