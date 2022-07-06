# %%
# Primero nos aseguramos que el módulo no esté instalado
try:
    del sys.modules["miModulo"]
except:
    ...
%sx pip uninstall miModulo -y

# %%
# Construimos el módulo

%sx python setup.py build

# %%
# Reinstalamos el módulo

%sx pip install .[dev] --force-reinstall

# %%
# En caso de querer desarrollar al mismo tiempo que debugueamos, es posible cargar el módulo en modo editable

%sx pip install -e .

# %%
# Veamos cuales son las propiedades del módulo
import importlib
import miModulo
print(miModulo.__version__)
importlib.reload(miModulo)
display(
    dir(miModulo)
)
import miModulo.CInterface as ci
display(
    dir(ci)
)
import miModulo.PythonInterface as pi
display(
    dir(pi)
)

# %%
# Ahora una prueba rápida llamando a la función en C

import miModulo.CInterface as ci
ci.helloworld()
ci.fib(6)

# Vemos que el hello no se imprime, veamos en la consola a ver si ahí si se ve.

# %%
# Ahora llamemos a una función de Windows nativa, si estás usando linux, por favor modifica el código en setup.py para excluir este modulo

import miModulo.CInterface as ci
ci.message_box("Hola")

# %%
# Podemos ver cómo los recursos del paquete fueron instalados correctamente

import miModulo.PythonInterface as pi
for a in pi.HolaTESE('BigQuery'):
    print(a)
