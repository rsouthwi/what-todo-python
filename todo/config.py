from pathlib import Path

from todo import SUCCESS, DIR_ERROR, FILE_ERROR, DB_WRITE_ERROR

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_LOCATION = Path(__file__).resolve().parent.parent.joinpath("data")


def init_app(user_db: str) -> int:
    """
    initialize application
    :param user_db:
    :return:
    """
    config_code = _init_db_file()
    if config_code != SUCCESS:
        return config_code
    database_code = _create_database(user_db)
    return database_code


def _init_db_file() -> int:
    try:
        DATA_LOCATION.mkdir(exist_ok=True)
    except OSError:
        return DIR_ERROR
    try:
        DATA_LOCATION.touch(exist_ok=True)
    except OSError:
        return FILE_ERROR
    return SUCCESS


def _create_database(user_db: str) -> int:
    db_file = DATA_LOCATION / f"{user_db}.json"
    try:
        with db_file.open("w") as file:
            file.write("{}")
    except OSError:
        return DB_WRITE_ERROR
    return SUCCESS

