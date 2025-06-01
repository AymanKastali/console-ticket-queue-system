from core import entities, repositories


class LoginUserUseCase:
    def __init__(self, repo: repositories.AuthenticationRepository):
        self.repo = repo

    def execute(self, username: str, password: str) -> entities.UserEntity | None:
        user = entities.UserEntity(
            username=username, password=password, role=entities.Role.GUEST
        )
        return self.repo.login(user)
