from collections import deque

from core import entities, repositories

in_memory_users_db = [
    {"username": "ayman kastali", "password": "secret", "role": entities.Role.ADMIN},
    {"username": "john doe", "password": "0000", "role": entities.Role.GUEST},
]


class InMemoryAuthenticationRepository(repositories.AuthenticationRepository):
    def __init__(self):
        pass

    def login(self, user: entities.UserEntity) -> entities.UserEntity | None:
        for record in in_memory_users_db:
            if (
                record.get("username") == user.username
                and record.get("password") == user.password
            ):
                return entities.UserEntity(
                    username=record["username"],
                    password=record["password"],
                    role=record["role"],
                )
        return None


class InMemoryTicketRepository(repositories.TicketRepository):
    def __init__(self):
        self.queues = {
            entities.TicketType.PRIORITY: deque(),
            entities.TicketType.GENERAL: deque(),
        }

    def save(self, ticket: entities.Ticket):
        self.queues[ticket.type].append(ticket)

    def get_next(self):
        for ticket_type in [entities.TicketType.PRIORITY, entities.TicketType.GENERAL]:
            if self.queues[ticket_type]:
                return self.queues[ticket_type].popleft()
        return None
