from dataclasses import dataclass

@dataclass
class CreateMusicDirectorRequest:
    name: str
    age: int
    experience: int
    famous_album: str
    is_active: bool = True


@dataclass
class UpdateMusicDirectorRequest:
    name: str | None = None
    age: int | None = None
    experience: int | None = None
    famous_album: str | None = None
    is_active: bool | None = None
