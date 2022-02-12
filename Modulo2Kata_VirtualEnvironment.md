# Entornos Virtuales (Virtual Environments) para el aislamiento y portabilidad de proyectos en Python.

## Creación de Virtual Environment utilizando ``venv``

* Creación de carpeta local mediante la instrucción ``python -m venv Mod2_Kata``, Mod2_Kata es el nombre asignado a mi carpeta de prueba.

![image](https://github.com/EmmanuelMontes/LaunchX_Katas/blob/main/images/Imagen1.PNG)

* Creación de subcarpetas de forma automática al haber ejecutado la instrucción anterior. 

![image](https://github.com/EmmanuelMontes/LaunchX_Katas/blob/main/images/Imagen2.PNG)


## Activación del Virtual Environment utilizando ``activate.bat``

La activación del entorno en Windows 10, con la ruta abierta hasta la carpeta de Scripts, mediante la instrucción: ``Mod2_Kata/Scripts/activate.bat``

![image](https://github.com/EmmanuelMontes/LaunchX_Katas/blob/main/images/Imagen3.PNG)

En la línea de comandos se observa qu el prompt cambió, en el inicio del path aparece el nombre de la carpeta entre paréntesis ``(Mod2_Kata)``. 
Lo anterior indica que el VE ha sido activado y que lo que se instale o archivos que sean creados estarán en esa estructura de carpetas, 
aislados de la demás instalación de Python.

![image](https://github.com/EmmanuelMontes/LaunchX_Katas/blob/main/images/Imagen4.PNG)

## Instalar una biblioteca

* Ejecuta el comando ``pip freeze`` para ver las bibliotecas instaladas en el entorno.

    ```
    pip freeze
    ```

La primera vez no habrá nada pues no se ha instalado ninguna librería o paquete.
A continuación, instalaremos algo para notar como cambia la salida de ``pip freeze``.

* Se ejecuta la instrucción ``pip install`` para instalar una biblioteca:
   ```
   pip install python-dateutil
   ```
* Aparecerá un mensaje de instalación satisfactoria.

* Se ejecuta nuevamente la instrucción ```pip freeze```.
    ```
    pip freeze
    ```
* Ahora notamos un cambio, ya que aparece:
    ```
    python-dateutil==2.8.2
    six==1.16.0
    ```
![image](https://github.com/EmmanuelMontes/LaunchX_Katas/blob/main/images/Imagen5.PNG)

## Desactivar un entorno virtual

La desactivación del entorno virtual en Windows 10, con la ruta abierta hasta la carpeta de Scripts, mediante la instrucción ``deactivate``

![image](https://github.com/EmmanuelMontes/LaunchX_Katas/blob/main/images/Imagen6.PNG)

La utilización de Virtual Environments me parece que es muy útil con motivos de interoperabilidad entre ambientes de prueba y desarrollo.
Otras alternativas son [Poetry](https://python-poetry.org/) y [virtualenvwrapper](https://virtualenvwrapper.readthedocs.io/en/latest/), 
que son capas de abstracción para la funcionalidad de ```venv``` además de [Docker](https://www.docker.com/) y otras herramientas.

Gracias.
