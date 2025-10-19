from pathlib import Path

import typer

from tools.commands.project.utils import write_file_from_template

app = typer.Typer(help="Genera la estructura base del proyecto Flask.")


@app.command("base")
def create_base_structure():
    """
    Crea la carpeta 'app/' con archivos base vacíos.
    """
    typer.echo("🛠️ Creando estructura base del proyecto...")

    write_file_from_template("config.py", Path("app/config.py"))
    write_file_from_template("extensions.py", Path("app/extensions.py"))
    write_file_from_template("init.py", Path("app/__init__.py"))
    write_file_from_template("run.py", Path("run.py"))

    typer.echo("✅ Estructura base creada correctamente.")
