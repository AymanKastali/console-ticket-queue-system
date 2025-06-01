import json

from rich.console import Console
from rich.prompt import Prompt

from adapters import constants, controllers
from core import entities

console = Console()


class ConsoleApp:
    def __init__(
        self,
        controller: controllers.ConsoleController,
        auth_controller: controllers.AuthenticationController,
    ):
        self.controller = controller
        self.auth_controller = auth_controller
        self.logged_in_user: entities.UserEntity | None = None

    def run(self):
        while True:
            console.print(constants.WELCOMING_MESSAGE, "\n")

            if (
                self.logged_in_user
                and self.logged_in_user.role == entities.Role.ADMIN
            ):
                console.print(constants.ADMIN_LOGGED_IN_MESSAGE)
                console.print(f"1. {constants.CALL_NEXT_TICKET_MESSAGE}")
                console.print(f"2. {constants.LOGOUT_MESSAGE}")
                console.print(f"3. {constants.EXIT_MESSAGE}", end="\n")
                choice = Prompt.ask(constants.CHOOSE_MESSAGE)

                match choice:
                    case "1":
                        ticket = self.controller.call_ticket()
                        if ticket:
                            console.print_json(json.dumps(ticket.to_dict()))
                            console.print(constants.SEPARATOR, end="\n")
                        else:
                            console.print(constants.NO_TICKETS_MESSAGE)
                            console.print(constants.SEPARATOR, end="\n")
                    case "2":
                        self.logged_in_user = None
                        console.print(constants.LOGGED_OUT_MESSAGE)
                        console.print(constants.SEPARATOR, end="\n")
                    case "3":
                        console.print(constants.EXITING_MESSAGE)
                        console.print(constants.SEPARATOR, end="\n")
                        break
                    case _:
                        console.print(
                            constants.INVALID_CHOICE_MESSAGE, end="\n"
                        )
                        console.print(constants.SEPARATOR, end="\n")

            else:
                console.print(constants.GUEST_MESSAGE)
                console.print(f"1. {constants.APPLY_FOR_TICKET_MESSAGE}")
                console.print(f"2. {constants.LOGIN_MESSAGE}")
                console.print(f"3. {constants.EXIT_MESSAGE}", end="\n")
                choice = Prompt.ask(constants.CHOOSE_MESSAGE)

                match choice:
                    case "1":
                        name = Prompt.ask(constants.ENTER_NAME_MESSAGE)
                        console.print(constants.CHOOSE_TICKET_TYPE_MESSAGE)
                        console.print(constants.TICKET_TYPE_GENERAL)
                        console.print(constants.TICKET_TYPE_PRIORITY)
                        ticket_type_choice = Prompt.ask(
                            constants.ENTER_TYPE_MESSAGE,
                            choices=["1", "2"],
                            default="1",
                        )
                        ticket_type = (
                            entities.TicketType.PRIORITY
                            if ticket_type_choice == "2"
                            else entities.TicketType.GENERAL
                        )
                        ticket = self.controller.apply_ticket(name, ticket_type)
                        console.print_json(json.dumps(ticket.to_dict()))
                        console.print(constants.EXITING_MESSAGE)
                        console.print(constants.SEPARATOR, end="\n")

                    case "2":
                        username = Prompt.ask(constants.ENTER_USERNAME_MESSAGE)
                        password = Prompt.ask(
                            constants.ENTER_PASSWORD_MESSAGE, password=True
                        )
                        user = self.auth_controller.login_user(
                            username, password
                        )
                        if user and user.role == entities.Role.ADMIN:
                            self.logged_in_user = user
                            console.print(
                                f"{constants.ADMIN_LOGGED_IN_MESSAGE}: {user.username}"
                            )
                        else:
                            console.print(constants.LOGIN_FAILED_MESSAGE)
                            console.print(constants.SEPARATOR, end="\n")

                    case "3":
                        console.print(constants.EXITING_MESSAGE)
                        console.print(constants.SEPARATOR, end="\n")
                        break

                    case _:
                        console.print(
                            constants.INVALID_CHOICE_MESSAGE, end="\n"
                        )
                        console.print(constants.SEPARATOR, end="\n")
