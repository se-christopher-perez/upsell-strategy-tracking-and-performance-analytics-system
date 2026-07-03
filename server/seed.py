from config import app, db
from models import Bill, Item, Interaction, Terms
from datetime import datetime

with app.app_context():
    db.drop_all()
    db.create_all()

    b1 = Bill(total=4500, tip=800, created_at=str(datetime.now()))
    b2 = Bill(total=2200, tip=300, created_at=str(datetime.now()))
    db.session.add_all([b1, b2])
    db.session.commit()

    i1 = Item(bill_id=b1.id, item_name="Ribeye Steak", category="entree", price=3200, quantity=1)
    i2 = Item(bill_id=b1.id, item_name="House Wine", category="drink", price=1300, quantity=1)
    i3 = Item(bill_id=b2.id, item_name="Caesar Salad", category="appetizer", price=1200, quantity=1)
    i4 = Item(bill_id=b2.id, item_name="Iced Tea", category="drink", price=400, quantity=2)
    db.session.add_all([i1, i2, i3, i4])
    db.session.commit()

    int1 = Interaction(
        bill_id=b1.id, item_id=i2.id,
        customer_gender="F", customer_carded=True, customer_repeat=True,
        approach="suggested wine pairing with steak", upsell=True
    )
    int2 = Interaction(
        bill_id=b1.id, item_id=i1.id,
        customer_gender="F", customer_carded=True, customer_repeat=True,
        approach="asked about steak temperature preference", upsell=False
    )
    int3 = Interaction(
        bill_id=b2.id, item_id=i3.id,
        customer_gender="M", customer_carded=False, customer_repeat=False,
        approach="offered to add grilled chicken to salad", upsell=True
    )
    int4 = Interaction(
        bill_id=b2.id, item_id=i4.id,
        customer_gender="M", customer_carded=True, customer_repeat=True,
        approach="suggested a refill before it ran low", upsell=False
    )
    db.session.add_all([int1, int2, int3, int4])
    db.session.commit()

    t1 = Terms(interaction_id=int1.id, term="pairs perfectly with")
    t2 = Terms(interaction_id=int1.id, term="limited reserve bottle")
    t3 = Terms(interaction_id=int3.id, term="protein boost")
    db.session.add_all([t1, t2, t3])
    db.session.commit()

    print("Seeded!")