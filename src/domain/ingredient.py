from typing import Optional

from domain.food import Food
from domain.unit import Unit


class Ingredient:
    """
    材料(量の概念を含むFood)
    """

    def __init__(self, food: Food, quantity: float, unit: Unit) -> None:
        self.food: Food = food
        self.quantity: float = quantity
        self.unit: Unit = unit

    def transform_unit(self, to_unit: Unit, density: Optional[float]) -> Ingredient:
        func = self.unit.transform_func(to_unit, density)
        return Ingredient(
            food=self.food,
            quantity=func(self.quantity),
            unit=to_unit
        )

    def calc_nutrients(self):
        pass
