from dataclasses import dataclass

@dataclass
class CreateSongRequest:
    name: str
    description: str
    singers: str
    music_director_id: int
    is_active: bool = True



@dataclass
class UpdateSongRequest:
    name: str | None = None
    description: str | None = None
    singers: str | None = None
    is_active: bool | None = None
