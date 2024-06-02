import os
from pystyle import Colors, Colorate, Write
from utils.banner import banner
from utils.tools import add_password, generate_password, clear_screen, show_passwords

def main_menu():
    options = ["Add a password", "Generate a password", "Show passwords", "Exit"]
    selected_option = 0

    def print_menu(selected):
        clear_screen()
        print(Colorate.Horizontal(Colors.purple_to_red, banner))
        Write.Print("    [?] What do you want to do?\n", Colors.white_to_red, interval=0)
        for i, option in enumerate(options):
            if i == selected:
                Write.Print(f"      {i+1}. {option}\n", Colors.white_to_red, interval=0)
            else:
                Write.Print(f"      {i+1}. {option}\n", Colors.white_to_red, interval=0)

    print_menu(selected_option)
    
    while True:
        try:
            choice = Write.Input(f"\n    [$] Enter your choice: ", Colors.white_to_red, interval=0)
            choice = int(choice)
            if 1 <= choice <= len(options):
                selected_option = choice - 1
                if choice == 1:
                    add_password()
                elif choice == 2:
                    generate_password()
                elif choice == 3:
                    show_passwords()
                elif choice == 4:
                    print(Colorate.Horizontal(Colors.yellow, "    Exiting..."))
                    break
            else:
                print(Colorate.Horizontal(Colors.red, "    Invalid choice. Please enter a number between 1 and 4."))
        except ValueError:
            Write.Print(f"    [!] Invalid choice. Please enter a number.\n", Colors.red_to_blue, interval=0)
        Write.Input(f"    [$] Press enter to continue\n", Colors.red_to_blue, interval=0)
        print_menu(selected_option)

if __name__ == "__main__":
    main_menu()
