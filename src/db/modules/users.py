"""Module to work with users in database"""


from ..errors import UserExistsError
from .base_database import BaseDatabase


class Users(BaseDatabase):
    """Class to work with users in database"""
    def is_exists(self, login: str) -> bool:
        """Is user exists"""
        # Getting all users from database
        users = self.get_users()

        for user in users:
            # Checking user login
            if user[0] == login:
                return True

        return False

    def get_users(self) -> tuple:
        """Returns list of all users in database"""
        request = f'SELECT * FROM {self.data_table_name}'
        return self.db.execute(request).fetchall()

    def create_user(self, login: str, password: str) -> None:
        """
        Create new user. Causes UserExistsError
        if user with specified login exists
        """
        # Cheking that user gave correct data
        if not isinstance(login, str) or not login.strip():
            raise ValueError('Login must be string and not empty')

        if not isinstance(password, str) or not password.strip():
            raise ValueError('Password must be string and not empty')

        # If user with this login exists
        if self.is_exists(login):
            raise UserExistsError('User with this login already exists')

        # Hashing user password
        password = self.hash_password(password)

        # Data to make request
        request = f'INSERT INTO {self.data_table_name} VALUES(?, ?)'
        data = (login, password)

        # Making request to database
        self.db.execute(request, data)
        self.db.commit()
