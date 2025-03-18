# QSS - Estilos do Qt for Python
# https://doc.qt.io/qtforpython-6/tutorials/basictutorial/widgetstyling.html
import qdarkstyle
from variables import PRIMARY_COLOR, DARKER_PRIMARY_COLOR, DARKEST_PRIMARY_COLOR

qss = f"""
    QPushButton[cssClass="specialButton"] {{
        color: #fff;
        background: {PRIMARY_COLOR};
        border-radius: 5px;
    }}
    QPushButton[cssClass="specialButton"]:hover {{
        color: #fff;
        background: {DARKER_PRIMARY_COLOR};
    }}
    QPushButton[cssClass="specialButton"]:pressed {{
        color: #fff;
        background: {DARKEST_PRIMARY_COLOR};
    }}
"""
def setupTheme(app):
    dark_stylesheet = qdarkstyle.load_stylesheet()
    combined_stylesheet = dark_stylesheet + qss
    app.setStyleSheet(combined_stylesheet)

