#ifndef UNICODE
#define UNICODE
#endif

#pragma comment(lib,"user32.lib") 

#include <Python.h>
#include <windows.h>
#include "message_box.h"

// Función 1: Una simple función Hello World
static PyObject* helloworld(PyObject* self, PyObject* args) 
{   
    printf("Hola \n");
    Py_RETURN_NONE;
    return Py_None;
}

// Función 2: La implementación de la serie fibonacci en C
int Cfib(int n)
{
    if (n < 2)
        return n;
    else
        return Cfib(n-1)+Cfib(n-2);
}
// La conexión a Python de la función en C
// Va a tomar como entrada solo un valor sin nombre
static PyObject* fib(PyObject* self, PyObject* args)
{
    // instanciar nuestro valor desde los parámetros de Python
    int n;
    // verificar el parámetro de entrada
    if(!PyArg_ParseTuple(args, "i", &n))
        return NULL;
    // regresar el valor fibonacci calculado
    return Py_BuildValue("i", Cfib(n));
}


// La definición de la estructura de funciones
// Se requiere incluir `NULL` para indicar la terminación de la definición
// de nuestro método
static PyMethodDef myMethods[] = {
    { "helloworld", helloworld, METH_NOARGS, "Prints Hello Munir" },
    { "message_box", DisplayMessageBox, METH_VARARGS, "Prints Hello" },
    { "fib", fib, METH_VARARGS, "Computes Fibonacci" },
    { NULL, NULL, 0, NULL }
};

// La estructura que define nuestro módulo
static struct PyModuleDef miModulo = {
    PyModuleDef_HEAD_INIT,
    "CInterface",
    "Test Module",
    -1,
    myMethods
};

// Inicializa nuestro módulo con la estructura de arriba
PyMODINIT_FUNC PyInit_CInterface(void)
{
    return PyModule_Create(&miModulo);
}
