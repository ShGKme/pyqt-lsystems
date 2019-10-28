import sys

from PyQt5.QtWidgets import QApplication

from ui.views.main_form import MainForm

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_form = MainForm()
    main_form.show()
    sys.exit(app.exec())
