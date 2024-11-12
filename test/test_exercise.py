import pytest
from exercise1.simulate_axes import SimulateAxes
import time


@pytest.fixture
def simulator():
    axes = SimulateAxes()
    axes.start()
    yield axes
    axes.stop()

def test_init(simulator):
    assert simulator.get_position() == (0.0, 0.0)

def test_move_left(simulator):
    t0 = time.time()
    simulator.move_left(40, blocking=True)
    assert simulator.get_position() == (40.0, 0.0)
    t_end = time.time() - t0
    assert t_end >= 4.0
    assert t_end < 6.0