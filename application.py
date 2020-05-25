import logging
from pathlib import Path
from struct import unpack_from, pack_into
from constants import NOTES_FILE, INITIAL_GAP, BLOCK_SIZE, END_POINTER, STRINGS, SHORTS, \
    SHORT_FORMAT

from PyQt5 import QtWidgets, QtCore
from PyQt5.QtGui import QStandardItemModel, QStandardItem, QIntValidator, QDoubleValidator

import editor


class EditorApp(QtWidgets.QMainWindow, editor.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self._logger = logging.getLogger('Editor Patapon Effect file')
        self._logger.setLevel(logging.DEBUG)
        self.setupUi(self)  # Это нужно для инициализации нашего дизайна
        self.openFileButton.clicked.connect(self.open_file)
        self.exitButton.clicked.connect(self.exit_app)
        self.saveFileButton.clicked.connect(self.save_file)
        self.comboBox.currentTextChanged.connect(self.process_item)
        self._file_content = None
        self._notes_file_content: str = ''
        self._all_effects = []
        self._file_name = None
        self._notes_file_name = None
        self._item_model = QStandardItemModel(self.comboBox)

        self._only_int = QIntValidator()
        self._only_float = QDoubleValidator()
        self._only_short = QIntValidator()
        self._bck = None
        # self.set_validators()
        # self.set_processor()

    def process_item(self, text):
        self._logger.debug('Process item')
        offset = next(item for item in self._all_effects if item[0] == text)[1]
        block = self._file_content[offset:offset + BLOCK_SIZE]
        self._logger.debug(block)
        for element in STRINGS:
            value = block[element[0]: element[0] + element[2]].decode('utf-8').strip('\x00')
            line_edit = self.findChild(QtWidgets.QLineEdit, element[1])
            if line_edit is not None:
                line_edit.setText(value)
                line_edit.setReadOnly(False)
        for element in SHORTS:
            value = unpack_from(SHORT_FORMAT, block, element[0])[0]
            self._logger.debug('Value: %s', value)
            line_edit = self.findChild(QtWidgets.QLineEdit, element[1])
            if line_edit is not None:
                line_edit.setText(str(value))
                line_edit.setReadOnly(False)

    def save_file(self):
        self._logger.debug('Saving file')
        if self._file_name is None:
            error_dialog = QtWidgets.QErrorMessage()
            error_dialog.showMessage('Файл не загружен, нечего сохранять!')
            error_dialog.setWindowTitle("Ошибка")
            error_dialog.exec_()
        else:

            try:
                with open(self._file_name, 'wb') as data_file:
                    data_file.write(self._file_content)
            except Exception:
                self._logger.exception('Невозможно сохранить основной файл эффектов')

            try:
                with open(self._notes_file_name, 'wt') as data_file:
                    data_file.write(self._notes_file_content)
            except Exception:
                self._logger.exception('Невозможно сохранить файл примечаний')

    def get_all_effects(self):
        pointer: int = INITIAL_GAP
        loaded_quantity: int = 0
        self._all_effects = []
        while pointer < END_POINTER:
            effect_name = self._file_content[pointer: pointer + 0x10].decode('utf-8').strip('\x00')
            self._all_effects.append((effect_name, pointer, id))
            item = QStandardItem(effect_name)
            self._item_model.appendRow(item)
            pointer += BLOCK_SIZE
            loaded_quantity += 1
        self._logger.debug(self._all_effects)
        self.comboBox.setModel(self._item_model)
        self.loadedCount.display(loaded_quantity)

    def open_file(self):
        self._logger.debug('Opening file')
        try:
            input_file = QtWidgets.QFileDialog.getOpenFileName(self, 'Выберите файл')
            self._file_name = input_file[0]
            self._logger.info('Input file: %s', self._file_name)
            with open(self._file_name, 'rb') as data_file:
                self._file_content = bytearray(data_file.read())
            self._bck = self._file_content.copy()
            file_length = len(self._file_content)
            self._logger.info('Read %s bytes', file_length)
            if self._file_content[0:6] != bytearray.fromhex('5947465f4746'):
                error_dialog = QtWidgets.QErrorMessage()
                error_dialog.showMessage('Неопознанный формат файла!')
                error_dialog.setWindowTitle("Ошибка")
                error_dialog.exec_()
                raise ValueError('Неопознанный формат файла!')
            self.fileName.setText(input_file[0])
            self.get_all_effects()
            self.centralwidget.setWindowTitle(f'Patapon Resource file editor: {input_file[0]}')
        except Exception:
            self._logger.exception('При открытии файла произошла ошибка')
            self._notes_file_name = None
            self._file_name = None
            self._file_content = None
            self._notes_file_content = ''
            self._all_effects = []
            self.item_model = QStandardItemModel(self.comboBox)
            self.fileName.setText('')
        try:
            main_file_path = Path(self._file_name)
            self._notes_file_name = f'{main_file_path.parent}/{NOTES_FILE}'
            notes_file_path = Path(self._notes_file_name)
            if notes_file_path.exists():
                with open(self._notes_file_name, 'rt') as notes_file:
                    self._notes_file_content = notes_file.readlines()
        except Exception:
            self._logger.exception('При открытии файла примечаний произошла ошибка')
            self._notes_file_name = None
            self._file_name = None
            self._file_content = None
            self._notes_file_content = ''
            self._all_effects = []
            self.item_model = QStandardItemModel(self.comboBox)
            self.fileName.setText('')

    def exit_app(self):
        self._logger.info('Exiting')
        QtCore.QCoreApplication.instance().quit()
