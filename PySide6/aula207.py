# QApplication e QPushButton de PySide6.QtWidgets
# QApplication -> O Widget principal da aplicação
# QPushButton -> Um botão
# QWidget e QLayout de PySide6.QtWidgets
# QWidget -> genérico
# QLayout -> Um widget de layout que recebe outros widgets
# PySide6.QtWidgets -> Onde estão os widgets do PySide6
import sys
from PySide6.QtWidgets import QApplication, QPushButton, QWidget, QVBoxLayout, QGridLayout

app = QApplication(sys.argv)

button = QPushButton('Botão inútil')
button.setStyleSheet('font-size: 30px; color: darkblue; background-color: pink')
# button.show() # adiciona o widget na hierarquia e exibe na janela

button2 = QPushButton('Botão inútil 2')
button2.setStyleSheet('font-size: 30px; color: salmon; background-color: cyan')

button3 = QPushButton('Botão inútil 3')
button3.setStyleSheet('font-size: 30px; color: black; background-color: white')

central_widget = QWidget()

layout = QVBoxLayout()
grid_layout = QGridLayout()
# central_widget.setLayout(layout)
central_widget.setLayout(grid_layout)

# layout.addWidget(button)
# layout.addWidget(button2)

grid_layout.addWidget(button, 1, 1, 1, 1)
grid_layout.addWidget(button2, 1, 2, 1, 1)
grid_layout.addWidget(button3, 3, 1, 1, 2)

central_widget.show()
app.exec()
