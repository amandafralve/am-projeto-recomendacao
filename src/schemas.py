from pydantic import BaseModel
from typing import Optional

#1 - Caracterpisticas da Música (base do cálculo)
class MusicFeatures(BaseModel):
    energy: float
    loudness: float

#2 - O que o usuário envia (Pedido)
class Trackrequest(BaseModel):
    track_id: Optional[str] = "unknow"
    track_name: str
    artist_name: str
    features: MusicFeatures

#3 - O que a API responde (Resposta)
class TrackResponse(BaseModel):
    track: str
    artist: str
    recommendation: str
    debug_info: dict