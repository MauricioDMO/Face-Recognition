@echo off

if exist "env" (
    echo "env" existe
    echo Activando entorno virtual
    env\Scripts\activate
) else (
    echo "env" no existe
    echo Creando entorno virtual
    py -m venv env
    echo Activando entorno virtual
    env\Scripts\activate
    echo Instalando dependencias
    pip install -r requirements.txt
    echo Entorno virtual creado y activado
)

echo.
echo Para desactivar el entorno, ejecuta: deactivate