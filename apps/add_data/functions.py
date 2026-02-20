from faker import Faker
import random
from datetime import date, datetime
from uuid import uuid4

faker = Faker()

def create_users(quantity):
    users = [
        {"username": faker.user_name(),
        "email": faker.free_email(),
        "password": faker.password(),
        "create_at": faker.date_between(
            start_date=date(2021, 1, 1),
            end_date=date(2026, 1, 1),
        ).strftime("%Y/%m/%d"),
        "last_login": faker.date_between(
            start_date=date(2025, 1, 1),
            end_date=date(2026, 1, 1),
        ).strftime("%Y/%m/%d"),
        "status": random.choice(["active", "inactive", "suspended"]),
        "country": faker.country(),
        "subscription_tier": random.choice(["free", "premium", "enterprise"])
        }
        for i in range(quantity)
    ]

    return users


def create_products(quantity):
    products = quantity*0.1 if quantity*0.1 > 5 else 5
    names = [faker.name().split(" ")[-1] for _ in range(quantity)]
    names = names[:products]
    product = [
        {
            "name": random.choice(names),
            "description": faker.paragraph(3),
            "price": random.randrange(0, 1001, 10),
            "stock_quantity": random.randrange(0, 55, 1),
            "catagory_id": random.randrange(1, 5, 1),
            "create_at": faker.date_between(
                    start_date=date(2021, 1, 1),
                    end_date=date(2026, 1, 1),
                ).strftime("%Y/%m/%d"),
            "updated_at": faker.date_between(
                        start_date=date(2024, 1, 1),
                        end_date=date(2026, 1, 1),
                    ).strftime("%Y/%m/%d"),
            "is_active": random.choice([True, False]),
            "weight_kg": random.choice([i for i in range(1,32)]),
            "image_url": faker.url()
        }
        for _ in range(quantity)
        
    ]
    return product


def create_categories(quantity):
    products = quantity*0.1 if quantity*0.1 > 5 else 3
    names = [faker.name().split(" ")[-1] for _ in range(quantity)]
    names = names[:products]
    categories = [
        {
            "name": random.choice(names),
            "description": faker.paragraph(3),
            "create_at": faker.date_between(
                    start_date=date(2021, 1, 1),
                    end_date=date(2026, 1, 1),
                ).strftime("%Y/%m/%d"),

        }
        for _ in range(quantity)
    ]

    return categories


def create_buy_orders(quantity):
    buy_orders = [
        {
            "user_id" : random.randrange(0, 10, 1),
            "total_amount" : random.randrange(0, 50, 1),
            "status" : random.choice(["pending", "confirmed", "shipped", "delivered", "cancelled"]),
            "create_at": faker.date_between(
                    start_date=date(2021, 1, 1),
                    end_date=date(2026, 1, 1),
                ).strftime("%Y/%m/%d"),
            "updated_at" : faker.date_between(
                    start_date=date(2025, 1, 1),
                    end_date=date(2026, 1, 1),
                ).strftime("%Y/%m/%d"),
            "shipping_adress" : faker.address(),
            "payment_method" : random.choice(["card", "cash"]),
            "payment_status" : random.choice(("pending", "completed", "failed", "refunded")),

        }
        for _ in range(quantity)
    ]
    return buy_orders


def create_order_items(quantity):
    order_items = [
        {
            "order_id": random.randrange(0, 10, 1),
            "product_id": random.randrange(0, 10, 1),
            "quantity": random.randrange(0, 10, 1),
            "unit_price": random.randrange(0, 100, 1)
        }
        for _ in range(quantity)
    ]
    return order_items


def create_reviews(quantity):
    reviews = [
        {
            "id": str(uuid4()),
            "product_id": random.randrange(0, 10, 1),
            "user_id": random.randrange(0, 10, 1),
            "rating": random.randrange(1, 6, 1),
            "title": faker.paragraph(1),
            "comment":  faker.paragraph(3),
            "create_at": faker.date_between(
                    start_date=date(2021, 1, 1),
                    end_date=date(2026, 1, 1),
                ).strftime("%Y/%m/%d"),
            "helpful_count": random.randrange(0, 100, 1),
            "verified_purchase": random.choice([True, False]),
        }
        for _ in range(quantity)
    ]
    return reviews


def create_inventory_logs(quantity):
    logs = [
        {
        "id": str(uuid4),
        "product_id": random.randrange(0, 10, 1),
        "change_type": random.choice(("restock", "sale", "return", "adjustment")),
        "quantity_change": random.randrange(0, 10, 1),
        "previous_quantity": random.randrange(0, 10, 1),
        "new_quantity": random.randrange(0, 10, 1),
        "create_at": faker.date_between(
                start_date=date(2021, 1, 1),
                end_date=date(2026, 1, 1),
            ).strftime("%Y/%m/%d"),
        "created_by": random.choice(("user_id", "system")),
        "notes": faker.paragraph(3)
        }
        for _ in range(quantity)
    ]
    return logs


def create_sesions(quantity):
    sesions = [
        {
        "id": str(uuid4()),
        "user_id": random.randrange(0, 10, 1),
        "session_token": str(uuid4()),
        "create_at": faker.date_between(
                start_date=date(2021, 1, 1),
                end_date=date(2026, 1, 1),
            ).strftime("%Y/%m/%d"),
        "expires_at": faker.date_between(
                start_date=date(2021, 1, 1),
                end_date=date(2026, 1, 1),
            ).strftime("%Y/%m/%d"),
        "last_activity": faker.date_between(
                start_date=date(2021, 1, 1),
                end_date=date(2026, 1, 1),
            ).strftime("%Y/%m/%d"),
        "ip_address": f"{random.randrange(0, 256, 1)}.{random.randrange(0, 256, 1)}.{random.randrange(0, 256, 1)}.{random.randrange(0, 256, 1)}",
        }
        for _ in range(quantity)
    ]
    return sesions


def create_api_logs(quantity):
    api_logs = [
        {
        "id": str(uuid4()),
        "timestamp": datetime.now().timestamp(),
        "endpoint": random.choice([f"endpoint{n}" for n in range(1, 4)]),
        "method": random.choice(("GET", "POST", "PUT", "DELETE")),
        "user_id": random.randrange(0, 10, 1),
        "status_code": random.choice([i for i in range(200, 210)]),
        "response_time_ms": random.randrange(40, 1500,1),
        "request_size_bytes": random.randrange(40, 1500,1),
        "response_size_bytes": random.randrange(40, 1500,1),
        "error_message": "Success"
        }
        for _ in range(quantity)
    ]
    return api_logs
