import typer
from pathlib import Path


app = typer.Typer(help="Genera archivos base para tu entorno de Flask.")

DEFAULT_REQUIREMENTS = """
# FLASK
Flask==3.1.2

# ENV
python-dotenv==1.1.1

# DB
Flask-SQLAlchemy==3.1.1

# MIGRACIONES
Flask-Migrate==4.1.0

# FORMS
Flask-WTF==1.2.2
"""

DB_DRIVERS = {
    "mysql": "mysqlclient==2.2.7",
    "postgres": "psycopg2-binary==2.9.10",
}

@app.command("requirements")
def create_requirements(
    db: str = typer.Option("mysql", help="Gestor de base de datos (mysql, postgres)"),   
):
    """
    Crea un archivo requirements.txt con dependencias base según el gestor de base de datos seleccionado.
    """
    typer.echo("Generando requirements.txt...")

    # Crear contenido base
    content = DEFAULT_REQUIREMENTS

    # Añadir driver según DB
    driver = DB_DRIVERS.get(db)
    if driver:
        content += f"\n# DRIVER (DB)\n{driver}"

    Path("requirements.txt").write_text(content)
    typer.echo("✅ Archivo requirements.txt creado correctamente.")