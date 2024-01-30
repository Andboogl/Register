"""Database class"""


from . import errors
from .modules import Users


class Database(Users):
    """Database"""
    def login(self, login: str, password: str) -> bool:
        """
        Try to login to account. Returns
        true if attemp passed successfully
        """
        # Checking that user gave correct data
        if not isinstance(login, str) or not login.strip():
            raise ValueError('Login must be string and not empty')

        if not isinstance(password, str) or not password.strip():
            raise ValueError('Password must be string and not empty')

        # Checking for user existence
        if not self.is_exists(login):
            raise errors.UserNotFoundError('User with this login doesn\'t exists')

        # Checking password
        request_password = f'SELECT password FROM {self.data_table_name} WHERE login == ?'
        data = (login,)
        password_ = self.db.execute(
            request_password, data).fetchone()[0]

        # If passwords match
        if password_ == self.hash_password(password):
            return True

        return False
