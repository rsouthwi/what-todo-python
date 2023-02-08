"""
the "database" should be pulled from the JSON file into memory as
soon as possible and kept there through the entire session.
all "writes/changes/deletes" should get to the JSON file immediately
"""
from os import walk
from pathlib import Path

from config import DATA_LOCATION
from todo import DB_WRITE_ERROR, SUCCESS

DEFAULT_DB_USER = "Default User"

# def init_db(db_path: Path) -> int:
#


def get_all_user_dbs():
    db_files = []
    print(DATA_LOCATION)
    for (_, _, filename) in walk(DATA_LOCATION):
        print(filename)
        if ".json" in filename:
            db_files.append(filename.replace(".json", ""))
    return db_files
