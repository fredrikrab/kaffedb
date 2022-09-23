from ConnectionCtrl import ConnectionCtrl
from helpFunctions import clear_terminal, print_table

def statistics():
    clear_terminal()
    print(f"Select statistic\n\n" \
            "1. Top drinkers\n" \
            "2. Best value\n")

    selection = input("Select option: ")

    if(selection == "1"):
        clear_terminal()
        print_table(["user_name", 'Count'], ConnectionCtrl.getMostTasted())

        return

    elif(selection == "2"):
        clear_terminal()
        print_table(['Roastery name', 'Coffee name', 'Kilo price(NOK)', 'Rating'], ConnectionCtrl.getBestValue())
        return
    
    elif(selection == "q"):
        return
    else:
        statistics()