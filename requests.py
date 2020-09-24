from urllib import request, parse
import json

from objects import Category, Meal, Recipe, Area


def get_categories():
    url = 'https://www.themealdb.com/api/json/v1/1/list.php?c=list'
    f = request.urlopen(url)
    categories = []

    try:
        data = json.loads(f.read().decode('utf-8'))
        for category_data in data['meals']:
            category = Category(category_data['strCategory'])

            categories.append(category)
    except (ValueError, KeyError, TypeError):
        print("JSON format error")

    return categories


def get_meals_by_category(category):
    url = 'https://www.themealdb.com/api/json/v1/1/filter.php?c=' +category
    f = request.urlopen(url)
    meals = []

    try:
        data = json.loads(f.read().decode('utf-8'))
        for meal_data in data['meals']:
            category = Meal(meal_data['idMeal'],
                            meal_data['strMeal'],
                            meal_data['strMealThumb'])
            meals.append(category)
    except (ValueError, KeyError, TypeError):
        print("JSON format error")

    return meals


def get_meal_by_name(meal):
    url = 'https://www.themealdb.com/api/json/v1/1/search.php?s=' + parse.quote(meal)
    f = request.urlopen(url)

    recipe = None
    try:
        data = json.loads(f.read().decode('utf-8'))

        for recipe_data in data['meals']:
            recipe = Recipe(recipe_data['idMeal'],
                            recipe_data['strMeal'],
                            recipe_data['strCategory'],
                            recipe_data['strInstructions'],
                            recipe_data['strMealThumb'],
                            recipe_data['strIngredient1'],
                            recipe_data['strIngredient2'],
                            recipe_data['strIngredient3'],
                            recipe_data['strIngredient4'],
                            recipe_data['strIngredient5'],
                            recipe_data['strIngredient6'],
                            recipe_data['strIngredient7'],
                            recipe_data['strIngredient8'],
                            recipe_data['strIngredient9'],
                            recipe_data['strIngredient10'],
                            recipe_data['strIngredient11'],
                            recipe_data['strIngredient12'],
                            recipe_data['strIngredient13'],
                            recipe_data['strIngredient14'],
                            recipe_data['strIngredient15'],
                            recipe_data['strIngredient16'],
                            recipe_data['strIngredient17'],
                            recipe_data['strIngredient18'],
                            recipe_data['strIngredient19'],
                            recipe_data['strIngredient20'],
                            recipe_data['strMeasure1'],
                            recipe_data['strMeasure2'],
                            recipe_data['strMeasure3'],
                            recipe_data['strMeasure4'],
                            recipe_data['strMeasure5'],
                            recipe_data['strMeasure6'],
                            recipe_data['strMeasure7'],
                            recipe_data['strMeasure8'],
                            recipe_data['strMeasure9'],
                            recipe_data['strMeasure10'],
                            recipe_data['strMeasure11'],
                            recipe_data['strMeasure12'],
                            recipe_data['strMeasure13'],
                            recipe_data['strMeasure14'],
                            recipe_data['strMeasure15'],
                            recipe_data['strMeasure16'],
                            recipe_data['strMeasure17'],
                            recipe_data['strMeasure18'],
                            recipe_data['strMeasure19'],
                            recipe_data['strMeasure20']
                            )
    except (ValueError, KeyError, TypeError):
        print("JSON format error")

    return recipe


def get_meal_by_area(area):
    url = 'https://www.themealdb.com/api/json/v1/1/filter.php?a=' + area
    f = request.urlopen(url)
    meals = []

    try:
        data = json.loads(f.read().decode('utf-8'))
        for meal_data in data['meals']:
            category = Meal(meal_data['idMeal'],
                            meal_data['strMeal'],
                            meal_data['strMealThumb'])
            meals.append(category)
    except (ValueError, KeyError, TypeError):
        print("JSON format error")

    return meals


def get_area():
    url = 'https://www.themealdb.com/api/json/v1/1/list.php?a=list'
    f = request.urlopen(url)
    areas = []

    try:
        data = json.loads(f.read().decode('utf-8'))
        for area_data in data['meals']:
            category = Area(area_data['strArea'])

            areas.append(category)
    except (ValueError, KeyError, TypeError):
        print("JSON format error")

    return areas
