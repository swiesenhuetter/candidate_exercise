import sys
from PySide6.QtWidgets import QApplication

from exercise1.zaber_axes import ZaberAxes
from exercise_gui import ExerciseGui
from simulate_axes import SimulateAxes


if __name__ == '__main__':
    app = QApplication()
    # axes = SimulateAxes()
    axes = ZaberAxes()
    axes.start()
    window = ExerciseGui(axes)
    window.show()
    return_code = app.exec()
    axes.stop()
    sys.exit(return_code)
