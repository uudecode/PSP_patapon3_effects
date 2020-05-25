import sys
import logging
import dll_corrections
from PyQt5 import QtWidgets
from constants import LOGGING_FORMAT
from application import EditorApp

if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG, format=LOGGING_FORMAT)
    logger = logging.getLogger('Editor Patapon file')
    app = QtWidgets.QApplication(sys.argv)  # Новый экземпляр QApplication
    window = EditorApp()  # Создаём объект класса ExampleApp
    window.show()  # Показываем окно
    app.exec_()  # и запус каем приложение
