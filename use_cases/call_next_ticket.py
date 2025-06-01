from core import entities, repositories


class CallNextTicketUseCase:
    def __init__(
        self, repo: repositories.TicketRepository, notifier: repositories.Notifier
    ):
        self.repo = repo
        self.notifier = notifier

    def execute(
        self,
    ):
        next_ticket = self.repo.get_next()
        if next_ticket:
            next_ticket.status = entities.TicketStatus.CALLED
            self.notifier.notify(next_ticket)
        return next_ticket
