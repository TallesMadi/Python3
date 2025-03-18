import os
os.environ['QT_API'] = 'pyside6'

import sys, main_window, display, info
from styles import setupTheme
from PySide6.QtWidgets import QApplication
from PySide6.QtGui import QIcon
from button import ButtonGrid
from variables import WINDOW_ICON_PATH

if __name__ == '__main__':
    # Cria a aplicação
    app = QApplication(sys.argv)
    setupTheme(app)
    window = main_window.MainWindow()

    # Define o icone
    icon = QIcon(str(WINDOW_ICON_PATH))
    window.setWindowIcon(icon)

    # Info
    info_ = info.Info('')
    window.addWidgetVLayout(info_)

    # Display
    display_ = display.Display()
    # display.setPlaceholderText('Digite Algo')
    window.addWidgetVLayout(display_)

    # Grid
    buttonGrid = ButtonGrid(display_, info_, window)
    window.vLayout.addLayout(buttonGrid)

    # Executa tudo
    window.adjustFixedSize()
    window.show()
    app.exec()
