from dataclasses import dataclass

@dataclass
class CreateTodoRequest:
    title: str
    description: str = ""
