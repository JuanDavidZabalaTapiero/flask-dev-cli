# CONFIG INICIAL

## 1. Instalar Typer
Antes de usar los comandos del CLI, instala Typer (necesario para ejecutar los comandos iniciales):
```bash
pip install "typer[all]"
```

## 2. Crear requirements.txt y .env
Este comando genera el archivo principal de dependencias y archivo con variables de entorno.
```bash
python -m tools.cli project new requirements
```
Parámetros:
* `--db`: Gestor de base de datos (mysql, postgres). (default = mysql)
* `--user`: Usuario del gestor de base de datos. (default = root)
* `--password`: Contraseña del usuario. (default = "")
* `--host`: Host de conexión. (default = localhost)
* `--dbname`: Nombre de la base de datos. (default = mi_base)

## Notas
* Los comandos deben ejecutarse desde la raíz del proyecto.
* Los módulos se encuentran dentro del paquete `tools/commands/project/`.
* Puedes ir agregando nuevos subcomandos o módulos según tus necesidades (por ejemplo, para crear .env, configurar Docker, etc.).
