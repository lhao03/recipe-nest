import os
import requests

API_URL = "https://api.spoonacular.com/recipes/complexSearch?"
API_KEY = "apiKey=40770178730f426c894749c027909c7a"

# function for searching for recipes
# search criteria includes: includeingredients,cuisine,diet,excludeingridients,maxreadytime,type
def user_interface():
    print("Hi! Recipe Nest helps you use ingridients that you have lying around. Just input your ingridients and I'll find you a recipe!")
    print("You can filter by cuisine, diet, maximum preperation time and type of meal. If there are ingridients you do not want in your recipes simply put no infront of the ingrident!")
    user = input()
    search_recipes(ingredients=input())

def search_recipes(ingredients):
     items = ingredients.split(",")
     list_ingredients = items.copy()
     to_get = [("+" + x) for x in list_ingredients]
     query = API_URL + "ingredients=" + items[0] + "," + ",".join(to_get) +"&"+ API_KEY
     response = requests.get(query)
     print(response.json())

# function to sort by cuisine  
def by_cuisine(cuisine):




# response = requests.get("https://api.spoonacular.com/recipes/findByIngredients?ingredients=apples,+flour,+sugar&number=2&apiKey=40770178730f426c894749c027909c7a")
                         
# print(response.json())