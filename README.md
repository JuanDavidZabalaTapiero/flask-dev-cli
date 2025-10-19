# CONFIG DEV

## 1. Instalar Typer
Antes de usar los comandos del CLI, instala Typer (necesario para ejecutar los comandos iniciales):
```bash
pip install "typer[all]"
```

# 2. Crear requirements-dev.txt
Este comando genera un archivo con las dependencias de desarrollo.
```bash
python -m tools.cli project dev requirements_dev
```
Parámetros:
* `--precommit`: Incluye dependencias relacionadas con pre-commit hooks. (default = True)
* `--out_path`: Ruta de salida para guardar el archivo. (default = raíz del proyecto)

## 3. Crear requirements.txt
Este comando genera el archivo principal de dependencias.
```bash
python -m tools.cli project new requirements
```
Parámetros:
* `--db`: Incluye dependencias relacionadas con bases de datos. (default = True)

## Notas
* Los comandos deben ejecutarse desde la raíz del proyecto.
* Los módulos se encuentran dentro del paquete `tools/commands/project/`.
* Puedes ir agregando nuevos subcomandos o módulos según tus necesidades (por ejemplo, para crear .env, configurar Docker, etc.).

