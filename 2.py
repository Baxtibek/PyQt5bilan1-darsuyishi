from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout,
    QLineEdit, QTextEdit, QPushButton   
)

class UserInfoApp(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()
        
    def init_ui(self):
        self.setWindowTitle("Foydalanuvchi ma'lumot formasi")
        self.setGeometry(100,100,400,400)
        
        self.ism_input = QLineEdit(self)
        self.ism_input.setPlaceholderText("Ismingizni kiriting...")
        
        self.email_input = QLineEdit(self)
        self.email_input.setPlaceholderText("Elektron pochatngizni kiriting...")
        
        self.bio_input = QLineEdit(self)
        self.bio_input.setPlaceholderText("Qisqacha tarjimai hol kiriting...")
        
        self.sumbit_button = QPushButton("Yuborish", self)
        self.sumbit_button.clicked.connect(self.display_info)
        
        self.info_display = QTextEdit(self)
        self.info_display.setReadOnly(True)
        
        
        layout = QVBoxLayout()
        layout.addWidget(self.ism_input)
        layout.addWidget(self.email_input)
        layout.addWidget(self.bio_input)
        layout.addWidget(self.sumbit_button)
        layout.addWidget(self.info_display)
        
        self.setLayout(layout)


    def display_info(self):
        ism = self.ism_input.text()
        email = self.email_input.text()
        bio = self.bio_input.text() 
        
               
        user_info = f"Ism: {ism}\Email: {email}\nTarjimai hol: {bio}\n"
        
        
        self.info_display.setPlainText(user_info)        
        
        
        
        
App = QApplication([])
window = UserInfoApp()
window.show()
App.exec_()
        
        
        
        
        
        
        
        
        