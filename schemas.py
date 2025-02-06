from pydantic import BaseModel
from typing import List, Optional

class SongBase(BaseModel):
    title: str
    artist_id: int

class SongCreate(SongBase):
    pass

class Song(SongBase):
    id: int

    class Config:
        orm_mode = True

class ArtistBase(BaseModel):
    artist_name: str

class ArtistCreate(ArtistBase):
    pass

class Artist(ArtistBase):
    id: int
    songs: List[Song] = []

    class Config:
        orm_mode = True