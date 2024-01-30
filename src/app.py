"""Main window"""


from PyQt6.QtWidgets import QMainWindow, QMessageBox
from design import MainWindowDesign
from db import Database
from db import errors as database_errors
import settings


def show_message(window: QMainWindow, text: str) -> None:
    """Show warning message"""
    msg = QMessageBox(window)
    msg.setText(text)
    msg.exec()


class MainWindow(QMainWindow):
    """Apllication main window"""
    def __init__(self, parent: None = None) -> None:
        """Class initialization"""
        super().__init__(parent)

        # Loading design
        self.design = MainWindowDesign()
        self.design.setupUi(self)

        # Connection to database
        self.db = Database(settings.DATABASE_FOLDER_PATH, settings.DATABASE_FILE_PATH)

        # Buttons pressing
        self.design.create_account.clicked.connect(self.create_account)
        self.design.create_account_menubar.triggered.connect(self.create_account)
        self.design.sing_in.clicked.connect(self.sing_in)
        self.design.sing_in_menubar.triggered.connect(self.sing_in)

    def create_account(self) -> None:
        """Create account"""
        login = self.design.login.text()
        password = self.design.password.text()

        try:
            self.db.create_user(login, password)

        except ValueError:
            show_message(self, 'Enter all data')

        except database_errors.UserExistsError:
            show_message(self, 'User with this login already exists')

    def sing_in(self) -> None:
        """Sing in to an account"""
        login = self.design.login.text()
        password = self.design.password.text()

        try:
            attemp = self.db.login(login, password)

            if attemp:
                show_message(self, 'Successflly singned in!')

            elif not attemp:
                show_message(self, 'Password is incorrect')

        except database_errors.UserNotFoundError:
            show_message(self, 'User with this login doesn\'t exists')

        except ValueError:
            show_message(self, 'Enter all data')
