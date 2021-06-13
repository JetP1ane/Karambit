import os
import hashlib
import sqlite3


class DBHandler:

    SQL_PATH = "C:\\Karambit.db"    # TODO: Move to GLOBAL Bots Config File
    dbConn = object
    OPS = object
    USER = None
    USER_ID = None

    def __init__(self, OPS):
        self.OPS = OPS
        self.dbConn = self.db_connect()
        self.modes = {  # Controller Modes
           "scanner": "SCAN",
           "trader": "TRADE"
       }

    # DB Connection
    def db_connect(self):
        try:
            conn = sqlite3.connect(self.SQL_PATH)
            conn.row_factory = sqlite3.Row
            print("Connected to DB")
            return conn
        except Exception as e:
            print("DB Connection Failed: " + str(e))

    # DB Authentication for User
    def login(self, mode):
        if self.modes[mode] != "SCAN":  # If running in any other mode besides SCAN, authenticate user

            username, password = self.OPS.login_prompt()   # Call on login prompt and store results

            cur = self.dbConn.cursor()
            cur.execute("SELECT id FROM Users WHERE username = ? AND password = ?", (username, password.upper()))
            rows = cur.fetchone()

            if len(rows) == 1:
                print("=> Logged in " + username)
                self.USER = username
                self.USER_ID = rows[0]  # Used for DB Queries
                return True, username   # Return True for authentication and Active User
            else:
                print("=> Failed to Authenticate User")
                return False

        else:
            return True

    # Fetch RESTful Keys for User
    def get_keys(self, exchange):

        keys = {}
        cur = self.dbConn.cursor()
        cur.execute("SELECT " + exchange + "_key," + exchange + "_secret FROM Users WHERE username=?",
                    (self.USER,))
        rows = cur.fetchall()
        if len(rows) > 0:
            for row in rows:
                keys['api'] = row[0]
                keys['secret'] = row[1]

        return keys

    # Fetch Requested BOT Associated Settings
    def fetch_bot_settings(self, bot_id):

        settings = {}
        cur = self.dbConn.cursor()
        cur.execute("SELECT * FROM Bots WHERE user=? and id=?",
                    (self.USER_ID, bot_id,))
        rows = cur.fetchone()

        settings['bot_type'] = rows['bot_type']
        settings['coins'] = rows['coins']

        return settings


