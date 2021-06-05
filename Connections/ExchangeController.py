import os
from Connections import Binance


class ExchangeConn:

    exchanges = {}

    def __init__(self, db):

        self.DB = db
        self.modes = {  # Controller Modes
            "scanner": "SCAN",
            "trader": "TRADE"
        }
        self.exchanges = {  # Exchange Dictionary
            0: self.binance,
            1: self.bitmex
        }

    def selector(self, exchange, mode, bot_id):   # Select exchange connection
        return self.exchanges[exchange](str(self.modes[mode]), bot_id)

    def binance(self, mode, bot_id):  # Binance exchange RESTful obj
        keys = self.DB.get_keys('binance')   # Fetch specified exchange RESTful Keys
        binance = Binance.BinanceOperators(mode, self.DB, keys, bot_id)   # Instantiate BinanceOperator and pass DB Instance
        binance.binance_orchestrator()

    # TODO: Build Bitmex RESTful Connection
    def bitmex(self, mode, bot_id):   # Bitmex exchange RESTful obj
        print('')
