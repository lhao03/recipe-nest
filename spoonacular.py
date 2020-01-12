import os
import requests

# function for searching for recipes
# search criteria includes: includeingredients,cuisine,diet,excludeingridients,maxreadytime,type


class Spoonacular:
    API_URL = "https://api.spoonacular.com/recipes/complexSearch?number=5&instructionsRequired=true&fillIngredients=true&addRecipeInformation=true&"
    API_KEY = "apiKey=0dea0ed6c1ec4063ae2e452decb07fb8"
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
        result = "Here are the recipes, enjoy! \n ==================================================================================================== \n"
        json_output = json_raw["results"]
        for j in range(0, len(json_output)):
            time_and_title = json_output[j]
            result += time_and_title["title"] + "\n  \n"
            result += "This recipe will take: " + \
                str(time_and_title["readyInMinutes"]) + " minutes" + "\n  \n"

            result += "Here are the ingredients you will need:" + "\n  \n"
            missing_ingredients = time_and_title["missedIngredients"]
            for i in range(0, len(missing_ingredients)):
                missing_dict = missing_ingredients[i]
                result += missing_dict["originalString"] + "\n  \n"

            result += "Here are the ingredients you mentioned that you have:" + "\n  \n"
            have_ingredients = time_and_title["usedIngredients"]
            for h_i in range(0, len(have_ingredients)):
                have_dict = have_ingredients[h_i]
                result += have_dict["originalString"] + "\n  \n"

            result += "And here are the instructions!" + "\n  \n"
            instructions = time_and_title["analyzedInstructions"][0]["steps"]
            for i in range(0, len(instructions)):
                step = instructions[i]
                result += "Step " + str(i + 1) + ": " + step["step"] + "\n  \n"

            result += "==================================================================================================== \n"

        return result
