from distutils.core import setup, Extension
from distutils.util import convert_path
import platform

ostype = platform.system().lower()

main_ns = {}
init_path = convert_path('src/__init__.py')
with open(init_path) as init_file:
    exec(init_file.read(), main_ns)

setup(
    author="Nisim.Hurst",
    author_email="nhurst@ndscognitivelabs.com",
    description="Paquete para demostrar el uso de paquetes en Python",
    name = 'miModulo',
    version = main_ns['__version__'],
    ext_package='miModulo',
    ext_modules = (
        [Extension('CInterface', ['src/CInterface/test.c'])]
        if ostype == 'windows'
        else []
    ),  # opcional
    packages=[
        'miModulo',
        'miModulo.PythonInterface',
        'miModulo.CommandLineInterface'
    ],
    package_dir={
        'miModulo': 'src',
        'miModulo.PythonInterface': 'src/PythonInterface',
        'miModulo.CommandLineInterface': 'src/CommandLineInterface'
    },
    package_data={'miModulo.PythonInterface': ['data/*.csv']},
    install_requires=[
        "Click",
        "pandas",
    ],
    entry_points='''
        [console_scripts]
        hola-tese=miModulo.CommandLineInterface:cli
    ''',
    extras_require = {
       'dev': ['pycodestyle'],
   },
    python_requires=">=3.7.0",
)
