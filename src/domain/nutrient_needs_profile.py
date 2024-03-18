from dataclasses import dataclass


from enum import Enum


class Sex(Enum):
    MAN: str = "man"
    WOMAN: str = "woman"


@dataclass(init=False, eq=True, frozen=True)
class Age:

    def __init__(self, age: int) -> None:
        if age < 0 or age > 150:
            return ValueError(f"ageが不正です({age})")
        age: int = age


@dataclass(init=False, eq=True, frozen=True)
class NutrientNeedsProfile:

    def __init__(self, sex: Sex, age: Age) -> None:
        self.sex: Sex = sex
        self.age: Age = age
