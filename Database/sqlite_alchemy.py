from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, ForeignKey, Integer, String, FLOAT, SmallInteger,DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.orm import sessionmaker
from datetime import datetime, date
from pprint import pprint

engine = create_engine('sqlite:////web/Sqlite-Data/lwm.db')
Base = declarative_base()


class Customer(Base):
    __tablename__ = 'Customer'
    id = Column(Integer, primary_key=True)
    first_name = Column(String(250), nullable=False)
    last_name = Column(String(250), nullable=False)
    username = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)
    address = Column(String(250), nullable=False)
    town = Column(String(250), nullable=False)
    created_on = Column(DateTime(), default=datetime.now)
    updated_on = Column(DateTime(), default=datetime.now, onupdate=datetime.now)
    orders = relationship("Order", backref='customer')


class Item(Base):
    __tablename__ = 'items'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    cost_price = Column(FLOAT, nullable=False)
    selling_price = Column(FLOAT, nullable=False)
    quantity = Column(Integer, nullable=False)


class Order(Base):
    __tablename__ = 'orders'
    id = Column(Integer(), primary_key=True)
    customer_id = Column(Integer, ForeignKey('customers.id'))
    order_lines = relationship("OrderLine", backref='orders')
    date_placed = Column(DateTime(), default=datetime.now)


class OrderLine(Base):
    __tablename__ = 'order_lines'
    id = Column(Integer(), primary_key=True)
    order_id = Column(Integer(), ForeignKey('orders.id'))
    item_id = Column(Integer(), ForeignKey('items.id'))
    quantity = Column(SmallInteger())


Base.metadata.create_all(engine)
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()

c1 = Customer(first_name='Toby',
              last_name='Miller',
              username='tmiller',
              email='tmiller@example.com',
              address='1662 Kinney Street',
              town='Wolfden'
              )

c2 = Customer(first_name='Scott',
              last_name='Harvey',
              username='scottharvey',
              email='scottharvey@example.com',
              address='424 Patterson Street',
              town='Beckinsdale'
              )

session.add_all([c1, c2])
session.commit()

print(c1.id)
print(c2.id)

c3 = Customer(
    first_name="John",
    last_name="Lara",
    username="johnlara",
    email="johnlara@mail.com",
    address="3073 Derek Drive",
    town="Norfolk"
)

c4 = Customer(
    first_name="Sarah",
    last_name="Tomlin",
    username="sarahtomlin",
    email="sarahtomlin@mail.com",
    address="3572 Poplar Avenue",
    town="Norfolk"
)

c5 = Customer(first_name='Toby',
              last_name='Miller',
              username='tmiller',
              email='tmiller@example.com',
              address='1662 Kinney Street',
              town='Wolfden'
              )

c6 = Customer(first_name='Scott',
              last_name='Harvey',
              username='scottharvey',
              email='scottharvey@example.com',
              address='424 Patterson Street',
              town='Beckinsdale'
              )

session.add_all([c3, c4, c5, c6])
session.commit()

i1 = Item(name='Chair', cost_price=9.21, selling_price=10.81, quantity=5)
i2 = Item(name='Pen', cost_price=3.45, selling_price=4.51, quantity=3)
i3 = Item(name='Headphone', cost_price=15.52, selling_price=16.81, quantity=50)
i4 = Item(name='Travel Bag', cost_price=20.1, selling_price=24.21, quantity=50)
i5 = Item(name='Keyboard', cost_price=20.1, selling_price=22.11, quantity=50)
i6 = Item(name='Monitor', cost_price=200.14, selling_price=212.89, quantity=50)
i7 = Item(name='Watch', cost_price=100.58, selling_price=104.41, quantity=50)
i8 = Item(name='Water Bottle', cost_price=20.89, selling_price=25, quantity=50)

session.add_all([i1, i2, i3, i4, i5, i6, i7, i8])
session.commit()

o1 = Order(customer_id=c1.id)
o2 = Order(customer_id=c1.id)

line_item1 = OrderLine(order_id=o1.id, item_id=i1.id, quantity=3)
line_item2 = OrderLine(order_id=o1.id, item_id=i2.id, quantity=2)
line_item3 = OrderLine(order_id=o2.id, item_id=i1.id, quantity=1)
line_item4 = OrderLine(order_id=o2.id, item_id=i2.id, quantity=4)

session.add_all([o1, o2])

session.new()
session.commit()

print('--------------------------------------------------------------------------')

o3 = Order(customer_id=c1.id)
orderline1 = OrderLine(item_id=i1.id, quantity=5)
orderline2 = OrderLine(item_id=i2.id, quantity=10)

o3.order_lines.append(orderline1)
o3.order_lines.append(orderline2)

session.add_all([o3])

session.commit()

print("customer1.orders")
print(c1.orders)
print()

print("order1.customer")
print(o1.customer)
print()

print("customer1.orders(3).order_lines")
print(c1.orders[2].order_lines)
print()

print("details of customer1.orders(3).order_lines")
for ol in c1.orders[2].order_lines:
    print("ol id:")
    print(ol.id)
    print()
    print("ol.item_id:")
    print(ol.item_id)
    print()
    print("ol.quantity:")
    print(ol.quantity)
    print()


print('--------------------------------------------------------------------------')
print()

print("# Section 3")

session.query(Customer).all()

session.query(Customer)

q = session.query(Customer)

for c in q:
    print(c.id, c.first_name)

print()

print(session.query(Customer.id, Customer.first_name).all())