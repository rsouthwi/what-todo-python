"""
the "database" should be pulled from the JSON file into memory as
soon as possible and kept there through the entire session.
all "writes/changes/deletes" should get to the JSON file immediately
"""

from pathlib import Path

from todo import DB_WRITE_ERROR, SUCCESS

DEFAULT_DB_USER = "Default User"

# def init_db(db_path: Path) -> int:
#