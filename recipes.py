#! /usr/bin/env python3
import requests, textwrap
from random import randint

##This runs like the main!

def show_title():
    print("The Recipes Program")


def display_menu():
    print()
    print("COMMAND MENU")
    print("1 - List all Categories")
    print("2 - List all Meals by Category")
    print("3 - Search Meal by Name")
    print("4 - Random Meal")
    print("5 - List all Areas")
    print("6 - List all Meals by Area")
    print("7 - Menu")
    print("0 - Exit the program")
    print()


def list_categories(categories):
    print()
    print("CATEGORIES:")
    for i in range(len(categories)):
        category = categories[i]
        print("    ",category.get_category())
    print()


def list_area(areas):
    print()
    print("AREAS:")
    for i in range(len(areas)):
        area = areas[i]
        print("    ",area.get_area())
    print()


def list_meals_by_category(category, meals):
    print()
    print(category.upper()+" MEALS")

    for i in range(len(meals)):
        meal = meals[i]
        print("    ",meal.get_meal())
    print()


def list_meals_by_area(area, meals):
    print(area.upper()+" MEALS")
    for i in range(len(meals)):
        meal = meals[i]
        print("    ",meal.get_meal())
    print()


def search_meal_by_category(categories):
    print()
    lookup_category = input("Enter a Category: ")
    found = False

    for i  in range(len(categories)):
        category = categories[i]
        if category.get_category().lower() == lookup_category.lower():
            found = True
            break
    if found:
        meals = requests.get_meals_by_category(lookup_category)
        list_meals_by_category(lookup_category, meals)
    else:
        print("Invalid Category, please try again")


def display_meal(recipe):
    print()
    my_wrap = textwrap.TextWrapper(width=80)
    wrap_list = my_wrap.wrap("Instructions: "+ recipe.get_instructions())
    print("Recipe: ", recipe.get_meal())
    print()
    for line in wrap_list:
        print(line)
    print()
    print("Ingredients:")
    print("{:<40} {:<50}".format("Measurements", "Ingredients"))
    print("--------------------------------------------------------------------------------------------------")
    if recipe.get_strIngredient1():
        print("{:<40} {:<50}".format(recipe.get_strMeasure1(),recipe.get_strIngredient1()))
    if recipe.get_strIngredient2():
        print("{:<40} {:<50}".format(recipe.get_strMeasure2(),recipe.get_strIngredient2()))
    if recipe.get_strIngredient3():
        print("{:<40} {:<50}".format(recipe.get_strMeasure3(),recipe.get_strIngredient3()))
    if recipe.get_strIngredient4():
        print("{:<40} {:<50}".format(recipe.get_strMeasure4(),recipe.get_strIngredient4()))
    if recipe.get_strIngredient5():
        print("{:<40} {:<50}".format(recipe.get_strMeasure5(),recipe.get_strIngredient5()))
    if recipe.get_strIngredient6():
        print("{:<40} {:<50}".format(recipe.get_strMeasure6(),recipe.get_strIngredient6()))
    if recipe.get_strIngredient7():
        print("{:<40} {:<50}".format(recipe.get_strMeasure7(),recipe.get_strIngredient7()))
    if recipe.get_strIngredient8():
        print("{:<40} {:<50}".format(recipe.get_strMeasure8(),recipe.get_strIngredient8()))
    if recipe.get_strIngredient9():
        print("{:<40} {:<50}".format(recipe.get_strMeasure9(),recipe.get_strIngredient9()))
    if recipe.get_strIngredient10():
        print("{:<40} {:<50}".format(recipe.get_strMeasure10(),recipe.get_strIngredient10()))
    if recipe.get_strIngredient11():
        print("{:<40} {:<50}".format(recipe.get_strMeasure11(), recipe.get_strIngredient11()))
    if recipe.get_strIngredient12():
        print("{:<40} {:<50}".format(recipe.get_strMeasure12(),recipe.get_strIngredient12()))
    if recipe.get_strIngredient13():
        print("{:<40} {:<50}".format(recipe.get_strMeasure13(),recipe.get_strIngredient13()))
    if recipe.get_strIngredient14():
        print("{:<40} {:<50}".format(recipe.get_strMeasure14(),recipe.get_strIngredient14()))
    if recipe.get_strIngredient15():
        print("{:<40} {:<50}".format(recipe.get_strMeasure15(),recipe.get_strIngredient15()))
    if recipe.get_strIngredient16():
        print("{:<40} {:<50}".format(recipe.get_strMeasure16(),recipe.get_strIngredient16()))
    if recipe.get_strIngredient17():
        print("{:<40} {:<50}".format(recipe.get_strMeasure17(),recipe.get_strIngredient17()))
    if recipe.get_strIngredient18():
        print("{:<40} {:<50}".format(recipe.get_strMeasure18(),recipe.get_strIngredient18()))
    if recipe.get_strIngredient19():
        print("{:<40} {:<50}}".format(recipe.get_strMeasure19(),recipe.get_strIngredient19()))
    if recipe.get_strIngredient20():
        print("{:<40} {:<50}".format(recipe.get_strMeasure20(),recipe.get_strIngredient20()))

    print()


def search_meal_by_name():
    print()
    lookup_meal = input("Enter Meal Name: ")
    print()
    meal = requests.get_meal_by_name(lookup_meal)
    if meal:
        display_meal(meal)
    else:
        print("A recipe for this meal was not found")


def search_meal_by_area(areas):
    print()
    lookup_category = input("Enter an Area: ")
    print()
    found = False

    for i in range(len(areas)):
        area = areas[i]
        if area.get_area().lower() == lookup_category.lower():
            found = True
            break
    if found:
        meals = requests.get_meal_by_area(lookup_category)
        list_meals_by_area(lookup_category, meals)
    else:
        print("Invalid Category, please try again")


def random_meal(categories):
    random_category_value = randint(0, len(categories))
    random_category = categories[random_category_value].get_category()
    meals = requests.get_meals_by_category(random_category)
    random_meal_value = randint(0, len(meals))
    random_meal = meals[random_meal_value].get_meal()
    meal = requests.get_meal_by_name(random_meal)
    display_meal(meal)


def main():
    show_title()
    display_menu()
    categories = requests.get_categories()
    areas = requests.get_area()
    while True:
        command = input("Command: ")
        if command == "1":
            list_categories(categories)
        elif command == "2":
            search_meal_by_category(categories)
        elif command == "3":
            search_meal_by_name()
        elif command == "4":
            random_meal(categories)
        elif command == "5":
            list_area(areas)
        elif command == "6":
            search_meal_by_area(areas)
        elif command =="7":
            display_menu()
        elif command == "0":
            print()
            print("Thank you for dining with us!")
            break
        else:
            print("Not a valid command. Please try again")


if __name__ == "__main__":
    main()
