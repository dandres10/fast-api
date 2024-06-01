Paso 1: Instalar Python 3.11

/bin/bash -c "$(curl -fsSL <https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh>)"

brew install python@3.11

python3.11 --version


Paso 2: Configurar un Entorno Virtual

python3.11 -m venv env


source env/bin/activate


Paso 3: Instalar FastAPI y Uvicorn

pip install fastapi

pip install uvicorn


Ejecuta tu aplicación: Usa Uvicorn para ejecutar tu aplicación:

uvicorn main:app --reload

exec zsh

python -m pip freeze > pipfiles.txt