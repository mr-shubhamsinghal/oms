from marshmallow import Schema, fields


class ProductSchema(Schema):
    """Product schema."""
    id = fields.Integer()
    measurement = fields.String()
    name = fields.String()
    quantity = fields.Integer()


class OrderSchema(Schema):
    """Order schema."""
    order_id = fields.Integer()
    product_count = fields.Integer()
    products = fields.Nested(ProductSchema, many=True)
