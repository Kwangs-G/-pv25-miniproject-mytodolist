import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QHBoxLayout,
    QLabel, QLineEdit, QComboBox, QPushButton,
    QListWidget, QMessageBox
)
from PyQt5.QtGui import QFont, QColor
from PyQt5.QtCore import Qt

class ToDoApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("To Do List Tugas Pember")
        self.setGeometry(300, 150, 500, 400)

        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()
    
        label_info = QLabel("Nama: Fernandao Kwangtama Tekayadi  |  NIM: F1D022120")
        label_info.setFont(QFont("Arial", 10, QFont.Bold))
        label_info.setStyleSheet("color: darkblue")
        layout.addWidget(label_info)

        input_layout = QHBoxLayout()

        self.task_input = QLineEdit()
        self.task_input.setPlaceholderText("Masukkan Kegiatan")
        self.task_input.setMinimumWidth(200)
        self.task_input.setMinimumHeight(30)

        self.category_box = QComboBox()
        self.category_box.addItems(["Kuliah", "Pribadi", "Lainnya"])
        self.category_box.setMinimumHeight(30)

        input_layout.addWidget(self.task_input)
        input_layout.addWidget(self.category_box)

        layout.addLayout(input_layout)

        button_layout = QHBoxLayout()

        self.add_button = QPushButton("Tambah Kegiatan")
        self.add_button.setStyleSheet("background-color: lightgreen; font-weight: bold;")
        self.add_button.clicked.connect(self.add_task)

        self.delete_button = QPushButton("Hapus Kegiatan")
        self.delete_button.setStyleSheet("background-color: lightcoral; font-weight: bold;")
        self.delete_button.clicked.connect(self.delete_task)

        self.priority_button = QPushButton("Prioritas")
        self.priority_button.setStyleSheet("background-color: lightblue; font-weight: bold;")
        self.priority_button.clicked.connect(self.set_priority)

        button_layout.addWidget(self.add_button)
        button_layout.addWidget(self.delete_button)
        button_layout.addWidget(self.priority_button)

        layout.addLayout(button_layout)

        self.task_list = QListWidget()
        self.task_list.setMinimumHeight(200)
        layout.addWidget(self.task_list)

        self.setLayout(layout)

    def add_task(self):
        task = self.task_input.text().strip()
        category = self.category_box.currentText()

        if not task:
            QMessageBox.warning(self, "Warning !", "Kegiatan tidak boleh kosong!")
            return

        formatted_task = f"{task} ({category})"
        self.task_list.addItem(formatted_task)
        self.task_input.clear()

    def delete_task(self):
        selected_items = self.task_list.selectedItems()
        if not selected_items:
            QMessageBox.information(self, "Info", "Pilih kegiatan yang ingin dihapus.")
            return
        for item in selected_items:
            self.task_list.takeItem(self.task_list.row(item))

    def set_priority(self):
        selected_items = self.task_list.selectedItems()
        if not selected_items:
            QMessageBox.information(self, "Info", "Pilih kegiatan untuk diberi prioritas.")
            return

        for item in selected_items:
            text = item.text()
            current_color = item.background().color()

            text = (
                text.replace("[Prioritas Tinggi]", "")
                    .replace("[Prioritas Sedang]", "")
                    .replace("[Prioritas Rendah]", "")
                    .strip()
            )

            if current_color == QColor("white") or current_color == QColor(0, 0, 0, 0):
                item.setBackground(QColor("red"))
                item.setText(f"{text} [Prioritas Tinggi]")
            elif current_color == QColor("red"):
                item.setBackground(QColor("yellow"))
                item.setText(f"{text} [Prioritas Sedang]")
            elif current_color == QColor("yellow"):
                item.setBackground(QColor("lightgreen"))
                item.setText(f"{text} [Prioritas Rendah]")
            else:
                item.setBackground(QColor("white"))
                item.setText(text)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ToDoApp()
    window.show()
    sys.exit(app.exec_())
