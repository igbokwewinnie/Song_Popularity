import pandas as pd
import numpy as np


ALL_MODEL_FEATURES = [
    'spotify_streams',
    'spotify_playlist_count',
    'spotify_playlist_reach',
    'youtube_views',
    'youtube_likes',
    'tiktok_posts',
    'tiktok_likes',
    'tiktok_views',
    'youtube_playlist_reach',
    'apple_music_playlist_count',
    'airplay_spins',
    'deezer_playlist_count',
    'deezer_playlist_reach',
    'amazon_playlist_count',
    'pandora_streams',
    'pandora_track_stations',
    'shazam_counts',
    'explicit_track',
    'spotify_streams_missing',
    'spotify_playlist_count_missing',
    'spotify_playlist_reach_missing',
    'youtube_views_missing',
    'youtube_likes_missing',
    'tiktok_posts_missing',
    'tiktok_likes_missing',
    'tiktok_views_missing',
    'youtube_playlist_reach_missing',
    'apple_music_playlist_count_missing',
    'airplay_spins_missing',
    'pandora_streams_missing',
    'pandora_track_stations_missing',
    'shazam_counts_missing',
    'deezer_playlist_count_missing',
    'deezer_playlist_reach_missing',
    'amazon_playlist_count_missing',
    'artist_encoded',
    'release_year',
    'release_month',
    'release_day'
]


def clean_column_names(df: pd.DataFrame) -> pd.DataFrame:
    """Standardize column names: lowercase, underscores, remove special characters."""
    df = df.copy()
    df.columns = (
        df.columns
        .astype(str)
        .str.strip()
        .str.lower()
        .str.replace(" ", "_")
        .str.replace("%", "pct")
        .str.replace(r"[^\w_]", "", regex=True)
    )
    return df


def ensure_numeric_and_impute(df: pd.DataFrame) -> pd.DataFrame:
    """
    Convert columns to numeric, create missing indicators, impute missing values.
    Returns DataFrame with ALL_MODEL_FEATURES in correct order.
    """
    df = df.copy()
    
    # Columns to median-fill
    median_fill_cols = [
        "spotify_streams","spotify_playlist_count","spotify_playlist_reach",
        "youtube_views","youtube_likes","tiktok_posts","tiktok_likes","tiktok_views",
        "youtube_playlist_reach","apple_music_playlist_count","airplay_spins",
        "pandora_streams","pandora_track_stations","shazam_counts"
    ]
    
    # Columns to zero-fill
    zero_fill_cols = ["deezer_playlist_count","deezer_playlist_reach","amazon_playlist_count"]

    # Convert to numeric
    numeric_candidates = list(set(median_fill_cols + zero_fill_cols))
    for col in numeric_candidates:
        if col in df.columns:
            s = df[col].astype(str).str.replace(",", "", regex=False).str.strip()
            s = s.replace({"": pd.NA, "nan": pd.NA, "None": pd.NA})
            df[col] = pd.to_numeric(s, errors="coerce")

    # Create missing flags + impute median
    for col in median_fill_cols:
        if col in df.columns:
            df[col + "_missing"] = df[col].isna().astype(int)
            median_val = df[col].median(skipna=True)
            df[col] = df[col].fillna(median_val if not pd.isna(median_val) else 0.0)

    # Zero-fill columns
    for col in zero_fill_cols:
        if col in df.columns:
            df[col + "_missing"] = df[col].isna().astype(int)
            df[col] = df[col].fillna(0)

    # Ensure explicit_track and artist_encoded exist
    if "explicit_track" in df.columns:
        df["explicit_track"] = pd.to_numeric(df["explicit_track"], errors="coerce").fillna(0).astype(int)
    if "artist_encoded" not in df.columns:
        df["artist_encoded"] = 0

    # Fill any missing features with 0
    for feat in ALL_MODEL_FEATURES:
        if feat not in df.columns:
            df[feat] = 0.0

    return df[ALL_MODEL_FEATURES]



def preprocess_single(sample: dict) -> pd.DataFrame:
    df = pd.DataFrame([sample])
    df = clean_column_names(df)

    if "release_date" in df.columns:
        df["release_date"] = pd.to_datetime(df["release_date"], errors="coerce")
        df["release_year"] = df["release_date"].dt.year.fillna(0).astype(int)
        df["release_month"] = df["release_date"].dt.month.fillna(0).astype(int)
        df["release_day"] = df["release_date"].dt.day.fillna(0).astype(int)
        df = df.drop(columns=["release_date"], errors="ignore")

    X = ensure_numeric_and_impute(df)

    print("----- DEBUG FEATURES -----")
    print("Count:", len(X.columns))
    print("Columns:", X.columns.tolist())
    print("---------------------------")

    return X