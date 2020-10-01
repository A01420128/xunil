# xunil
## Instalacion
De preferencia usar siempre python3, se puede ocupar pip3 o pip. (Es la version de python que tengan)
- installar virtualenv, esto ayuda a mantener la lib flask en la carpeta, 
sin embargo no es necesario y se puede installar Flask globalmente si se tienen
los permisos::
    - WIN: 
        - python3 -m venv venv
    - MAC:
        - sudo pip3 install virtualenv
- Crear el venv en la carpeta del repo:
    - WIN:
        - py -3 -m venv venv
    - MAC:
        - python3 -m virtualenv venv
- Activar el venv, este paso se repite cada vez que se quiera trabajar en el proy:
    - WIN:
        - .\venv\Scripts\activate
    - MAC:
        - source venv/bin/activate
- Se desactiva con:
    - deactivate 
- Si algo sale mal aqui hay otra forma: https://mothergeo-py.readthedocs.io/en/latest/development/how-to/venv-win.html
- Ya activado el venv installar Flask:
    - pip3 install Flask

## Mostrar la pagina en localhost:
- Correr python3 app.py, si usaron venv tiene que estar activado para que funcione..
- Ahi muestra en que puerto y direccion esta corriendo.
- Ya se puede abrir en el navegador.

## Flask
- app.route es la direccion en el navegador
- ese metodo regresa una template, pero antes se le puede enviar informacion.
- En las templates si esta entre {%%} son commandos y {{}} son variables del codigo en python.

## Bootstrap
- Agrege bootstrap para facilitar la presentacion
- [Documentacion de bootstrap](https://getbootstrap.com/docs/4.5/getting-started/introduction/)
