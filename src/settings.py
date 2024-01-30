"""Application settings"""


import os


DATABASE_FOLDER_PATH = os.path.join(os.path.expanduser('~'), '.register')
DATABASE_FILE_PATH = os.path.join(DATABASE_FOLDER_PATH, 'users.db')
