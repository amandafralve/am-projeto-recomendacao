from pydantic import BaseModel
from typing import Optional

# 1. CARACTERÍSTICAS DA MÚSICA (Base do cálculo)
class MusicFeatures(BaseModel):
    energy: float
    loudness: float

# 2. O QUE O USUÁRIO ENVIA (Pedido)
class TrackRequest(BaseModel):
    track_id: Optional[str] = "unknown"  # ID da música, pode ser opcional
    track_name: str 
    artist_name: str
    features: MusicFeatures
    
# 3. O QUE O MODELO(API) RESPONDE (Resposta)
class TrackResponse(BaseModel):
    track: str
    artist: str
    recommendation: str
    debug_info: dict