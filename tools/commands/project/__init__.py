import typer
from tools.commands.project import requirements
from tools.commands.project import requirements_dev

app = typer.Typer(help="Comandos relacionados con la configuración inicial del proyecto.")
app.add_typer(requirements.app, name="new") # project new requirements
app.add_typer(requirements_dev.app, name="dev") # project dev requirements_dev