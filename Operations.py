import os
import hashlib


class Ops:

    def login_prompt(self):

        print("\n")
        username = input("Username: ")
        password = input("Password: ")
        password = hashlib.sha256(password.encode('utf-8')).hexdigest()  # Hash password

        return username, password
