import os
import shutil
import re
from PyQt5.QtWidgets import QApplication, QFileDialog, QMainWindow, QPushButton, QVBoxLayout, QWidget

class FileOrganizer(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
    
    def initUI(self):
        self.setWindowTitle('Photo Organizer')
        self.setGeometry(100, 100, 300, 150)

        layout = QVBoxLayout()

        self.btn_select_folder = QPushButton('Select Folder', self)
        self.btn_select_folder.clicked.connect(self.select_folder)
        layout.addWidget(self.btn_select_folder)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)
    
    def select_folder(self):
        folder = str(QFileDialog.getExistingDirectory(self, "Select Directory"))
        if folder:
            self.organize_photos(folder)
    
    def organize_photos(self, folder):
        for filename in os.listdir(folder):
            if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp', '.mp4')):
                # 이 부분의 정규식을 파일 이름 형식에 맞게 수정
                # date_match = re.search(r'(\d{4})(\d{2})(\d{2})', filename)
                date_match = re.search(r'(\d{4})-(\d{2})-(\d{2})', filename)
                if date_match:
                    year, month, day = date_match.groups()
                    date_folder = os.path.join(folder, f"{year}-{month}-{day}")
                    if not os.path.exists(date_folder):
                        os.makedirs(date_folder)
                    shutil.move(os.path.join(folder, filename), os.path.join(date_folder, filename))

if __name__ == '__main__':
    app = QApplication([])
    ex = FileOrganizer()
    ex.show()
    app.exec_()
