import hashlib
import secrets

from .config import settings


def generate_api_key() -> tuple[str, str, str]:
    """Returns (raw_key, prefix_for_display, sha256_hash_to_store)."""
    token = secrets.token_urlsafe(32)
    raw_key = f"{settings.api_key_prefix}{token}"
    prefix = raw_key[: len(settings.api_key_prefix) + 6]
    key_hash = hash_key(raw_key)
    return raw_key, prefix, key_hash


def hash_key(raw_key: str) -> str:
    return hashlib.sha256(raw_key.encode()).hexdigest()
