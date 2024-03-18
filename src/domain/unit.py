from dataclasses import dataclass
from enum import Enum
from typing import Callable, Optional


class UnitName(Enum):
    GRAM: str = "weight"
    LITER: str = "volume"
    MILILITER: str = "mililiter"
    TABLESPOON: str = "tablespoon"
    TEASPOON: str = "teaspoon"
    


@dataclass(init=False, eq=True, frozen=True)
class Unit:

    MILILITER_PER_LITER = 1000
    MILILITER_PER_TABLESPOON = 15
    MILILITER_PER_TEASPOON = 5

    def __init__(self, name: UnitName) -> None:
        self.name: UnitName = name

    def transform_func(
        self,
        to_unit_name,
        gram_per_mililiter: Optional[float]
    ) -> Callable[[int | float], int | float]:
        from_unit_name = self.name
        return {
            UnitName.GRAM: {
                UnitName.GRAM: lambda x: x,
                UnitName.LITER: lambda x: x / gram_per_mililiter / self.MILILITER_PER_LITER,
                UnitName.MILILITER: lambda x: x / gram_per_mililiter,
                UnitName.TABLESPOON: lambda x: x / gram_per_mililiter / self.MILILITER_PER_TABLESPOON,
                UnitName.TEASPOON: lambda x: x / gram_per_mililiter / self.MILILITER_PER_TEASPOON,
            },
            UnitName.LITER: {
                UnitName.GRAM: lambda x: gram_per_mililiter * self.MILILITER_PER_LITER * x,
                UnitName.LITER: lambda x: x,
                UnitName.MILILITER: lambda x: self.MILILITER_PER_LITER * x,
                UnitName.TABLESPOON: lambda x: self.MILILITER_PER_LITER * x / self.MILILITER_PER_TABLESPOON,
                UnitName.TEASPOON: lambda x: self.MILILITER_PER_LITER * x / self.MILILITER_PER_TEASPOON,                
            },
            UnitName.MILILITER: {
                UnitName.GRAM: lambda x: gram_per_mililiter * x,
                UnitName.LITER: lambda x: x / self.MILILITER_PER_LITER,
                UnitName.MILILITER: lambda x: x,
                UnitName.TABLESPOON: lambda x: x / self.MILILITER_PER_TABLESPOON,
                UnitName.TEASPOON: lambda x: x / self.MILILITER_PER_TEASPOON,
            },
            UnitName.TABLESPOON: {
                UnitName.GRAM: lambda x: gram_per_mililiter * x * self.MILILITER_PER_TABLESPOON,
                UnitName.LITER: lambda x: x * self.MILILITER_PER_TABLESPOON / self.MILILITER_PER_LITER,
                UnitName.MILILITER: lambda x: x * self.MILILITER_PER_TABLESPOON,
                UnitName.TABLESPOON: lambda x: x,
                UnitName.TEASPOON: lambda x: x * self.MILILITER_PER_TABLESPOON / self.MILILITER_PER_TEASPOON,                
            },
            UnitName.TEASPOON: {
                UnitName.GRAM: lambda x: gram_per_mililiter * x * self.MILILITER_PER_TEASPOON,
                UnitName.LITER: lambda x: x * self.MILILITER_PER_TEASPOON / self.MILILITER_PER_LITER,
                UnitName.MILILITER: lambda x: x * self.MILILITER_PER_TEASPOON,
                UnitName.TABLESPOON: lambda x: x * self.MILILITER_PER_TEASPOON / self.MILILITER_PER_TABLESPOON,
                UnitName.TEASPOON: lambda x: x,
            }
        }[from_unit_name][to_unit_name]