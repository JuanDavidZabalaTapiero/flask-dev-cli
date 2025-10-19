from pathlib import Path

import typer

from tools.commands.project.config_generator import create_config_file

app = typer.Typer(help="Genera la estructura base del proyecto Flask.")


@app.command("base")
def create_base_structure():
    """
    Crea la carpeta 'app/' con archivos base vacíos.
    """
    typer.echo("🛠️ Creando estructura base del proyecto...")

    app_path = Path("app")
    app_path.mkdir(exist_ok=True)

    for filename in ["__init__.py", "extensions.py"]:
        (app_path / filename).touch()

    Path("run.py").touch()

    # Crear config.py con contenido
    create_config_file()

    typer.echo(
        "✅ Estructura base creada: app/, __init__.py, config.py, extensions.py y run.py"
    )
