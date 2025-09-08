
# Console Cocktails

A simple Python console application that fetches a random cocktail recipe from TheCocktailDB API and saves it as a JSON file. The app also displays the recipe in the console and allows you to fetch more recipes interactively.

## Features

- Fetches a random cocktail recipe from the internet
- Saves the recipe as a real JSON file (named after your input)
- Prints the recipe details to the console
- Lets you fetch another cocktail or exit
- Handles API and data errors gracefully

## Requirements

- Python 3.7 or higher
- `requests` library

Install dependencies with:

```sh
pip install requests
```

## Usage

1. Run the app:

   ```sh
   python ConsoleApp.py
   ```

2. Enter your name when prompted (or press Enter to use "Guest").
3. View your random cocktail recipe in the console and as a JSON file (e.g., `Cocktail_YourName.json`).
4. Choose to fetch another cocktail or exit.

## Example Output

```text
What is your name? Laura
Hello, Laura! Let's find a random cocktail for you.

Here is your random cocktail recipe:
Drink Name: Margarita
Alcoholic: Alcoholic
Instructions: Rub the rim of the glass with the lime slice to make the salt stick to it. ...
Ingredients:
  1 1/2 oz Tequila
  1/2 oz Triple sec
  1 oz Lime juice
  Salt

Your cocktail recipe has been saved to Cocktail_Laura.json

Would you like another cocktail? (y/n):
```

## API Reference

- [TheCocktailDB API](https://www.thecocktaildb.com/api.php)

## License

This project is for educational and personal use.
