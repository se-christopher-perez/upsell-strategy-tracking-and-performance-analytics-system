from config import db
from sqlalchemy.orm import validates

class Bill(db.Model):
    __tablename__ = "bills"

    id = db.Column(db.Integer, primary_key=True)
    total = db.Column(db.Integer)
    tip = db.Column(db.Integer)
    created_at = db.Column(db.String)

    items = db.relationship("Item", back_populates="bill")
    interactions = db.relationship("Interaction", back_populates="bill")


class Item(db.Model):
    __tablename__ = "items"

    id = db.Column(db.Integer, primary_key=True)
    bill_id = db.Column(db.Integer, db.ForeignKey('bills.id'), nullable=False)
    item_name = db.Column(db.String)
    category = db.Column(db.String)
    price = db.Column(db.Integer)
    quantity = db.Column(db.Integer)

    bill = db.relationship("Bill", back_populates="items")
    interactions = db.relationship("Interaction", back_populates="item")


class Interaction(db.Model):
    __tablename__ = "interactions"

    id = db.Column(db.Integer, primary_key=True)
    bill_id = db.Column(db.Integer, db.ForeignKey('bills.id'), nullable=False)
    item_id = db.Column(db.Integer, db.ForeignKey('items.id'), nullable=False)
    approach = db.Column(db.String)
    upsell = db.Column(db.Boolean)
    customer_gender = db.Column(db.String)
    customer_carded = db.Column(db.Boolean)
    customer_repeat = db.Column(db.Boolean)

    bill = db.relationship("Bill", back_populates="interactions")
    item = db.relationship("Item", back_populates="interactions")
    terms = db.relationship("Terms", back_populates="interaction")


class Terms(db.Model):
    __tablename__ = "terms"

    id = db.Column(db.Integer, primary_key=True)
    interaction_id = db.Column(db.Integer, db.ForeignKey('interactions.id'), nullable=False)
    term = db.Column(db.String)

    interaction = db.relationship("Interaction", back_populates="terms")