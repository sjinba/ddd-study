from dataclasses import dataclass


@dataclass(init=False, eq=True, frozen=True)
class Nutrient:
    """
    栄養素
    """

    nutrient_id: int
    name: str
    gram: float
