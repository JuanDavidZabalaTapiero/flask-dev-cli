from pathlib import Path


def write_file_from_template(template_name: str, destination: Path):
    """
    Copia el contenido de un archivo plantilla desde project/templates/ al destino indicado.
    """
    template_path = Path(__file__).parent / "templates" / template_name
    if not template_path.exists():
        raise FileNotFoundError(f"Plantilla no encontrada: {template_path}")

    destination.parent.mkdir(parents=True, exist_ok=True)
    destination.write_text(template_path.read_text(encoding="utf-8"))
