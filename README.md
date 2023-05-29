OMS


This project is used to get information about order information i.e. you can get order information by order_id, can get average quantity of products which is ordered with the help of product_id etc.


Table of Contents

Installation
Usage
Configuration
Endpoints


Installation

1. clone the repository:
git clone lovelocal/oms

2. change into the project directory:
cd oms

3. Create and activate a virtual environment (optional but recommended):
python3 -m venv venv
source venv/bin/activate

4. Install the dependencies:
pip install -r requirements.txt

5. Download mongodb compass and server
server download link -> https://www.mongodb.com/try/download/community
compass download link -> https://www.mongodb.com/try/download/compass

dump db_data.json file into mongodb
create index of order_id and product.id


Usage

1. Run the Flask development server:
flask run

2. Open your browser and visit http://0.0.0.0:5000 to see the application.


Endpoints

List and describe the available API endpoints or routes in your Flask application.

* GET /api/<int:order_id>: Retrieves a order info by using order_id.
* /api/avg-products-in-orders: Retrieves average products in orders.
* /api/orders-each-product-avg-qty/<int:product_id>: Retrieves average ordered product by using product_id.
