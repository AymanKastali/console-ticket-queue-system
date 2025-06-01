from core import entities, repositories


class ApplyForTicketUseCase:
    def __init__(self, repo: repositories.TicketRepository):
        self.repo = repo

    def execute(
        self, customer_name: str, ticket_type: entities.TicketType
    ) -> entities.Ticket:
        ticket = entities.Ticket(customer_name, ticket_type)
        self.repo.save(ticket)
        return ticket
