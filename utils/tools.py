import os, json, random, string
from difflib import get_close_matches
from pystyle import *

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def add_password(password=None):
    print(" ")
    site = Write.Input("    Enter the website: ", Colors.white_to_red, interval=0)
    email = Write.Input("    Enter the email: ", Colors.white_to_red, interval=0)
    if not password:
        password = Write.Input("    Enter the password: ", Colors.white_to_red, interval=0)
    password_info = {
        "site": site,
        "email": email,
        "password": password
    }
    try:
        with open("passwords.json", "r") as file:
            data = json.load(file)
            if isinstance(data, dict):
                data = [data]
            elif not isinstance(data, list):
                data = []
    except FileNotFoundError:
        data = []
    except json.JSONDecodeError:
        data = []

    data.append(password_info)

    with open("passwords.json", "w") as file:
        json.dump(data, file, indent=4)

    Write.Print("    Password added successfully!\n \n", Colors.white_to_red, interval=0)

def generate_password():
    try:
        length = int(Write.Input("    Enter the length of the password: ", Colors.white_to_red, interval=0))
        if length <= 0:
            Write.Print("    Invalid length. Please enter a positive integer.", Colors.white_to_red, interval=0)
            return None
    except ValueError:
        Write.Print("    Invalid input. Please enter a valid integer.", Colors.white_to_red, interval=0)
        return None

    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    Write.Print(f"    [*] Generated password: {password}\n", Colors.white_to_red, interval=0)

    save = Write.Input("    Do you want to save this password? (y/n): ", Colors.white_to_red, interval=0).lower()
    if save == 'y':
        add_password(password)

def show_passwords():
    try:
        with open("passwords.json", "r") as file:
            data = json.load(file)
            if isinstance(data, dict):
                data = [data]
        
        site = Write.Input("\n    Enter the website to search for: ", Colors.white_to_red, interval=0)
        exact_matches = [entry for entry in data if entry.get("site") == site]
        
        if exact_matches:
            for entry in exact_matches:
                Write.Print(f"\n    Website: {entry['site']}\n", Colors.white_to_red, interval=0)
                Write.Print(f"    Email: {entry['email']}\n", Colors.white_to_red, interval=0)
                Write.Print(f"    Password: {entry['password']}\n\n", Colors.white_to_red, interval=0)
        else:
            # If no exact matches, find the closest matches
            sites = [entry.get("site") for entry in data]
            closest_matches = get_close_matches(site, sites, n=3, cutoff=0.6)  # Adjust cutoff for sensitivity
            if closest_matches:
                Write.Print(f"    No exact match found. Did you mean:\n", Colors.red_to_white, interval=0)
                for match in closest_matches:
                    for entry in data:
                        if entry.get("site") == match:
                            Write.Print(f"    Website: {entry['site']}\n", Colors.white_to_red, interval=0)
                            Write.Print(f"    Email: {entry['email']}\n", Colors.white_to_red, interval=0)
                            Write.Print(f"    Password: {entry['password']}\n\n", Colors.white_to_red, interval=0)
            else:
                Write.Print(f"\n    No similar matches found for '{site}'.\n", Colors.red_to_white, interval=0)

    except FileNotFoundError:
        Write.Print("\n    No passwords stored.\n", Colors.white_to_red, interval=0)
    except json.JSONDecodeError:
        Write.Print("    Error reading passwords.json. Please ensure it contains valid JSON.\n", Colors.red_to_white, interval=0)
