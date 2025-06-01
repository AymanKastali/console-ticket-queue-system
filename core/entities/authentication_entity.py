import dataclasses
import enum


class Role(enum.StrEnum):
    GUEST = enum.auto()
    ADMIN = enum.auto()


@dataclasses.dataclass
class UserEntity:
    username: str
    password: str
    role: Role
