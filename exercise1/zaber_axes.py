from zaber_motion import Units
from PySide6.QtCore import Signal, QObject
from zaber_motion.ascii import Connection
from threading import Thread
import time


class ZaberAxes(QObject):
    pos_change = Signal(float, float)

    def __init__(self):
        super().__init__()
        self.serial_port="COM3"

        self.connection = Connection.open_serial_port(self.serial_port)
        devices = self.connection.detect_devices()
        if not devices:
            raise Exception('No Zaber devices found')

        self.controller = self.connection.detect_devices()[0]
        self.controller_connected = True

        self.left_axis = self.controller.get_axis(1)
        self.right_axis = self.controller.get_axis(2)
        self.stop_flag = False
        self.worker = None

    def move_left(self, position):
        pos_mm = float(position) / 10.0
        self.left_axis.move_absolute(pos_mm, wait_until_idle=False, unit=Units.LENGTH_MILLIMETRES)

    def move_right(self, position):
        pos_mm = float(position) / 10.0
        self.right_axis.move_absolute(pos_mm, wait_until_idle=False, unit=Units.LENGTH_MILLIMETRES)

    def home(self):
        self.controller.all_axes.home()

    def get_positions(self) -> tuple[float, float]:
        left_pos = self.left_axis.get_position(Units.LENGTH_MILLIMETRES)
        right_pos = self.right_axis.get_position(Units.LENGTH_MILLIMETRES)
        return left_pos, right_pos

    def close(self):
        if self.controller is not None:
            self.connection.close()

    def _run(self):
        print("Zaber Thread started")
        x, y = self.get_positions()
        self.pos_change.emit(x * 10.0, y * 10.0)

        while not self.stop_flag:
            time.sleep(0.1)

            new_x, new_y = self.get_positions()
            if new_x != x or new_y != y:
                self.pos_change.emit(new_x * 10.0, new_y * 10.0)
                x, y = new_x, new_y

    def start(self):
        self.worker = Thread(target=self._run, name="Zaber")
        self.worker.start()

    def stop(self):
        if self.worker is None:
            print("Not running")
            return
        self.stop_flag = True
        self.worker.join()

