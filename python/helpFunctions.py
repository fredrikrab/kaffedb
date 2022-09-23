from os import system, name
from tabulate import tabulate

def clear_terminal():
    """Clears all current text from the user's terminal.
    """
    if name == "nt":
        system('cls')
    else:
        system('clear')


def print_table(table, column_titles:list, showindex=False, tablefmt='fancy_grid'):
    """Prints a nicely formatted table to terminal.

    Args:
        table (tabular_data): raw table data
        header_list (list): list of column titles
        showindex (bool | iterator): add row index column
    """
    print(tabulate(table, headers=column_titles, showindex=showindex, tablefmt=tablefmt))


def get_int_user_input(min:int, max:int):
    """Require the user to input an integer within the given interval (inclusive).

    Args:
        min (int): minimum allowed input
        max (int): maxiumum allowed input

    Raises:
        ValueError: user input is outside permitted interval or is not an integer

    Returns:
        int: integer from user input
    """
    while True:
        try:
            user_input = int(input(" "))
            if min <= user_input <= max:
                break
            raise ValueError
        except ValueError:
            print(f"Velg et tall mellom {min} og {max}:", end="")
    return user_input