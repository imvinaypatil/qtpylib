class sides:
    BUY = 'buy'
    SELL = 'sell'


class trade_types:
    LONG = 'long'
    SHORT = 'short'


class order_statuses:
    ACTIVE = 'ACTIVE'
    CANCELED = 'CANCELED'
    EXECUTED = 'EXECUTED'
    QUEUED = 'QUEUED'


class Timeframes:
    MINUTE_T = 'T'
    MINUTE_1 = '1m'
    MINUTE_3 = '3m'
    MINUTE_5 = '5m'
    MINUTE_15 = '15m'
    MINUTE_30 = '30m'
    HOUR_1 = '1h'
    HOUR_2 = '2h'
    HOUR_3 = '3h'
    HOUR_4 = '4h'
    HOUR_6 = '6h'
    HOUR_8 = '8h'
    DAY_1 = '1D'

    @staticmethod
    def to_dict():
        return (
            Timeframes.MINUTE_T,
            Timeframes.MINUTE_1,
            Timeframes.MINUTE_3,
            Timeframes.MINUTE_5,
            Timeframes.MINUTE_15,
            Timeframes.MINUTE_30,
            Timeframes.HOUR_1,
            Timeframes.HOUR_2,
            Timeframes.HOUR_3,
            Timeframes.HOUR_4,
            Timeframes.HOUR_6,
            Timeframes.HOUR_8,
            Timeframes.DAY_1
        )

    @staticmethod
    def timeframe_to_one_minutes(timeframe):
        dic = {
            Timeframes.MINUTE_T: 1,
            Timeframes.MINUTE_1: 1,
            Timeframes.MINUTE_3: 3,
            Timeframes.MINUTE_5: 5,
            Timeframes.MINUTE_15: 15,
            Timeframes.MINUTE_30: 30,
            Timeframes.HOUR_1: 60,
            Timeframes.HOUR_2: 60 * 2,
            Timeframes.HOUR_3: 60 * 3,
            Timeframes.HOUR_4: 60 * 4,
            Timeframes.HOUR_6: 60 * 6,
            Timeframes.HOUR_8: 60 * 8,
            Timeframes.DAY_1: 60 * 24,
        }
        try:
            return dic[timeframe]
        except KeyError:
            raise Exception(
                'Timeframe "{}" is invalid. Supported timeframes are 1m, 3m, 5m, 15m, 30m, 1h, 2h, 3h, 4h, 6h, 8h, 1D'.format(
                    timeframe))

    @staticmethod
    def timeframe_to_resolution(timeframe):
        dic = {
            Timeframes.MINUTE_T: "1T",
            Timeframes.MINUTE_1: "1T",
            Timeframes.MINUTE_3: "3T",
            Timeframes.MINUTE_5: "5T",
            Timeframes.MINUTE_15: "15T",
            Timeframes.MINUTE_30: "30T",
            Timeframes.HOUR_1: "60T",
            Timeframes.HOUR_2: f'{60 * 2}T',
            Timeframes.HOUR_3: f'{60 * 3}T',
            Timeframes.HOUR_4: f'{60 * 4}T',
            Timeframes.HOUR_6: f'{60 * 6}T',
            Timeframes.HOUR_8: f'{60 * 8}T',
            Timeframes.DAY_1: f'{60 * 24}T',
        }

        try:
            return dic[timeframe]
        except KeyError:
            raise Exception(
                'Timeframe "{}" is invalid. Supported timeframes are 1m, 3m, 5m, 15m, 30m, 1h, 2h, 3h, 4h, 6h, 8h, 1D'.format(
                    timeframe))

    @staticmethod
    def max_timeframe(timeframes_list):
        if Timeframes.DAY_1 in timeframes_list:
            return Timeframes.DAY_1
        if Timeframes.HOUR_8 in timeframes_list:
            return Timeframes.HOUR_8
        if Timeframes.HOUR_6 in timeframes_list:
            return Timeframes.HOUR_6
        if Timeframes.HOUR_4 in timeframes_list:
            return Timeframes.HOUR_4
        if Timeframes.HOUR_3 in timeframes_list:
            return Timeframes.HOUR_3
        if Timeframes.HOUR_2 in timeframes_list:
            return Timeframes.HOUR_2
        if Timeframes.HOUR_1 in timeframes_list:
            return Timeframes.HOUR_1
        if Timeframes.MINUTE_30 in timeframes_list:
            return Timeframes.MINUTE_30
        if Timeframes.MINUTE_15 in timeframes_list:
            return Timeframes.MINUTE_15
        if Timeframes.MINUTE_5 in timeframes_list:
            return Timeframes.MINUTE_5
        if Timeframes.MINUTE_3 in timeframes_list:
            return Timeframes.MINUTE_3

        return Timeframes.MINUTE_1


class colors:
    GREEN = 'green'
    YELLOW = 'yellow'
    RED = 'red'
    MAGENTA = 'magenta'
    BLACK = 'black'


class order_roles:
    OPEN_POSITION = 'OPEN POSITION'
    CLOSE_POSITION = 'CLOSE POSITION'
    INCREASE_POSITION = 'INCREASE POSITION'
    REDUCE_POSITION = 'REDUCE POSITION'


class order_flags:
    OCO = 'OCO'
    POST_ONLY = 'PostOnly'
    CLOSE = 'Close'
    HIDDEN = 'Hidden'
    REDUCE_ONLY = 'ReduceOnly'


class order_types:
    MARKET = 'MARKET'
    LIMIT = 'LIMIT'
    STOP = 'STOP'
    FOK = 'FOK'
    STOP_LIMIT = 'STOP LIMIT'


class exchanges:
    KRAKEN = "Kraken"
    COINBASE = 'Coinbase'
    BITFINEX = 'Bitfinex'
    BINANCE = 'Binance'
    BINANCE_FUTURES = 'Binance Futures'
    TESTNET_BINANCE_FUTURES = 'Testnet Binance Futures'
    SANDBOX = 'Sandbox'
