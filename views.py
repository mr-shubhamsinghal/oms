from db.mongo_connection import run_db_query
import schema


async def get_order(order_id: int, collection_name: str) -> dict:
    """To get order with order_id."""
    query_param = {
        "collection_name": collection_name,
        "query_type": "find_one",
        "query": {"order_id": order_id},
    }
    data = await run_db_query(**query_param)
    order_schema = schema.OrderSchema()
    data = order_schema.dump(data)
    return data


async def get_avg_no_of_products_in_orders(collection_name: str) -> dict:
    """To get avg no of products in orders."""
    query_param = {
        "collection_name": collection_name,
        "query_type": "aggregate",
        "query": [
            {
                "$group": {
                    "_id": None,
                    "averageProducts": {"$avg": "$product_count"}
                }
            }
        ]
    }
    data = await run_db_query(**query_param)
    average_products = {}
    for average_product in data:
        rounded_avg_product = round(average_product['averageProducts'], 2)
        average_products["average_products"] = rounded_avg_product
    return average_products


async def get_orders_each_product_avg_qty(collection_name: str,
                                          product_id: int) -> dict:
    """To get orders each product average quantity."""
    query_param = {
        "collection_name": collection_name,
        "query_type": "aggregate",
        "query": [
                    {
                        "$unwind": "$products"
                    },
                    {
                        "$match": {
                            "products.id": product_id
                        }
                    },
                    {
                        "$group": {
                            "_id": None,
                            "averageQuantity": {"$avg": "$products.quantity"}
                        }
                    }
                ]
        }
    data = await run_db_query(**query_param)
    product_average_quantity = {}
    for average_quantity in data:
        rounded_avg_qty = round(average_quantity["averageQuantity"], 2)
        product_average_quantity["product_average_quantity"] = rounded_avg_qty
    return product_average_quantity
