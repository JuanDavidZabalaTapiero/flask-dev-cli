from pathlib import Path

import typer

app = typer.Typer(help="Genera archivos base para tu entorno de Flask.")

DEFAULT_REQUIREMENTS = """# FLASK
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
    user: str = typer.Option("root", help="Usuario de la base de datos"),
    password: str = typer.Option("", help="Contraseña del usuario"),
    host: str = typer.Option("localhost", help="Host de la base de datos"),
    dbname: str = typer.Option("mi_base", help="Nombre de la base de datos"),
):
    typer.echo("🛠️ Generando requirements.txt...")

    content = DEFAULT_REQUIREMENTS
    driver = DB_DRIVERS.get(db)
    if driver:
        content += f"\n# DRIVER (DB)\n{driver}"

    Path("requirements.txt").write_text(content)
    typer.echo("✅ Archivo requirements.txt creado correctamente.")

    # Crear el .env con los valores ingresados
    from tools.commands.project import env_file

    env_file.create_env(db=db, user=user, password=password, host=host, dbname=dbname)
