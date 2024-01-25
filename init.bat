@echo off

if exist "env" (
    echo carpeta "env" existe
    echo "Activando entorno virtual"
    env\Scripts\activate
) else (
    echo "env" folder does not exist
    echo "Creando entorno virtual"
    python -m venv env
    echo "Activando entorno virtual"
    env\Scripts\activate
    echo "Instalando dependencias"
    pip install -r requirements.txt
    echo "Done"
)

echo.
echo Para desactivar el entorno, ejecuta: deactivate