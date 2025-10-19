from pathlib import Path

import typer

app = typer.Typer(help="Genera el archivo .env con configuración base de Flask.")

DEFAULT_SECRET = "mi_llave_secreta"

DB_URIS = {
    "mysql": "mysql://{user}:{password}@{host}:3306/{dbname}",
    "postgres": "postgresql://{user}:{password}@{host}:5432/{dbname}",
}


@app.command("env")
def create_env(db: str, user: str, password: str, host: str, dbname: str):
    """
    Crea un archivo .env con configuración base y la DATABASE_URI según los parámetros.
    """
    typer.echo("Generando .env...")

    db_uri_template = DB_URIS.get(db)
    if not db_uri_template:
        typer.echo(f"⚠️ Gestor de base de datos '{db}' no soportado.")
        raise typer.Exit()

    db_uri = db_uri_template.format(
        user=user, password=password, host=host, dbname=dbname
    )

    content = f"""
# === BASE CONFIG ===
SECRET_KEY={DEFAULT_SECRET}

# === DB ===
DATABASE_URI={db_uri}
"""

    Path(".env").write_text(content)
    typer.echo("✅ Archivo .env creado correctamente.")
