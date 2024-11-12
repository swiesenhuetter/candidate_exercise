import pytest
from exercise1.simulate_axes import SimulateAxes


@pytest.fixture
def simulator():
    return SimulateAxes()


def test_move(simulator):
    assert simulator.get_position() == (0.0, 0.0)
