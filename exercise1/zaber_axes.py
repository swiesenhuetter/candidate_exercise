from zaber_motion import Units
from zaber_motion.ascii import Connection

class ZaberAxes:
    def __init__(self):
        self.serial_port="COM3"

        self.connection = Connection.open_serial_port(self.serial_port)
        devices = self.connection.detect_devices()
        if not devices:
            raise Exception('No Zaber devices found')

        self.controller = self.connection.detect_devices()[0]
        self.controller_connected = True

        self.left_axis = self.controller.get_axis(1)
        self.right_axis = self.controller.get_axis(2)

    def move_left(self, position):
        self.left_axis.move_absolute(position, wait_until_idle=False)

    def move_right(self, position):
        self.right_axis.move_absolute(position, wait_until_idle=False)

    def home(self):
        self.controller.all_axes.home()

    def get_positions(self: tuple[float, float]):
        left_pos = self.left.get_position(Units.LENGTH_MILLIMETRES)
        right_pos = self.left.get_position(Units.LENGTH_MILLIMETRES)
        return left_pos, right_pos

    def close(self):
        if self.controller is not None:
            self.connection.close()
