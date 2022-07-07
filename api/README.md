# Consumir nuestro modelo desde Flask

1. Instalar los requerimientos
    ```
    pip install -r requirements.txt
    ```
2. Correr la aplicación con `gunicorn`
    ```
    gunicorn app:app
    ```
3. Para debuguear localmente se recomienda usar [vscode](https://code.visualstudio.com/download) con las extensiones de [Python](vscode:extension/ms-python.python) y [REST Client](vscode:extension/humao.rest-client)
