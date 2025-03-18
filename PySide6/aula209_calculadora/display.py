from PySide6.QtGui import QKeyEvent
from PySide6.QtWidgets import QLineEdit
from PySide6.QtCore import Qt, Signal
from variables import BIG_FONT_SIZE, TEXT_MARGIN, MINIMUM_WIDTH
from utils import isEmpty, isNumOrDot

class Display(QLineEdit):
    eq_presssed = Signal()
    del_pressed = Signal()
    clear_pressed = Signal()
    input_pressed = Signal(str)
    operator_pressed  = Signal(str)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.configStyle()

    def configStyle(self):
        self.setStyleSheet(f'font-size: {BIG_FONT_SIZE}px')
        self.setMinimumHeight(BIG_FONT_SIZE * 2)
        self.setMinimumWidth(MINIMUM_WIDTH)
        self.setAlignment(Qt.AlignmentFlag.AlignRight)
        self.setTextMargins(*[TEXT_MARGIN for _ in range(4)])
    
    def keyPressEvent(self, event: QKeyEvent) -> None:
        text = event.text().strip()
        key = event.key()
        KEYS = Qt.Key

        is_enter = key in [KEYS.Key_Enter, KEYS.Key_Return, KEYS.Key_Equal]
        is_backspace = key in [KEYS.Key_Backspace, KEYS.Key_Delete, KEYS.Key_D]
        is_esc = key in [KEYS.Key_Escape, KEYS.Key_C]
        is_operator = key in [KEYS.Key_Plus, KEYS.Key_Minus, KEYS.Key_Slash, KEYS.Key_Asterisk, KEYS.Key_P]

        if is_enter:
            self.eq_presssed.emit()
            return event.ignore()
        if is_backspace:
            self.del_pressed.emit()
            return event.ignore()
        if is_esc:
            self.clear_pressed.emit()
            return event.ignore()
        if is_operator:
            if text.lower() == 'p':
                text = '^'
            self.operator_pressed.emit(text)
            return event.ignore()

        # Não passa daqui se não tiver texto
        if isEmpty(text):
            return event.ignore()
        
        if isNumOrDot(text):
            self.input_pressed.emit(text)
            return event.ignore()
            