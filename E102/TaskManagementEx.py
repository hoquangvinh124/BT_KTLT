import datetime
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import QMessageBox, QListWidgetItem
from FileFactory import FileFactory
from E102.TaskManagement import Ui_MainWindow
from Task import Task
from Tasks import Tasks

class MainWindowEx(Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.tasks = Tasks()
        self.file_factory = FileFactory()
        self.selected_task = None

    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow = MainWindow
        arr_data = self.file_factory.read_data("database.json", Task)
        self.tasks.add_all(arr_data)
        self.show_tasks_into_q_list_widget()
        self.pushButtonNew.clicked.connect(self.process_new)
        self.pushButtonSave.clicked.connect(self.process_save)
        self.pushButtonRemove.clicked.connect(self.process_remove)
        self.listWidgetTask.itemSelectionChanged.connect(self.process_item_selection)

    def show_tasks_into_q_list_widget(self):
        self.listWidgetTask.clear()
        for index in range(self.tasks.size()):
            task = self.tasks.get_item(index)
            item = QListWidgetItem()
            item.setData(Qt.ItemDataRole.UserRole, task)
            item.setText(str(task))
            item.setCheckState(Qt.CheckState.Unchecked)
            if task.isfinish:
                item.setIcon(QIcon("images/ic_finished.png"))
            else:
                item.setIcon(QIcon("images/ic_notfinished.png"))
            if isinstance(task.deadline, str):
                task.deadline = datetime.date.fromisoformat(task.deadline)
            if isinstance(task.deadlinetime, str):
                task.deadlinetime = datetime.time.fromisoformat(task.deadlinetime)
            self.listWidgetTask.addItem(item)

    def process_new(self):
        self.lineEditTitle.setText("")
        self.textEditContent.setText("")
        self.dateEditDeadline.setSpecialValueText(None)
        self.radFinished.setAutoExclusive(False)
        self.radNotFinished.setAutoExclusive(False)
        self.radFinished.setChecked(False)
        self.radNotFinished.setChecked(False)
        self.radFinished.setAutoExclusive(True)
        self.radNotFinished.setAutoExclusive(True)
        self.selected_task = None
        self.lineEditTitle.setFocus()

    def process_save(self):
        title = self.lineEditTitle.text()
        content = self.textEditContent.toPlainText()
        date = self.dateEditDeadline.date().toPyDate()
        time = self.timeEditDeadline.time().toPyTime()
        is_finished = self.radFinished.isChecked()
        task = Task(title, content, date, time, is_finished)
        if self.selected_task is None:
            self.tasks.add(task)
        else:
            index = self.tasks.get_index(self.selected_task)
            self.tasks.update(index, task)
        self.selected_task = task
        self.show_tasks_into_q_list_widget()
        self.file_factory.write_data("database.json", self.tasks.task_list)

    def process_remove(self):
        answer = QMessageBox.question(
            self.MainWindow,
            'Confirmation',
            'Do you want to remove checked Items?',
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No
        )
        if answer == QMessageBox.StandardButton.No:
            return
        size = self.listWidgetTask.count()
        for index in range(size - 1, -1, -1):
            item = self.listWidgetTask.item(index)
            if item.checkState() == Qt.CheckState.Checked:
                self.tasks.remove_by_index(index)
        self.selected_task = None
        self.show_tasks_into_q_list_widget()
        self.file_factory.write_data("database.json", self.tasks.task_list)

    def process_item_selection(self):
        row = self.listWidgetTask.currentRow()
        task = self.tasks.get_item(row)
        self.lineEditTitle.setText(task.title)
        self.textEditContent.setText(task.content)
        self.dateEditDeadline.setDate(task.deadline)
        self.timeEditDeadline.setTime(task.deadlinetime)
        if task.isfinish:
            self.radFinished.setChecked(True)
            self.radNotFinished.setChecked(False)
        else:
            self.radFinished.setChecked(False)
            self.radNotFinished.setChecked(True)
        self.selected_task = task

    def show(self):
        self.MainWindow.show()
