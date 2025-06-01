import use_cases
from core import entities


class AuthenticationController:
    def __init__(self, login_user_use_case: use_cases.LoginUserUseCase):
        self.login_user_use_case = login_user_use_case

    def login_user(self, username: str, password: str) -> entities.UserEntity | None:
        return self.login_user_use_case.execute(username, password)


class ConsoleController:
    def __init__(
        self,
        apply_use_case: use_cases.ApplyForTicketUseCase,
        call_use_case: use_cases.CallNextTicketUseCase,
    ):
        self.apply_use_case = apply_use_case
        self.call_use_case = call_use_case

    def apply_ticket(
        self, name: str, ticket_type: entities.TicketType
    ) -> entities.Ticket:
        return self.apply_use_case.execute(name, ticket_type)

    def call_ticket(self) -> entities.Ticket | None:
        return self.call_use_case.execute()
