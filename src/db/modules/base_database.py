"""Base class for database"""



import os
import sqlite3
import hashlib


class BaseDatabase:
    """Base class for database"""
    def __init__(self,
                 database_folder_path: str,
                 database_file_path: str,
                 data_table_name: str = 'users') -> None:
        """Class initialization"""
        self.data_table_name = data_table_name

        # Creating database folder if it doesn't exists
        if not os.path.exists(database_folder_path):
            os.mkdir(database_folder_path)

        # Connetion to database and creation of
        # data table if it doesn't exists
        self.db = sqlite3.connect(database_file_path)
        self.db.execute(
            f'CREATE TABLE IF NOT EXISTS {data_table_name}(login PRIMARY KEY, password)')

    def hash_password(self, password: str) -> str:
        """Returns hased password using sha256"""
        sha = hashlib.sha256(password.encode())
        return sha.hexdigest()
