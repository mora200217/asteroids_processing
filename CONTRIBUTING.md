# Contributing Asteroids 
Este documento explica los lineamientos de contribución al proyecto. 

- Inicialmente, deben agregar su nombre al README del proyecto, con el lenguaje de su elección para el proyecto. (JS o Python), y aspecto del proyecto en el que se enfocará. (Leer más adelante)

Se hará uso de la libreria de processing para el desarrollo de la interfaz. 

JS: https://p5js.org
Python: https://py.processing.org

El proyecto se dividirá en 3 puntos. 

* Interfaz Gráfica: Puntuacion, Menú
* Nave: Movimiento y Disparo
* Asteroides: Construcción, Movimiento e interacción con Nave 

Una vez se agregue su nombre al README, se deberá mandar un correo a amoralesma@unal.edu.co Con su nombre y lenguaje a usar, y aspecto a elegir. 

Nota: Si más de una persona está trabajando en el mismo aspecto, deben dividirse sub-features para completarlo.  

---

El repositorio tiene 3 ramas principales. 
* master
* dev 
* docs 

La rama master estará bloqueada, y solo podrá actualizarse con el respectivo PR desde dev. Se realizará una revisión de los cambios y se aprobará/rechazará la solicitud. 

## Manejo de Features 
Cada nueva característica a incluir en el repositorio, será agregada como un nuevo __feature__ a dev. Para esto debe crearse una rama desde la última versión disponible de __dev__ y se llamará `f/language/feature`. Por ejemplo, si se desea agregar un sistema de puntuación en el proyecto de JS, se podría llamar el feature score y la rama se crearía como `f/js/score`. 

Dentro de las ramas de feature, se deben agregar los respectivos commits que consideren necesarios para estructurar el historial de la rama. Una vez terminado su respectivo feature, se enviará un PR a la rama dev, en donde el los miembros del equipo deben comentar, revisar y aprobar los cambios agregados antes de realizar el merge. 

No deben borrar las ramas de features. Servirán para futura revisión.

## Documentacion 
Cada cambio que se realice, debe tener su respectiva documentanción (algo simple), explicando que aporta el feature al proyecto. Nota: No es necesario explicar el funcionamiento técnico o el código fuente del feature. Esta explicacion 

## Estructura del Proyecto 
Existirá un carpeta `/source` en donde estará todo el código del proyecto. Internamente se tienen las carpetas `/JS` y `\python`, en donde se encontrará todo el código necesario para el funcionamiento del juego. Como primer commit, se tiene la base en ambos lenguajes. 
* En JS está el index principal con los scripts para comenzar a usar P5JS. 
* En python está un main.py y un requirements.txt. Todo maneja de modulos externos debe manejarse desde el requirements.txt con entornos virtuales (virtualenv) y realizer el respectivo freeze en el txt para guardar los requerimientos. (Si tienen dudas con respecto a esto, escribanme) 


