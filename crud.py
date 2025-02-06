from sqlalchemy.orm import Session
from models import Artist, Song
from schemas import ArtistCreate, SongCreate

def create_artist(db:Session, artist:ArtistCreate):
    new_artist = Artist(name=artist.artist_name)
    db.add(new_artist)
    db.commit()
    db.refresh(new_artist)
    return new_artist

def create_song(db:Session, song:SongCreate):
    new_song = Song(name=song.song_name, artist_id=song.artist_id)
    db.add(new_song)
    db.commit()
    db.refresh(new_song)
    return new_song

def get_artists(db:Session):
    return db.query(Artist).all()

def get_songs(db:Session):
    return db.query(Song).all()

def delete_artist(db:Session, artist_id:int):
    artist = db.query(Artist).filter(Artist.id == artist_id).first()
    if artist:
        db.delete(artist)
        db.commit()
    return artist

def delete_song(db:Session, song_id:int):
    song = db.query(Song).filter(Song.id == song_id).first()
    if song:
        db.delete(song)
        db.commit()
    return song
