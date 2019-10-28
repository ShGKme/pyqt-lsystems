from PyQt5.QtWidgets import QWidget, QFileDialog

from core.lsystem import LSystem
from ui.built.ui_main_form import Ui_MainForm


class MainForm(QWidget, Ui_MainForm):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.open_file_button.clicked.connect(self.choose_definition_file)
        self.evolution_step_spin.valueChanged.connect(self.paint)
        self.init_x_spin.valueChanged.connect(self.paint)
        self.init_y_spin.valueChanged.connect(self.paint)
        self.step_length_spin.valueChanged.connect(self.paint)
        self.lsystem = None
        self.open_sample()

    def open_sample(self):
        self.evolution_step_spin.setValue(3)
        self.init_x_spin.setValue(100)
        self.init_y_spin.setValue(0)
        self.step_length_spin.setValue(10)
        self.open_definition_file('./samples/tree.ls')

    def choose_definition_file(self):
        file_name = QFileDialog.getOpenFileName(self, 'Определение L-системы', '', 'Определение L-системы (*.ls)')[0]
        self.open_definition_file(file_name)
        return file_name

    def open_definition_file(self, file_name):
        with open(file_name, 'r', encoding='UTF-8') as file:
            self.open_definition(file.read())

    def open_definition(self, definition):
        self.lsystem = LSystem(definition)
        self.file_name_edit.setText(self.lsystem.name)
        self.definition_text.setPlainText(self.lsystem.definition)
        self.paint()

    def paint(self):
        if not self.lsystem:
            return
        self.lsystem.reset()
        self.lsystem.evolve_to(self.evolution_step_spin.value())
        self.paint_frame.paint(init_x=self.init_x_spin.value(),
                              init_y=self.init_y_spin.value(),
                              length=self.step_length_spin.value(),
                              lsystem=self.lsystem)
