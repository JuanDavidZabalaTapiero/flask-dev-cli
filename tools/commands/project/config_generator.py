from pathlib import Path

import typer


def create_config_file():
    """
    Genera el archivo app/config.py con configuración base.
    """
    app_path = Path("app")
    app_path.mkdir(exist_ok=True)

    config_path = app_path / "config.py"
    if config_path.exists():
        typer.echo("⚠️ app/config.py ya existe, se omitió.")
        return

    content = """import os

from dotenv import load_dotenv

load_dotenv()


class Config:
    SECRET_KEY = os.getenv("SECRET_KEY", "mi_llave_secreta")
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URI") or os.getenv("DATABASE_URL")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
"""

    config_path.write_text(content)
    typer.echo("✅ Archivo app/config.py creado correctamente.")
