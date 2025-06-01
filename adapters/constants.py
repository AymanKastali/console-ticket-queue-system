from core import entities

# General system messages
WELCOMING_MESSAGE = "[bold cyan]Welcome to the Console Ticket System[/bold cyan]"
CHOOSE_MESSAGE = "[bold white]Choose an option[/bold white]"
EXIT_MESSAGE = "[bold red]3. Exit[/bold red]"
EXITING_MESSAGE = "[bold magenta]Exiting... Goodbye![/bold magenta]"
INVALID_CHOICE_MESSAGE = "[bold red]Invalid choice. Please try again.[/bold red]"

# Guest
GUEST_MESSAGE = "[bold blue]You are using the system as a Guest[/bold blue]"
APPLY_FOR_TICKET_MESSAGE = "[bold green]1. Apply for Ticket[/bold green]"
LOGIN_MESSAGE = "[bold yellow]2. Login (Admin Only)[/bold yellow]"
LOGIN_FAILED_MESSAGE = "[bold red]Login failed or not an admin.[/bold red]"

# Admin
ADMIN_LOGGED_IN_MESSAGE = "[bold yellow]Logged in as Admin[/bold yellow]"
CALL_NEXT_TICKET_MESSAGE = "[bold green]1. Call Next Ticket[/bold green]"
CALLING_TICKET_MESSAGE = "[bold cyan]Calling[/bold cyan]"
LOGOUT_MESSAGE = "[bold red]2. Logout[/bold red]"
LOGGED_OUT_MESSAGE = "[bold red]Logged out[/bold red]"
NO_TICKETS_MESSAGE = "[bold yellow]No tickets in queue.[/bold yellow]"

# Prompts
ENTER_NAME_MESSAGE = "[bold white]Enter your name[/bold white]"
ENTER_USERNAME_MESSAGE = "[bold white]Enter username[/bold white]"
ENTER_PASSWORD_MESSAGE = "[bold white]Enter your password[/bold white]"
CHOOSE_TICKET_TYPE_MESSAGE = "[bold white]Choose ticket type:[/bold white]"
TICKET_TYPE_GENERAL = (
    f"[bold cyan]1. {entities.TicketType.GENERAL.capitalize()}[/bold cyan]"
)
TICKET_TYPE_PRIORITY = (
    f"[bold magenta]2. {entities.TicketType.PRIORITY.capitalize()}[/bold magenta]"
)
ENTER_TYPE_MESSAGE = "[bold white]Enter type [1/2][/bold white]"
CREATED_TICKET_MESSAGE = "[bold green]Created Ticket[/bold green]"
