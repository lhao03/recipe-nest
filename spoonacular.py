import os
import requests

# function for searching for recipes
# search criteria includes: includeingredients,cuisine,diet,excludeingridients,maxreadytime,type


class Spoonacular:
    API_URL = "https://api.spoonacular.com/recipes/complexSearch?number=1&instructionsRequired=true&fillIngredients=true&addRecipeInformation=true&"
    API_KEY = "apiKey=40770178730f426c894749c027909c7a"
    API_URL_IMAGES = "https://api.spoonacular.com/recipes/"
    IMAGE_CONT = "/ingredientWidget"

    def search_recipes(self, ingredients, diet, mealtype, time, cuisine):
        i = 1
        while i > 0:
            # for the ingridients to include - list
            user_ingredients = ingredients
            final_ingre = self.check_inputs(user_ingredients)
            if final_ingre == None:
                pass
            else:
                response = "includeIngredients=" + final_ingre + "&"

            # for the cuisines to include - list
            user_cuisine = cuisine
            final_cuisine = self.check_inputs(user_cuisine)
            if final_cuisine == None:
                pass
            else:
                response = response + "cuisine=" + final_cuisine + "&"

            # for the diet - string
            if diet.strip() == "none":
                pass
            else:
                response = response + "diet=" + diet.strip() + "&"

            # for time - dict/string
            final_time = self.check_time(time)
            if final_time == None:
                pass
            else:
                response = response + "maxReadyTime=" + str(final_time) + "&"

            # for meal type - string
            i = i - 1
            if mealtype.strip() == "none":
                pass
            else:
                response = response + "type=" + mealtype.strip() + "&"
        query = Spoonacular.API_URL + response + Spoonacular.API_KEY
        # response = requests.get(query)
        # return response.json()
        response = requests.get(query)
        return self.show_output(response.json())

    def join_inputs(self, user_inputs):
        if len(user_inputs) == 1:
            return user_inputs[0]
        else:
            X_get = [("+" + x.strip()) for x in user_inputs]
            X_joined = user_inputs[0] + "," + ",".join(X_get)
            return X_joined

    def check_inputs(self, the_input):
        if the_input[0].strip() == "none":
            return None
        else:
            return self.join_inputs(the_input)

    def check_time(self, usertime):
        if usertime == "none" or usertime == "":
            return None
        elif usertime["unit"] == "min":
            return int(usertime["amount"])
        elif usertime["unit"] == "h":
            return int(usertime["amount"] * 60)

    # def show_ingredients(self):
    def show_output(self, json_raw):
        result = ""
        json_output = json_raw["results"]
        time_and_title = json_output[0]
        result += time_and_title["title"] + "\n"
        result += "This recipe will take: " + \
            str(time_and_title["readyInMinutes"]) + " minutes" + "\n"

        result += "Here are the ingredients you will need:" + "\n"
        missing_ingredients = time_and_title["missedIngredients"]
        for i in range(0, len(missing_ingredients)):
            missing_dict = missing_ingredients[i]
            result += missing_dict["originalString"] + "\n"

        result += "Here are the ingredients you mentioned that you have:" + "\n"
        have_ingredients = time_and_title["usedIngredients"]
        for h_i in range(0, len(have_ingredients)):
            have_dict = have_ingredients[h_i]
            result += have_dict["originalString"] + "\n"

        result += "And here are the instructions!" + "\n"
        instructions = time_and_title["analyzedInstructions"][0]["steps"]
        for i in range(0, len(instructions)):
            step = instructions[i]
            result += "Step " + str(i + 1) + ": " + step["step"] + "\n"

        return result
