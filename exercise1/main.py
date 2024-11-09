import sys
from PySide6.QtWidgets import QApplication
from exercise_gui import ExerciseGui


if __name__ == '__main__':
    app = QApplication()
    window = ExerciseGui()
    window.show()
    return_code = app.exec()
    sys.exit(return_code)
