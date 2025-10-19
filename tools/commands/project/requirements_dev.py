import typer
from pathlib import Path

app = typer.Typer(help="Genera requirements-dev y archivos de configuración de desarrollo.")

# Versiones
PRECOMMIT_VERSION = "4.3.0"
BLACK_VERSION = "25.1.0"
ISORT_VERSION = "6.0.1"
RUFF_VERSION = "0.12.11"

DEFAULT_DEV_REQUIREMENTS = f"""
# DEV TOOLS
pre-commit=={PRECOMMIT_VERSION}
black=={BLACK_VERSION}
isort=={ISORT_VERSION}
ruff=={RUFF_VERSION}
"""

PRE_COMMIT_CONFIG = f"""
repos:
  - repo: https://github.com/psf/black
    rev: {BLACK_VERSION}
    hooks:
      - id: black

  - repo: https://github.com/pycqa/isort
    rev: {ISORT_VERSION}
    hooks:
      - id: isort

  - repo: https://github.com/astral-sh/ruff-pre-commit
    rev: v0.12.11
    hooks:
      - id: ruff
        args: [--fix]
"""

PYPROJECT_TOML = """
[tool.black]
line-length = 88

[tool.isort]
profile = "black"

[tool.ruff]
line-length = 88
"""

@app.command("requirements_dev")
def create_requirements_dev(
    precommit: bool = typer.Option(True, "--precommit/--no-precommit", help="Incluir pre-commit y archivos relacionados (por defecto: True)"),
    out_path: Path = typer.Option(Path("."), "--path", "-p", help="Directorio donde crear los archivos (por defecto: directorio actual)"),
):
    """
    Crea requirements-dev.txt y (opcionalmente) .pre-commit-config.yaml y pyproject.toml.
    """
    out_path = out_path.resolve()
    typer.echo(f"Generando archivos de desarrollo en: {out_path}")

    # 1. Crear requirements-dev.txt (base)
    req_dev_path = out_path / "requirements-dev.txt"
    req_dev_path.write_text(DEFAULT_DEV_REQUIREMENTS)
    typer.echo(f"✅ {req_dev_path.name} creado.")

    # 2. Si precommit solicitado crear .pre-commit-config.yaml y pyproject.toml
    if precommit:
        precommit_path = out_path / ".pre-commit-config.yaml"
        precommit_path.write_text(PRE_COMMIT_CONFIG)
        typer.echo(f"✅ {precommit_path.name} creado.")

        pyproject_path = out_path / "pyproject.toml"
        pyproject_path.write_text(PYPROJECT_TOML)
        typer.echo(f"✅ {pyproject_path.name} creado.")

        typer.echo("ℹ️ Recuerda ejecutar: pre-commit install  (tras instalar el entorno virtual y dependencias).")
    else:
        typer.echo("ℹ️ pre-commit no fue solicitado; solo se generó requirements-dev.txt.")

    typer.echo("✅ Archivos de desarrollo generados correctamente.")