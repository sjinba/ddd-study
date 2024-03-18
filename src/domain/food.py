from dataclasses import dataclass
from typing import Optional

from domain.nutrient import Nutrient


@dataclass(init=False, eq=True, frozen=True)
class Food:
    """
    食料品
    """
    def __init__(
        self,
        food_id: int,
        name: str,
        gram_per_nutrients: list[Nutrient],
        gram_per_mililiter: Optional[float],
        gram_per_piece: Optional[float]
    ) -> None:
        self.food_id: int = food_id
        self.name: str = name
        self.gram_per_nutrients: list[Nutrient] = gram_per_nutrients
        self.gram_per_mililiter: Optional[float] = gram_per_mililiter
        self.gram_per_piece: Optional[float] = gram_per_piece