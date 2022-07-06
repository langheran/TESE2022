#include <Python.h>
#include <windows.h>

static PyObject* DisplayMessageBox(PyObject* self, PyObject* args)
{
    const char *str;
    if(!PyArg_ParseTuple(args, "s", &str))
        return NULL;

    wchar_t message[4096] = {0};
    MultiByteToWideChar(0, 0, str, strlen(str), message, strlen(str));

    int msgboxID = MessageBox(
        NULL,
        (LPCWSTR)message,
        (LPCWSTR)L"Ejemplo de MessageBox",
        MB_ICONINFORMATION | MB_OKCANCEL | MB_DEFBUTTON2
    );

    switch (msgboxID)
    {
    case IDCANCEL:
        // TODO: add code
        break;
    case IDTRYAGAIN:
        // TODO: add code
        break;
    case IDCONTINUE:
        // TODO: add code
        break;
    case IDOK:
        // TODO: add code
        break;
    }

    return Py_BuildValue("i", msgboxID);
}
