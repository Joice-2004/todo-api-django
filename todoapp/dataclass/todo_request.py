from dataclasses import dataclass

@dataclass
class CreateTodoRequest:
    title: str
    description: str
    is_completed: bool = False

@dataclass
class UpdateTodoRequest:
    title: str | None = None
    description: str | None = None
    is_completed: bool | None = None



