from threading import Thread
from PySide6.QtCore import QObject, Signal
from time import sleep


class SimulateAxes(QObject):
    stopped = Signal()
    pos_change = Signal(float, float)

    def __init__(self):
        super().__init__()
        self.worker = None
        self.x = 0
        self.y = 0

        self.set_x_pos = 0
        self.set_y_pos = 0

        self.max = 4.0
        self.stop_flag = False

    def move_x(self, position):
        if position < 0 or position > self.max:
            return
        else:
            self.set_x_pos = position

    def move_y(self, position):
        if position < 0 or position > self.max:
            return
        else:
            self.set_y_pos = position

    def get_position(self):
        return self.x, self.y

    def home(self):
        self.x = 0
        self.y = 0

    def start(self):
        self.worker = Thread(target=self._run, name="SimulateAxes")
        self.worker.start()

    def stop(self):
        self.stop_flag = True
        self.worker.join()

    def _run(self):
        print("Axes simulator Thread started")
        while not self.stop_flag:
            change_requested = self.x != self.set_x_pos or self.y != self.set_y_pos

            if self.x < self.set_x_pos:
                self.x += 1
            elif self.x > self.set_x_pos:
                self.x -= 1

            if self.y < self.set_y_pos:
                self.y += 1
            elif self.y > self.set_y_pos:
                self.y -= 1
            sleep(0.1)

            if change_requested:
                self.pos_change.emit(self.x, self.y)

        print("Simulator Thread stopped")
        self.stopped.emit()