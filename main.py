import sys
from PySide6 import QtWidgets

class MyWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.titleField = QtWidgets.QPlainTextEdit(placeholderText="Title For Task")
        self.createTaskBtn = QtWidgets.QPushButton("Create Task")
        
        self.mainLayout = QtWidgets.QHBoxLayout(self)
        self.leftLayout = QtWidgets.QVBoxLayout()
        self.rightLayout = QtWidgets.QVBoxLayout()
        self.mainLayout.addLayout(self.leftLayout)
        self.mainLayout.addLayout(self.rightLayout)
        self.leftLayout.addWidget(self.titleField)
        self.leftLayout.addWidget(self.createTaskBtn)
        
if __name__ == "__main__":
    app = QtWidgets.QApplication([])

    widget = MyWidget()
    widget.resize(800, 600)
    widget.show()

    sys.exit(app.exec())
