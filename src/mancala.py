import sys

def run_game():
    while 1:
        display_menu()


def display_menu():
    print("Menu:")
    menu_choice = input("Press s to start the game.\n" +
                        "Press e to end quit the game.\n")
    if menu_choice == 's':
        print("Game started.")
        display_board()
    elif menu_choice == 'e':
        print("Exiting game.")
        sys.exit(0)
    else:
        print("Please choose between 's' and 'e'.")


def display_board(self):
    return str(self.board)






run_game()