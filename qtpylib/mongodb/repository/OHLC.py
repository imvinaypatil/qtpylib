from mongoengine import Document, StringField, DateTimeField, DecimalField, IntField, DynamicDocument
import datetime

from qtpylib.enums import Timeframes

RESOLUTION = Timeframes.to_dict()


class OHLC(DynamicDocument):
    tickerId = StringField(max_length=50, required=True)
    symbol = StringField(max_length=50, required=False)
    datetime = DateTimeField(required=True, default=datetime.datetime.utcnow)
    open = DecimalField(required=True)
    high = DecimalField(required=True)
    low = DecimalField(required=True)
    close = DecimalField(required=True)
    volume = IntField(required=True)
    vwap = DecimalField()
    resolution = StringField(choices=RESOLUTION, default=Timeframes.MINUTE_T, unique_with=['tickerId', 'datetime'])
