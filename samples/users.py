"""Small safe baseline for the CodeRabbit Python review labs."""

from collections.abc import Mapping, Sequence
from pathlib import Path
import sqlite3


def get_user(conn: sqlite3.Connection, username: str) -> tuple[object, ...] | None:
    """Return one user by name using a parameterized query."""
    return conn.execute(
        "SELECT * FROM users WHERE name = ?", (username,)
    ).fetchone()


def average_age(users: Sequence[Mapping[str, object]]) -> float:
    """Return the average age, or zero when there are no users."""
    if not users:
        return 0.0
    return sum(int(user["age"]) for user in users) / len(users)


def load_config(path: str | Path) -> str:
    """Read a UTF-8 configuration file and let callers handle I/O errors."""
    return Path(path).read_text(encoding="utf-8")
