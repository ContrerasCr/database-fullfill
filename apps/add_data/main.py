from fastapi import FastAPI
import functions

app = FastAPI(title="Fullfill database")

@app.get("/ping")
def read_root():
    return {"mensaje": "API funcionando 🚀"}


@app.post("/create_users")
def create_users(quantity: int):
    data = functions.create_users(quantity=quantity)
    return data

@app.post("/create_categories")
def create_categories(quantity: int):
    data = functions.create_categories(quantity=quantity)
    return data



@app.post("/create_buy_orders")
def create_buy_orders(quantity: int):
    data = functions.create_buy_orders(quantity=quantity)
    return data



@app.post("/create_order_items")
def create_order_items(quantity: int):
    data = functions.create_order_items(quantity=quantity)
    return data


@app.post("/create_reviews")
def create_reviews(quantity: int):
    data = functions.create_reviews(quantity=quantity)
    return data


@app.post("/create_inventory_logs")
def create_inventory_logs(quantity: int):
    data = functions.create_inventory_logs(quantity=quantity)
    return data


@app.post("/create_sesions")
def create_sesions(quantity: int):
    data = functions.create_sesions(quantity=quantity)
    return data


@app.post("/create_api_logs")
def create_api_logs(quantity: int):
    data = functions.create_api_logs(quantity=quantity)
    return data
