from PySide6.QtWidgets import (QMainWindow,
                               QWidget,
                               QLCDNumber,
                               QSlider,
                               QGridLayout,
                               QPushButton)


class ExerciseGui(QMainWindow):
    def __init__(self):
        super().__init__()

        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        self.setWindowTitle("Exercise 1")
        self.setGeometry(100, 100, 400, 200)

        self.slider_left = QSlider()
        self.slider_left.valueChanged.connect(self.set_left_position)
        self.slider_right = QSlider()
        self.slider_right.valueChanged.connect(self.set_right_position)
        # min 0.0, max 4.0 mm, step 0.1 mm
        self.slider_left.setMinimum(0)
        self.slider_left.setMaximum(40)
        self.slider_left.setSingleStep(1)
        self.slider_right.setMinimum(0)
        self.slider_right.setMaximum(40)
        self.slider_right.setSingleStep(1)

        self.left_position = QLCDNumber()
        self.right_position = QLCDNumber()
        layout = QGridLayout()
        layout.addWidget(self.slider_left, 0, 0)
        layout.addWidget(self.left_position, 0, 1)
        layout.addWidget(self.slider_right, 1, 0)
        layout.addWidget(self.right_position, 1, 1)
        self.home_button = QPushButton("Home")
        self.home_button.clicked.connect(self.home_actuators)
        layout.addWidget(self.home_button, 2, 0, 1, 2)
        central_widget.setLayout(layout)
        self.statusBar().showMessage("Ready")

    def home_actuators(self):
        self.statusBar().showMessage("Home button clicked")
        print("Home button clicked")

    def set_left_position(self, value):
        self.left_position.display(value)
        self.statusBar().showMessage(f"Left slider value: {value}")

    def set_right_position(self, value):
        self.left_position.display(value)
        self.statusBar().showMessage(f"Right slider value: {value}")
