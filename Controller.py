#!/usr/bin/python
import sys
import Operations
import DB_Handler as db
from Connections import ExchangeController


class Controller:   # Main Controller class that will handle all top level execution

    OPS = object    # Operations Handler
    DB = object     # Database Handler
    Exchange = object   # Exchange Handler
    selected_exchange = 0
    bot_id = 0
    USER = None

    def __init__(self):
        self.OPS = Operations.Ops()
        self.DB = db.DBHandler(self.OPS)
        self.Exchange = ExchangeController.ExchangeConn(self.DB)   # Instantiate ExchangeController and pass DB Instance
        self.selected_exchange = int(sys.argv[1])    # Argument 1 from cmdline will be our preferred exchange
        self.mode = sys.argv[2]     # Argument 2 dictates the mode that the Controller will run in
        self.bot_id = sys.argv[3]

    def orchestrator(self):
        auth, self.USER = self.DB.login(self.mode)  # Authenticate Session. Return Bool and User
        if auth:
            print("=> Active User: [" + self.USER + "]")
            active_exchange = self.Exchange.selector(self.selected_exchange, self.mode, self.bot_id)    # Grab selected exchange obj
        else:
            print("=> You Do Not Have Access. Shutting Down.")


if __name__ == "__main__":
    controller = Controller()
    controller.orchestrator()
