from typing import TYPE_CHECKING
from math import pow
from PySide6.QtWidgets import QPushButton, QGridLayout
from PySide6.QtCore import Slot
from variables import MEDIUM_FONT_SIZE
from utils import isNumOrDot, isEmpty, isValidNumber

if TYPE_CHECKING:
    from display import Display
    from info import Info
    from main_window import MainWindow  


class Button(QPushButton):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.configStyle()

    def configStyle(self):
        font = self.font()
        font.setPixelSize(MEDIUM_FONT_SIZE)
        self.setFont(font)
        self.setMinimumSize(50, 50)
        self.setCheckable(False)

class ButtonGrid(QGridLayout):
    def __init__(self, display: 'Display', info: 'Info', window: 'MainWindow', *args, **kwargs):
        super().__init__(*args, **kwargs)

        self._gridMask = [
            ['C', '◀', '^', '/'],
            ['7', '8', '9', '*'],
            ['4', '5', '6', '-'],
            ['1', '2', '3', '+'],
            ['N',  '0', '.', '='],
        ]

        self.display = display
        self.info = info
        self.window = window
        self._equation = ''
        self._left = None
        self._right = None
        self._operator = None
        self._makeGrid()

    @property
    def equation(self):
        return self._equation
    
    @equation.setter
    def equation(self, value):
        self._equation = value
        self.info.setText(value) 

    def _makeGrid(self):
        self.display.eq_presssed.connect(self._equal)
        self.display.del_pressed.connect(self.display.backspace)
        self.display.clear_pressed.connect(self._clear)
        self.display.input_pressed.connect(self._insertToDisplay)
        self.display.operator_pressed.connect(self._configOp)

        for i, row in enumerate(self._gridMask):
            for j, button_text in enumerate(row):
                button = Button(button_text)

                if not isNumOrDot(button_text) and not isEmpty(button_text):
                    button.setProperty('cssClass', 'specialButton')
                    self._configSpecialButton(button)

                self.addWidget(button, i, j)
                button_slot = self._makeSlot(self._insertToDisplay, button_text)
                self._connectButtonClicked(button, button_slot)

    def _connectButtonClicked(self, button, slot):
        button.clicked.connect(slot)
        
    def _configSpecialButton(self, button):
        text = button.text()

        if text == 'C':
            # slot = self._makeSlot( self._clear)               
            self._connectButtonClicked(button, self._clear)
        if text == '◀':
            self._connectButtonClicked(button, self.display.backspace)    
        if text == 'N':
            self._connectButtonClicked(button, self._invertNumber)    
        if text in '+-/*^':
            self._connectButtonClicked(
                button, 
                self._makeSlot(self._configOp, text)
                )    
        if text == '=':
            self._connectButtonClicked(button, self._equal)    

    @Slot() #type: ignore
    def _makeSlot(self, func, *args, **kwargs):
        @Slot(bool) #type: ignore
        def realSlot(_):
            func(*args, **kwargs)
        return realSlot
    
    @Slot()
    def _invertNumber(self):
        display_text = self.display.text()

        if not isValidNumber(display_text):
            return
        
        inverted_number = float(display_text) * (-1)
        self.display.setText(str(inverted_number))

    @Slot() # type: ignore
    def _insertToDisplay(self, text):
        new_display_value = self.display.text() + text
        if not isValidNumber(new_display_value):
            return
        self.display.insert(text)

    @Slot()
    def _clear(self):
        self._left = None
        self._right = None
        self._operator = None
        self.equation = ''
        self.display.clear()

    @Slot() # type: ignore
    def _configOp(self, text):
        display_text = self.display.text() # numero _left
        self.display.clear() # limpa o display

        # Clicou no operador sem colocar nenhum número
        if not isValidNumber(display_text) and self._left is None:
            self._showError('Não há informações para efetuar o cálculo.')
            return
        
        # se houver algo no numero da esquerda não faz nada.
        if self._left is None:
            self._left = float(display_text)

        self._operator = text
        self.equation = f'{self._left} {self._operator} '

    @Slot()
    def _equal(self):
        display_text = self.display.text()

        if not isValidNumber(display_text):
            self._showError('Não foi digitado um valor válido.')
            return
        
        self._right = float(display_text)
        self.equation = f'{self._left} {self._operator} {self._right}'

        try:
            if '^' in self.equation and isinstance(self._left, float):
                result = pow(self._left, self._right)               
            else:
                result = eval(self.equation)
        except ZeroDivisionError:
            self._showError('Não é possível fazer divisão por zero.')
            result = 'Error'
        except OverflowError:
            self._showInfo('O resultado da conta excede o limite de caracteres.')
            result = 'Estouro'

        self.display.clear()
        self.info.setText(f'{self.equation} = {result}')
        self._left = result
        self._right = None
        self._operator = None

        if result == 'Error' or 'Estouro':
            self._left = None

    def _showError(self, text):
        msg_box = self.window.makeMsgBox()
        msg_box.setText(text)
        msg_box.setInformativeText('''Sou um texto informativo''')
        msg_box.setIcon(msg_box.Icon.Warning)

        msg_box.setStandardButtons(
            # msg_box.StandardButton.Ok | 
            msg_box.StandardButton.Cancel
        )

        msg_box.button(msg_box.StandardButton.Cancel).setText('Cancelar')

        msg_box.exec()

    def _showInfo(self, text):
        msg_box = self.window.makeMsgBox()
        msg_box.setText(text)
        msg_box.setInformativeText('''Sou um texto informativo''')
        msg_box.setIcon(msg_box.Icon.Information)

        msg_box.setStandardButtons(
            msg_box.StandardButton.Ok  
        )

        msg_box.exec()