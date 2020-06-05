from mongoengine import Document, StringField, DateTimeField, DecimalField, IntField
import datetime


class Trade(Document):
    tickerId = StringField(max_length=50, required=True)
    symbol = StringField(max_length=50, required=False)
    datetime = DateTimeField(required=True, default=datetime.datetime.utcnow)
    algo = StringField(max_length=100)
    direction = StringField(max_length=20)
    quantity = IntField()
    entry_time = DateTimeField()
    exit_time = DateTimeField()
    exit_reason = StringField()
    order_type = StringField()
    market_price = DecimalField()
    target = DecimalField()
    stop = DecimalField()
    entry_price = DecimalField()
    exit_price = DecimalField()
    realized_pnl = DecimalField()

