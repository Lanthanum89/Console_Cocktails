"""
Console Cocktails: Fetch a random cocktail recipe from TheCocktailDB API and save it as a real JSON file.
API: https://www.thecocktaildb.com/api/json/v1/1/random.php
Docs: https://www.thecocktaildb.com/api.php
"""

import requests
import json

def get_user_name():
    name = input("What is your name? ").strip()
    if not name:
        return "Guest"
    return name.capitalize()

def fetch_random_cocktail():
    url = "https://www.thecocktaildb.com/api/json/v1/1/random.php"
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        if not data or 'drinks' not in data or not data['drinks']:
            print("No cocktail data found.")
            return None
        return data['drinks'][0]
    except requests.exceptions.RequestException as e:
        print(f"An error occurred while fetching the cocktail data: {e}")
        return None

def extract_cocktail_info(drink):
    # Extract ingredients and measures
    ingredients = []
    for i in range(1, 16):
        ingredient = drink.get(f'strIngredient{i}')
        measure = drink.get(f'strMeasure{i}')
        if ingredient and ingredient.strip():
            ingredients.append({
                'ingredient': ingredient.strip(),
                'measure': measure.strip() if measure else ''
            })
    # Build cocktail info dict
    return {
        'name': drink.get('strDrink', 'Unknown'),
        'alcoholic': drink.get('strAlcoholic', 'Unknown'),
        'instructions': drink.get('strInstructions', 'No instructions'),
        'ingredients': ingredients
    }

def print_cocktail_to_console(cocktail):
    print("\nHere is your random cocktail recipe:")
    print(f"Drink Name: {cocktail['name']}")
    print(f"Alcoholic: {cocktail['alcoholic']}")
    print(f"Instructions: {cocktail['instructions']}")
    print("Ingredients:")
    for item in cocktail['ingredients']:
        print(f"  {item['measure']} {item['ingredient']}")

def save_cocktail_to_json(cocktail, filename):
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(cocktail, f, indent=4, ensure_ascii=False)

def main():
    input_name = get_user_name()
    print(f"Hello, {input_name}! Let's find a random cocktail for you.")
    while True:
        drink = fetch_random_cocktail()
        if not drink:
            break
        cocktail = extract_cocktail_info(drink)
        print_cocktail_to_console(cocktail)
        filename = f"Cocktail_{input_name}.json"
        save_cocktail_to_json(cocktail, filename)
        print(f"\nYour cocktail recipe has been saved to {filename}")
        again = input("\nWould you like another cocktail? (y/n): ").strip().lower()
        if again != 'y':
            print("Goodbye!")
            break

if __name__ == "__main__":
    main()