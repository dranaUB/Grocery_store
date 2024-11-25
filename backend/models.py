from app import db


class UOM(db.Model):
    __tablename__ = 'uom'
    uom_id = db.Column(db.Integer, primary_key=True)
    uom_name = db.Column(db.String(45), nullable=False)

class Product(db.Model):
    __tablename__ = 'products'
    product_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    uom_id = db.Column(db.Integer, db.ForeignKey('uom.uom_id'), nullable=False)
    price_per_unit = db.Column(db.Float, nullable=False)

class Order(db.Model):
    __tablename__ = 'orders'
    order_id = db.Column(db.Integer, primary_key=True)
    customer_name = db.Column(db.String(100), nullable=False)
    total = db.Column(db.Float, nullable=False)
    datetime = db.Column(db.DateTime, nullable=False)

class OrderDetail(db.Model):
    __tablename__ = 'order_details'
    order_id = db.Column(db.Integer, db.ForeignKey('orders.order_id'), primary_key=True)
    product_id = db.Column(db.Integer, db.ForeignKey('products.product_id'), primary_key=True)
    quantity = db.Column(db.Float, nullable=False)
    total_price = db.Column(db.Float, nullable=False)
    