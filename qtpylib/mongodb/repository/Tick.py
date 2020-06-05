from mongoengine import Document, StringField, DateTimeField, DecimalField, IntField, DynamicDocument
import datetime

tick_types = ('TICK', 'QUOTE')


class Tick(DynamicDocument):
    tickerId = StringField(max_length=50, required=True)
    symbol = StringField(max_length=50, required=False)
    datetime = DateTimeField(required=True, default=datetime.datetime.utcnow)
    open = DecimalField(required=False)
    high = DecimalField(required=False)
    low = DecimalField(required=False)
    close = DecimalField(required=False)
    volume = IntField(required=False)
    vwap = DecimalField()
    buy = DecimalField()
    buysize = IntField()
    sell = DecimalField()
    sellsize = IntField()
    last = DecimalField()
    lastSize = IntField()
    ask = DecimalField()
    asksize = IntField()
    bid = DecimalField()
    bidSize = IntField()
    kind = StringField(default="TICK", choices=tick_types)
    meta = {
        'indexes': ['tickerId', 'datetime', 'kind']
    }
