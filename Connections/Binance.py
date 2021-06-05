import os
from RESTful import HTTP


class BinanceOperators:    # Handles all Binance related functions

    MODE = 'Scanning'
    DB = object
    http = object

    def __init__(self, mode, db, keys, bot_id):
        self.MODE = mode
        self.DB = db
        self.bot_id = bot_id    # Requested BOT ID#
        self.api_key = keys['api']
        self.secret = keys['secret']
        self.http = HTTP.APIController("https://api.binance.com/api/v3/")

    # Coordinates all Binance functions
    def binance_orchestrator(self):

        print("\n=> Binance BOT Now Running")
        print("=> Active Mode: [" + self.MODE + "]")

        if self.test_conn():
            print('=> Connected to Binance RESTful')
            self.fetch_settings()   # Fetch and establish BOT settings
        else:
            print("=> %Error Connecting to Binance")

    # TODO Pull BOT Settings from BOTS Data Table by BotID and set variables. Then Initiate Bot
    def fetch_settings(self):

        settings = self.DB.fetch_bot_settings(self.bot_id)
        print(settings)
        return True

    # TODO Build BOT Trading Functions

    # Communicates with HTTP library for RESTful requests
    def requester(self, ext, data):
        request = self.http.http_request(ext, '')
        if request:
            return request
        else:
            return False

    # Ping Test with RESTful EndPoint
    def test_conn(self):
        url_ext = "ping"
        return self.requester(url_ext, '')

    # Fetches Exchange Data
    def exchange_info(self):
        url_ext = "exchangeInfo"
        return self.requester(url_ext, '')

    def fetch_klines(self):
        url_ext = 'klines'
        return self.requester(url_ext, '')