import sys
from PySide6 import QtWidgets
from manageDb import createTable, addItemToTable
tasks = [
    "hello",
    "welcome",
    "Sohaib",
    "yahya"
]


class TaskCard(QtWidgets.QWidget):
    def __init__(self, card_title: str):
        super().__init__()   # VERY IMPORTANT
        # Main vertical layout
        self.card = QtWidgets.QVBoxLayout(self)

        # Title
        self.taskTitle = QtWidgets.QLabel(card_title)
        self.card.addWidget(self.taskTitle)

        # Buttons
        self.cardAction = QtWidgets.QHBoxLayout()
        self.deleteBtn = QtWidgets.QPushButton("Delete")
        self.doneBtn = QtWidgets.QPushButton("Done")

        self.cardAction.addWidget(self.deleteBtn)
        self.cardAction.addWidget(self.doneBtn)

        self.card.addLayout(self.cardAction)

        self.deleteBtn.clicked.connect(self.deleteItem)

    def deleteItem(self):
        # This will remove the widget from its parent layout and delete it
        self.setParent(None)


class MyWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        createTable(table_name="tasks")
        self.tasks = tasks

        self.titleField = QtWidgets.QPlainTextEdit(placeholderText="Title For Task")
        self.createTaskBtn = QtWidgets.QPushButton("Create Task")

        self.mainLayout = QtWidgets.QHBoxLayout(self)
        self.leftLayout = QtWidgets.QVBoxLayout()
        self.rightLayout = QtWidgets.QVBoxLayout()
        self.mainLayout.addLayout(self.leftLayout)
        self.mainLayout.addLayout(self.rightLayout)
        self.leftLayout.addWidget(self.titleField)
        self.leftLayout.addWidget(self.createTaskBtn)

        self.createTaskBtn.clicked.connect(self.createTask)

        self.showTasks()

    def showTasks(self):
        for task in self.tasks:
            tsk = TaskCard(task)
            self.rightLayout.addWidget(tsk)

    def clean_layout(self, layout):
        if layout is None:
            return
        while layout.count():
            item = layout.takeAt(0)
            if item.widget():
                item.widget().setParent(None)
            elif item.layout():
                self.clean_layout(item.layout())
    
    def createTask(self):
        new_task_text = self.titleField.toPlainText().strip()
        if not new_task_text:
            return

        self.tasks.append(new_task_text)
        addItemToTable({'title':new_task_text}, 'tasks')
        self.titleField.clear()
        self.clean_layout(self.rightLayout)
        self.showTasks()


if __name__ == "__main__":
    app = QtWidgets.QApplication([])

    widget = MyWidget()
    widget.resize(800, 600)
    widget.show()

    sys.exit(app.exec())
