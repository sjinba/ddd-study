from domain.ingredient import Ingredient
from domain.nutrient_needs_profile import NutrientNeedsProfile
from domain.steps import Steps


class Recipe:
    """
    料理のレシピ
    """

    def __init__(
        self,
        recipe_id: int,
        name: str,
        ingredients: list[Ingredient],
        nutrient_needs_profiles: list[NutrientNeedsProfile],
        steps: Steps
    ) -> None:
        self.recipe_id: int = recipe_id
        self.name: str = name
        self.ingredients: list[Ingredient] = ingredients
        self.nutrient_needs_profiles: list[NutrientNeedsProfile] = \
            nutrient_needs_profiles
        self.steps: Steps = steps
