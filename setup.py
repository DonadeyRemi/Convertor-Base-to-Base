from cx_Freeze import setup , Executable

setup(
    name = "Convertisseur de base en base",
    version = "0.3",
    description = "Pour convertir de base en base",
    executables = [Executable("Convertisseurbb.py")]
)