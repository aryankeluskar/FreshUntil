from fastapi import FastAPI, Response, Cookie, Request
import requests
import json
from dotenv import load_dotenv
import os
from fastapi import UploadFile

load_dotenv()

app = FastAPI()

from fastapi.middleware.cors import CORSMiddleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Adjust this to your specific requirements
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE", "OPTIONS"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    return "Choose one of the two paths: /convertFromISO or /convertFromMilliseconds \nPass duration as a query parameter."


# @app.get("/help")
# async def root():
#     return "Choose one of the two paths: /convertFromISO or /convertFromMilliseconds \nPass duration as a query parameter."

import google.generativeai as genai
from IPython.display import Image
from PIL import Image as image

import os
from dotenv import load_dotenv
load_dotenv()


# route called '/scanreceipt' that takes an image file as input and returns some dummy text
@app.post("/scanreceipt")
async def scan_receipt(image: UploadFile):
    # # Process the image here
    # # create a json with multiple arrays of 'ingridient'
    # # every ingridient has a name, quantity, expirationDate and weight
    # # return the json
    # return {"ingridients": [{"name": "apple", "quantity": 3, "expirationDate": "2022-04-01", "weight": 0.5},
    #                         {"name": "banana", "quantity": 5, "expirationDate": "2022-04-01", "weight": 0.5},
    #                         {"name": "orange", "quantity": 2, "expirationDate": "2022-04-01", "weight": 0.5},
    #                         {"name": "potato", "quantity": 3, "expirationDate": "2022-04-01", "weight": 0.5},
    #                         {"name": "tomato", "quantity": 4, "xexpirationDate": "2022-04-01", "weight": 0.5}]}

    genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

    rec = genai.upload_file(path="./receipt2.png", display_name="receipt2.png")
    model = genai.GenerativeModel(model_name="models/gemini-pro-vision")

    response = model.generate_content(["parse the receipt and tell me what items did i buy and what quantity. return a string formatted as [['item_name', 'quantity'],['item_name', 'quantity'], ['item_name', 'quantity']]. make sure to use single quotes and avoid double quotes, do not return anything before [ or after ]", rec])
    # print(response)
    # print(response.text)

    # the output is:
    # ```
    # [["TOMATO", "5"], ["EGG", "6"], ["FROZEN PIZZA", "2"], ["BANANAS", "12"], ["BROCOLLI", "3"]]
    # ```
    # create a json from the string where there is a array of 'ingredient', which has a 'name', 'expirationDate' and 'quantity' key

    import ast
    items = ast.literal_eval(response.text)
    for i in items:
        print(f"Item: {i[0]}, Quantity: {i[1]}")
        # model = genai.GenerativeModel(model_name="models/gemini-1.5-pro-latest")
        model2 = genai.GenerativeModel(model_name="models/gemini-1.0-pro")
        expdate = model2.generate_content(f"if today is 4/20/24, estimate the date when {i[0]} will expire based on its general perishability. assume its generally being stored in room temperature unless everyone knows it is stored in a fridge. respond strictly as a string in 'mm/dd/yyyy' , strictly do not give any other text because we dont need it")
        print(expdate.text[:10])
        i.append(expdate.text[:10])



    import json
    data = []
    for i in items:
        data.append({"name": i[0], "expirationDate": i[2], "quantity": i[1]})

    out = json.dumps(data, indent=4)


@app.post("/addIngredients")
# ingredients: list of str
async def add_ingredients(ingredients: list):
    try:
        print(ingredients)
        print("received ingredients")
        return True
    except:
        return False
    
@app.post("/findRecipes")
async def find_recipes(ingredients: list):
    print(ingredients)
    outrec = []
    outrec.append({"name": "Apple Pie", "ingredients": ["apple", "flour", "sugar", "butter"], "steps": ["1. first", "2.second", ["3. bake"]]})
    outrec.append({"name": "Salad", "ingredients": ["apple", "tomato", "cucumber", "carrot"], "steps": ["1. Wash the vegetables", "2. Chop the vegetables", "3. Mix the vegetables"]})
    outrec.append({"name": "Ice Pops", "ingredients": ["apple", "kiwi", "strawberry", "lime"], "steps": ["1. Blend the fruits", "2. Pour into popsicle molds", "3. Freeze until solid"]})
    outrec.append({"name": "Pizza", "ingredients": ["apple", "tomato sauce", "cheese", "pepperoni"], "steps": ["1. Roll out the dough", "2. Spread tomato sauce", "3. Add cheese and toppings", "4. Bake in the oven"]})
    outrec.append({"name": "Pasta", "ingredients": ["apple", "tomato sauce", "meatballs", "parmesan cheese"], "steps": ["1. Boil water and cook spaghetti", "2. Heat tomato sauce", "3. Cook meatballs", "4. Combine everything and serve with parmesan cheese"]})
    
    return {"recipes": outrec}