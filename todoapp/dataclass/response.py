from dataclasses import dataclass

@dataclass
class TodoResponse:
    id: int
    title: str
    description: str
    is_completed: bool
