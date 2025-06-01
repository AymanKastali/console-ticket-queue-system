import abc

from core import entities


class Notifier(abc.ABC):
    @abc.abstractmethod
    def notify(self, ticket: entities.Ticket): ...
