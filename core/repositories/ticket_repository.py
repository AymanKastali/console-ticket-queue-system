import abc

from core import entities


class TicketRepository(abc.ABC):
    @abc.abstractmethod
    def save(self, ticket: entities.Ticket): ...

    @abc.abstractmethod
    def get_next(self) -> entities.Ticket: ...
