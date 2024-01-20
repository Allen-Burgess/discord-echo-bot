from dataclasses import dataclass

@dataclass
class User:
    id: int
    username: str
    nickname: str
    description: str