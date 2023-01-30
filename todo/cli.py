from typing import Optional

import typer

from todo import __app_name__, __version__, config, database, ERRORS

app = typer.Typer()


@app.command()
def init(
        user_db: str = typer.Option(
            str(database.DEFAULT_DB_USER),
            "--user",
            "-u",
            prompt="Enter User Name"
        )
) -> None:
    app_init_error = config.init_app(user_db)
    if app_init_error:
        typer.secho(
            f"Creating user db failed with {ERRORS[app_init_error]}",
            fg=typer.colors.RED
        )
        raise typer.Exit(1)
    typer.secho(f"The to-do database is {app_init_error}", fg=typer.colors.GREEN)


def _version_callback(value: bool) -> None:
    if value:
        typer.echo(f"{__app_name__} v{__version__}")
        raise typer.Exit()


@app.callback()
def main(version: Optional[bool] = typer.Option(
    None,
    "--version",
    "-v",
    help="Show the application's version and exit.",
    callback=_version_callback,
    is_eager=True)
) -> None:
    return
