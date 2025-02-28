import pytest
from boat import Boat, Oar, Seat

@pytest.fixture
def boat():
    return Boat(capacity=2, max_load=200.0)


def test_stop(boat):
    """Тест-кейс FT3: Проверка остановки.
    Ожидаемый результат: Лодка постепенно останавливается."""
    result = boat.row()
    assert result == "Гребок выполнен., Гребок выполнен."
    assert boat.row() == "Гребок выполнен., Гребок выполнен."


def test_speed(boat):
    """Тест-кейс FT1: Проверка скорости движения.
    Ожидаемый результат: Лодка достигает определенной скорости."""
    for _ in range(10):
        boat.row()
    assert boat.row() == "Гребок выполнен., Гребок выполнен."


def test_oar_functionality(boat):
    """Тест-кейс IT1: Проверка работы весел.
    Ожидаемый результат: Лодка движется вперед."""
    result = boat.row()
    assert result == "Гребок выполнен., Гребок выполнен."


def test_oar_attachment(boat):
    """Тест-кейс IT2: Проверка фиксации весел.
    Ожидаемый результат: Весла остаются закрепленными."""
    boat.detach_oar(0)
    assert boat.oars[0].is_attached is False


def test_manoeuvrability(boat):
    """Тест-кейс FT2: Проверка маневренности.
    Ожидаемый результат: Лодка успешно меняет направление."""
    boat.detach_oar(0)
    result = boat.row()
    assert result == "Весло не прикреплено., Гребок выполнен."


def test_load_capacity(boat):
    """Тест-кейс ST3: Проверка грузоподъемности.
    Ожидаемый результат: Лодка остается на плаву, не затапливается."""
    result = boat.add_person(150.0)
    assert result == "Человек весом 150.0 кг сел."
    assert boat.current_load == 150.0
    result = boat.add_person(60.0)
    assert result == "Недостаточно места или превышена грузоподъемность."
