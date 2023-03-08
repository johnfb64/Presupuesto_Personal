--------------CREACION DE EJECUTABLES PARA WINDOWS-----------------

En cmd en la ruta del proyecto, ejecutar los siguientes comandos:

- Comando para crear ejecutable

python -m PyInstaller main.py

- Comando para crear ejecutable de un solo archivo:

python -m PyInstaller main.py --onefile

- Comando para crear ejecutable de un solo archivo sin ventana prompt de Windows:

python -m PyInstaller main.py --onefile -w


Al finalizar el archivo se encuentra en la ruta del proyecto en la carpeta "dist"
