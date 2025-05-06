import json

def load_data():
    with open("app/data/products.json", "r", encoding="utf-8") as file:
      all_products = json.load(file)
      return all_products