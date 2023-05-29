# lovelocal.py

from flask import Flask

from constants import ORDERS_COLLECTION
import views


app = Flask(__name__)


@app.route("/", methods=["GET"])
async def lovelocal() -> str:
    """Entry page."""
    return "LoveLocal Welcomes! you"


@app.route("/api/<int:order_id>", methods=["GET"])
async def get_order(order_id: int) -> dict:
    """To Get a order by order_id."""
    collection_name = ORDERS_COLLECTION
    data = await views.get_order(order_id, collection_name)
    return data


@app.route("/api/avg-products-in-orders", methods=["GET"])
async def get_avg_no_of_products_in_orders() -> dict:
    """To get avg. no of products in orders."""
    collection_name = ORDERS_COLLECTION
    data = await views.get_avg_no_of_products_in_orders(collection_name)
    return data


@app.route("/api/orders-each-product-avg-qty/<int:product_id>",
           methods=["GET"])
async def get_orders_each_product_avg_qty(product_id: int) -> dict:
    """Get orders each product avg qty."""
    collection_name = ORDERS_COLLECTION
    data = await views.get_orders_each_product_avg_qty(collection_name,
                                                       product_id)
    return data


if __name__ == "__main__":
    app.run()
