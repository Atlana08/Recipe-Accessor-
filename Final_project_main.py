#! /usr/bin/env python3


def display_menu():
    print("1 - List all Categories")
    print("2 - List all Meals by Category")
    print("3 - Search Meal by Name")
    print("4 - Random Meal")
    print("5 - List all Areas")
    print("6 - List all Meals by Area")
    print("7 - Menu")
    print("0 - Exit all Meals by Areas")
    print()


def command_1():
    print()
    print("CATEGORIES:")
    print("   Beef")
    print("   Breakfast")
    print("   Chicken")
    print("   Dessert")
    print("   Goat")
    print("   Lamb")
    print("   Miscellaneous")
    print("   Pasta")
    print("   Port")
    print("   Seafood")
    print("   Side")
    print("   Starter")
    print("   Vegan")
    print("   Vegetarian")
    print()

def main():
    print("The Recipes Program")
    print()
    display_menu()
    while True:
        command = input("Command: ")
        if command == "1":
            command_1()



if __name__ == "__main__":
    main()