from abc import ABC, abstractmethod

from domain.recipe import Recipe


# class IRecipeCreator(ABC):
#     """
#     レシピ作成ユースケースのIF
#     """

#     def __init__(self) -> None:
#         pass


# class IRecipeReader(ABC):
#     """
#     レシピ読み出しユースケースのIF
#     """
#     def __init__(self, repositry: IRepository) -> None:
#         super().__init__()
#         self.__repositry: IRepository = repositry

#     @abstractmethod
#     def excecute(self) -> list[Recipe]:
#         pass

# class IRecipeUpdater(ABC):
#     """
#     レシピ更新ユースケースのIF
#     """

#     def __init__(self) -> None:
#         pass


# class IRecipeDeleter(ABC):
#     """
#     レシピ削除ユースケースのIF
#     """

#     def __init__(self) -> None:
#         pass
