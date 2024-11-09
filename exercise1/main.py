import sys
from PySide6.QtWidgets import QApplication
from exercise_gui import ExerciseGui
from simulate_axes import SimulateAxes


if __name__ == '__main__':
    app = QApplication()
    axes = SimulateAxes()
    axes.start()
    window = ExerciseGui()
    window.show()
    return_code = app.exec()
    axes.stop()
    sys.exit(return_code)
