from pydantic import BaseModel, Field, validator
from typing import Optional

class SongFeatures(BaseModel):
    # Raw numeric features (20 total — the model generates missing flags itself)
    spotify_streams: float = Field(0, ge=0)
    spotify_playlist_count: float = Field(0, ge=0)
    spotify_playlist_reach: float = Field(0, ge=0)
    youtube_views: float = Field(0, ge=0)
    youtube_likes: float = Field(0, ge=0)
    tiktok_posts: float = Field(0, ge=0)
    tiktok_likes: float = Field(0, ge=0)
    tiktok_views: float = Field(0, ge=0)
    youtube_playlist_reach: float = Field(0, ge=0)
    apple_music_playlist_count: float = Field(0, ge=0)
    airplay_spins: float = Field(0, ge=0)
    deezer_playlist_count: float = Field(0, ge=0)
    deezer_playlist_reach: float = Field(0, ge=0)
    amazon_playlist_count: float = Field(0, ge=0)
    pandora_streams: float = Field(0, ge=0)
    pandora_track_stations: float = Field(0, ge=0)
    shazam_counts: float = Field(0, ge=0)

    # Categorical / encoded
    explicit_track: int = Field(0, ge=0, le=1)
    artist_encoded: int = Field(0, ge=0)

    # Date field (converted into 3 features)
    release_date: Optional[str] = None

    @validator("release_date")
    def validate_date(cls, v):
        if v is None:
            return v
        import re
        if not re.match(r"^\d{4}-\d{2}-\d{2}$", v):
            raise ValueError("release_date must be in YYYY-MM-DD format")
        return v