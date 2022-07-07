# Introducción al desarrollo de paquetes en Python

## Trucos para desarrollar más rápido

Estos son los cheatsheets recomendados para `Python`, `pandas`, `matplotlib`. 

- Python
  - https://github.com/gto76/python-cheatsheet
- Pandas
  - [Pandas_Cheat_Sheet.pdf](./docs/Pandas_Cheat_Sheet.pdf)
- Matplotlib
  - [matplotlib-cheatsheets.pdf](./docs/matplotlib-cheatsheets.pdf)
  - [handout-beginner.pdf](./docs/handout-beginner.pdf)
  - [handout-intermediate.pdf](./docs/handout-intermediate.pdf)
  - [handout-tips.pdf](./docs/handout-tips.pdf)

También se recomienda modificar los [snippets](command:workbench.action.openSnippets) para `markdown` y `python`.

## Empaquetado y Extensión de módulo en Python

Asumiendo que ya conocemos Python, podemos hacer proyecto mínimo para llamar código en C y distribuir un paquete (source distribution).

Es posible crear también distribuciones que no dependen del compilador. Para más información ver [wheels](https://realpython.com/python-wheels/).

### Requerimientos

Lo vamos a hacer local. Para esto necesitas instalar:

- [vscode](https://code.visualstudio.com/download)
  - habilitar [Python](vscode:extension/ms-python.python)
- [miniconda](https://docs.conda.io/en/latest/miniconda.html)
- [git](https://github.com/git-guides/install-git)
- instalar `virtual env`
    ```
    pip install virtualenv
    ```
  - opcionalmente activar el ambiente `miniconda` o trabajar en el ambiente `(base)`
    ```
    conda create --name tese
    conda activate tese
    ```
- Descargar el repo localmente con el comando 
    ```
    git clone https://github.com/langheran/TESE2022.git
    ```

Si estás en windows, compilaremos nuestro módulo en C y usaremos algo de la librería `<windows.h>` por lo tanto necesitas tener este requerimiento también.

- [Build Tools for Visual Studio](http://download.microsoft.com/download/5/F/7/5F7ACAEB-8363-451F-9425-68A90F98B238/visualcppbuildtools_full.exe).
- Verifica que desde la ventana que vas a hacer el `python setup.py build` puedas ver el archivo `cl.exe`, por ejemplo el mío está en `C:\Program Files (x86)\Microsoft Visual Studio\2019\BuildTools\VC\Tools\MSVC\14.29.30133\bin\Hostx86\x86\cl.exe`, ya sea entrando desde la consola de developer o agregando ese path al %PATH%. Ahorita no te preocupes si no la tienes, explicaré más de esto adelante.
- También es recomendable instalar otros plugins para `vscode` que vienen [aquí](https://code.visualstudio.com/docs/cpp/config-msvc#_prerequisites)
  - En especial [cpptools](vscode:extension/ms-vscode.cpptools)

### Instrucciones para crear el paquete

Cómo usar este paquete:

1. Crear `virtualenv` con el comando 
    ```
    virtualenv venv
    ```
2. Activar el virtual env con `call .\venv\Scripts\activate.bat` o `source ./venv/bin/activate`
3. Construir con el comando `python setup.py build`
4. Instalar el paquete con `python setup.py install` o con `pip install .[dev] --force-reinstall`
   1. Estas pruebas se encuentran en el [Jupyter Interactive](./test.py) que abriremos en [vscode](http://code.visualstudio.com/docs/python/jupyter-support-py)
5. Opcionalmente puedes subir tu paquete al _test server_ usando estas [instrucciones oficiales](https://packaging.python.org/en/latest/tutorials/packaging-projects/#uploading-the-distribution-archives)

### Estructura de archivos

| file                                                                             | description                                                              |
| -------------------------------------------------------------------------------- | ------------------------------------------------------------------------ |
| [./README.md](./README.md)                                                       | Instructivo                                                              |
| [./setup.py](./setup.py)                                                         | Archivo principal usado por `distutils` para construir el paquete        |
| [./src/CInterface/test.c](./src/CInterface/test.c)                               | Entrada para el módulo de extensión en C                                 |
| [./src/CInterface/message_box.h](./src/CInterface/message_box.h)                 | Función en C para desplegar un MessageBox con parámetros de Python       |
| [./src/CommandLineInterface/__init__.py](./src/CommandLineInterface/__init__.py) | Definición de los imports de la herramienta de consola.                  |
| [./src/CommandLineInterface/main.py](./src/CommandLineInterface/main.py)         | Definición de parámetros y funciones a usar en la herramienta de consola |
| [./src/PythonInterface/__init__.py](./src/PythonInterface/__init__.py)           | Definición de los imports del paquete en Python                          |
| [./src/PythonInterface/data/alumnos.csv](./src/PythonInterface/data/alumnos.csv) | Datos a usar en el paquete Python                                        |
| [./src/PythonInterface/main.py](./src/PythonInterface/main.py)                   | Clase que lleva a cabo la lógica en el paquete Python                    |
| [./src/__init__.py](./src/__init__.py)                                           | Especificar la versión del paquete                                       |
| [./test.py](./test.py)                                                           | Python Interactive Notebook para probar el paquete                       |
| [./build](./build)                                                               | Carpeta que se genera al compilar el paquete                             |

### Instrucciones para usar el paquete

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
7. También es posible instalar este requerimiento con `pip`
    ```
    pip install git+https://git@github.com/langheran/TESE2022.git@main#subdirectory=paquete_python
    ```
8. Verificar que el paquete se haya instalado correctamente
   1. En una terminal ejecutar el comando 
    ```
    hola-tese --busqueda "Rubén"
    ```
   2. El resultado debe ser
    ```
    {'Nombre': 'Rubén', 'Apellido': 'Raya', 'Intereses': 'Amazon Alexa'}
    ```
   3. Si estás en windows también puedes ejecutar el siguiente comando
    ```
    hola-tese --msgbox "Hola TESE"
    ```
   4. El resultado debe ser
   
      ![msgbox](./images/msgbox.png)
