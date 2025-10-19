import typer
from tools.commands import project

app = typer.Typer(help="CLI personalizada para crear y gestionar tu proyecto Flask.")
app.add_typer(project.app, name="project")

def main():
    app()

if __name__ == "__main__":
    main()