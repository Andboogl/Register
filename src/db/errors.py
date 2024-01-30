"""Database errors"""



class UserExistsError(Exception):
    """
    Error when user exists
    (on user creation)
    """



class UserNotFoundError(Exception):
    """
    Error when user doesn't exists
    (on singning to account)
    """
