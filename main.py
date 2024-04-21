from fastapi import FastAPI, Response, Cookie, Request
import requests
import json
from dotenv import load_dotenv
import os
from fastapi import UploadFile

load_dotenv()

app = FastAPI()

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
                            {"name": "tomato", "quantity": 4, "expirationDate": "2022-04-01", "weight": 0.5}]}