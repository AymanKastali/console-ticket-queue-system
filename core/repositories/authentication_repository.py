import abc

from core import entities


class AuthenticationRepository(abc.ABC):
    @abc.abstractmethod
    def login(self, user: entities.UserEntity) -> entities.UserEntity | None: ...
