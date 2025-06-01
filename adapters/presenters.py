from rich.console import Console

from core import entities, repositories

console = Console()


class ConsoleNotifier(repositories.Notifier):
    def notify(self, ticket: entities.Ticket):
        console.print(
            f"[green]Notifying {ticket.customer_name}[/green]: Your ticket {ticket.id} is called."
        )
