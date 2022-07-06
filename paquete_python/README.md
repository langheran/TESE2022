# Empaquetado y Extensión de módulo en Python

Un proyecto mínimo para llamar código en C y distribuir un paquete Python.

Cómo usar este paquete:

1. Instalar `virtualenv` con el comando `virtualenv venv`
2. Activar el virtual env con `call .\venv\Scripts\activate.bat` o `source ./venv/bin/activate`
3. Construir con el comando `python setup.py build`
4. Instalar el paquete con `python setup.py install` o con `pip install .[dev] --force-reinstall`

Una vez que el paquete ha sido creado, es posible usarlo dentro de otro módulo. Para ello haremos lo siguiente.

1. Subir el paquete a un repo propio con un `fork` (o un `clone` quitando la carpeta `.git`)
2. Crear una carpeta nueva
3. En esta carpeta crear un nuevo `virtualenv`
4. Crear un archivo `requirements.txt`
5. Pegar la siguiente línea y substituir en donde sea necesario
   ```
   miModulo[dev] @ git+https://git@github.com/langheran/TESE2022.git@main#subdirectory=paquete_python
   ```
6. Ejecutar `pip install -r requirements.txt`
7. Verificar que el paquete se haya instalado correctamente
