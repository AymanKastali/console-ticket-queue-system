import enum


class TicketStatus(enum.StrEnum):
    WAITING = enum.auto()
    CALLED = enum.auto()
    COMPLETED = enum.auto()


class TicketType(enum.StrEnum):
    GENERAL = enum.auto()
    PRIORITY = enum.auto()


class Ticket:
    _id_counter = 1

    def __init__(self, customer_name: str, ticket_type: TicketType):
        self.id = Ticket._id_counter
        Ticket._id_counter += 1
        self.customer_name = customer_name
        self.type = ticket_type
        self.status = TicketStatus.WAITING

    def __str__(self):
        return (
            f"Ticket #{self.id} ({self.type.name.capitalize()}) - "
            f"{self.customer_name} - {self.status.name.capitalize()}"
        )

    def to_dict(self):
        return {
            "ticket_number": self.id,
            "customer_name": self.customer_name,
            "type": self.type,
            "status": self.status,
        }
