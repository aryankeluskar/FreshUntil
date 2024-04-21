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


# route called '/scanreceipt' that takes an image file as input and returns some dummy text
@app.post("/scanreceipt")
async def scan_receipt(image: UploadFile):
    # Process the image here
    # create a json with multiple arrays of 'ingridient'
    # every ingridient has a name, quantity, expirationDate and weight
    # return the json
    return {"ingridients": [{"name": "apple", "quantity": 3, "expirationDate": "2022-04-01", "weight": 0.5},
                            {"name": "banana", "quantity": 5, "expirationDate": "2022-04-01", "weight": 0.5},
                            {"name": "orange", "quantity": 2, "expirationDate": "2022-04-01", "weight": 0.5},
                            {"name": "potato", "quantity": 3, "expirationDate": "2022-04-01", "weight": 0.5},
                            {"name": "tomato", "quantity": 4, "xexpirationDate": "2022-04-01", "weight": 0.5}]}

@app.get("/addIngredients")
# ingredients: list of str
async def add_ingredients(ingredients: list):
    try:
        print(ingredients)
        print("received ingredients")
        return True
    except:
        return False
    
@app.get("/findRecipes")
async def find_recipes(ingredients: list):
    outrec = []
    outrec.append({"name": "Apple Pie", "ingredients": ["apple", "flour", "sugar", "butter"], "steps": ["1. first", "2.second", ["3. bake"]]})
    outrec.append({"name": "Salad", "ingredients": ["apple", "tomato", "cucumber", "carrot"], "steps": ["1. Wash the vegetables", "2. Chop the vegetables", "3. Mix the vegetables"]})
    outrec.append({"name": "Ice Pops", "ingredients": ["apple", "kiwi", "strawberry", "lime"], "steps": ["1. Blend the fruits", "2. Pour into popsicle molds", "3. Freeze until solid"]})
    outrec.append({"name": "Pizza", "ingredients": ["apple", "tomato sauce", "cheese", "pepperoni"], "steps": ["1. Roll out the dough", "2. Spread tomato sauce", "3. Add cheese and toppings", "4. Bake in the oven"]})
    outrec.append({"name": "Pasta", "ingredients": ["apple", "tomato sauce", "meatballs", "parmesan cheese"], "steps": ["1. Boil water and cook spaghetti", "2. Heat tomato sauce", "3. Cook meatballs", "4. Combine everything and serve with parmesan cheese"]})
    
    return {"recipes": outrec}