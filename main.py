import use_cases
from adapters import controllers, gateways, presenters
from external.console import ConsoleApp

if __name__ == "__main__":
    ticket_repo = gateways.InMemoryTicketRepository()
    auth_repo = gateways.InMemoryAuthenticationRepository()
    notifier = presenters.ConsoleNotifier()

    apply_use_case = use_cases.ApplyForTicketUseCase(ticket_repo)
    call_use_case = use_cases.CallNextTicketUseCase(ticket_repo, notifier)
    login_use_case = use_cases.LoginUserUseCase(auth_repo)

    ticket_controller = controllers.ConsoleController(apply_use_case, call_use_case)
    auth_controller = controllers.AuthenticationController(login_use_case)

    app = ConsoleApp(ticket_controller, auth_controller)
    app.run()
