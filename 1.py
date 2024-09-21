from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout,
    QLineEdit, QTextEdit, QPushButton
)

class NoteApp(QWidget):
    def __init__(self) :
        super().__init__()
        self.init_ui()
        
    def init_ui(self):
        self.setWindowTitle("Oddiy Note oluvchi ilova")
        self.setGeometry(100,100,400,300)
        
        
        self.note_input = QLineEdit(self)
        self.note_input.setPlaceholderText("Note kiriting...")
        
        self.notes_display = QTextEdit(self)
        self.notes_display.setReadOnly(True)
        
        
        self.save_button = QPushButton("Saqlash", self)
        self.save_button.clicked.connect(self.save_note)
        
        layout = QVBoxLayout()
        layout.addWidget(self.note_input)
        layout.addWidget(self.save_button)
        layout.addWidget(self.notes_display)
        
        self.setLayout(layout)
        
        
    def save_note(self):
        note = self.note_input.text()
        
        if note:
            current_notes = self.notes_display.toPlainText()
            new_notes = current_notes + note + '\n'
            self.notes_display.setPlainText(new_notes)
            self.note_input.clear()
            
            
App = QApplication([])
window = NoteApp()
window.show()
App.exec_()            
            
            
            
            
            
            