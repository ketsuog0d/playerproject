from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from databases import SessionLocal, engine
import models, crud, schemas

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post('/artists/', response_model=schemas.Artist)
def add_artist(artist:schemas.ArtistCreate, db:Session=Depends(get_db)):
    return crud.create_artist(db, artist)

@app.post('/songs/', response_model=schemas.Song)
def add_song(song:schemas.SongCreate, db:Session=Depends(get_db)):
    return crud.create_song(db, song)

@app.get('/artists/', response_model=list[schemas.Artist])
def get_artists(db:Session=Depends(get_db)):
    return crud.get_artists(db)

@app.get('/songs/', response_model=list[schemas.Song])
def get_songs(db:Session=Depends(get_db)):
    return crud.get_songs(db)

@app.delete('/artists/{artist_id}')
def delete_artist(artist_id:int, db:Session=Depends(get_db)):
    artist = crud.delete_artist(db, artist_id)
    if not artist:
        raise HTTPException(status_code=404, detail="Исполнитель не найден")
    return {"message": "Исполнитель удален"}

@app.delete('/songs/{song_id}')
def delete_song(song_id:int, db:Session=Depends(get_db)):
    song = crud.delete_song(db, song_id)
    if not song:
        raise HTTPException(status_code=404, detail="Трек не найден")
    return {"message": "Трек удален"}
