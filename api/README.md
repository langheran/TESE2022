# Consumir nuestro modelo desde Flask

1. Instalar los requerimientos
    ```
    pip install -r requirements.txt
    ```
2. Correr la aplicación con `gunicorn`
    ```
    gunicorn app:app
    ```
3. Crear un `.env` tomando como base `.env.example`
   1. substituir `GCP_PROJECT` por el nombre del proyecto en nuestro Jupyter
   2. pegar json con las credenciales en `GOOGLE_CREDENTIALS`
      1. substituir `\n` por `\\n` 
      2. substituir `"` for `\"`
4. Para debuguear localmente se recomienda usar [vscode](https://code.visualstudio.com/download) con las extensiones de [Python](vscode:extension/ms-python.python) y [REST Client](vscode:extension/humao.rest-client)
