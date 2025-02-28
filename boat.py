from dataclasses import dataclass
from typing import List

@dataclass
class Oar:
    length: float
    is_attached: bool = True

    def row(self) -> str:
        if self.is_attached:
            return "Гребок выполнен."
        return "Весло не прикреплено."

    def detach(self) -> None:
        self.is_attached = False

@dataclass
class Seat:
    max_weight: float
    current_weight: float = 0.0

    def sit(self, weight: float) -> str:
        if self.current_weight + weight <= self.max_weight:
            self.current_weight += weight
            return f"Человек весом {weight} кг сел."
        return "Превышена допустимая нагрузка."

    def stand_up(self) -> None:
        self.current_weight = 0.0

@dataclass
class Boat:
    capacity: int
    max_load: float 
    current_load: float = 0.0
    oars: List[Oar] = None
    seats: List[Seat] = None 

    def __post_init__(self):
        self.oars = [Oar(length=2.0) for _ in range(2)]
        self.seats = [Seat(max_weight=100.0) for _ in range(self.capacity)]

    def add_person(self, weight: float) -> str:
        if self.current_load + weight <= self.max_load and len(self.seats) > 0:
            seat = self.seats.pop(0)
            result = seat.sit(weight)
            self.current_load += weight
            return result
        return "Недостаточно места или превышена грузоподъемность."

    def remove_person(self) -> str:
        if len(self.seats) < self.capacity:
            seat = self.seats.append(Seat(max_weight=100.0))
            self.current_load -= seat.current_weight
            return "Человек покинул лодку."
        return "Лодка уже пуста."

    def row(self) -> str:
        results = [oar.row() for oar in self.oars]
        return ", ".join(results)

    def detach_oar(self, index: int) -> str:
        if 0 <= index < len(self.oars):
            self.oars[index].detach()
            return f"Весло {index} отсоединено."
        return "Неверный индекс весла."
