from PyQt6.QtWidgets import QMessageBox


def mostrar_acerca_de(parent=None):
    titulo = "Acerca de Escuadra"
    
    try:
        from escuadra import __version__
        version = __version__
    except (ImportError, AttributeError):
        version = "0.1.0"
    
    texto = f"""
    <b>Escuadra</b><br>
    Versión {version}<br>
    <br>
    Suite de herramientas de cálculo para distintas carreras de ingeniería<br>
    <br>
    <b>Licencia:</b> MIT<br>
    <br>
    <b>Créditos:</b><br>
    Desarrollado por la Carrera de Ingeniería de Sistemas e Informática,<br>
    Facultad Nacional de Ingeniería,<br>
    Universidad Técnica de Oruro
    """
    
    QMessageBox.about(parent, titulo, texto)
