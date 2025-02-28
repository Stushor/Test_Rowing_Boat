import pytest
from boat import Boat, Oar, Seat

@pytest.fixture
def boat():
    return Boat(capacity=2, max_load=200.0)

def test_add_person(boat):
    assert boat.add_person(70.0) == "Человек весом 70.0 кг сел."
    assert boat.current_load == 70.0

def test_remove_person(boat):
    boat.add_person(70.0)
    assert boat.remove_person() == "Человек покинул лодку."
    assert boat.current_load == 0.0

def test_row(boat):
    result = boat.row()
    assert result == "Гребок выполнен., Гребок выполнен."

def test_detach_oar(boat):
    assert boat.detach_oar(0) == "Весло 0 отсоединено."
    assert boat.oars[0].is_attached is False
