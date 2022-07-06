# Empaquetado y Extensión de módulo en Python

Un proyecto mínimo para llamar código en C y distribuir un paquete Python.

Cómo usar este paquete:
1. Instalar `virtualenv` con el comando `virtualenv venv`
2. Activar el virtual env con `call .\venv\Scripts\activate.bat` o `source ./venv/bin/activate`
3. Construir con el comando `python setup.py build`
4. Instalar el paquete con `python setup.py install` o con `pip install .[dev] --force-reinstall`
