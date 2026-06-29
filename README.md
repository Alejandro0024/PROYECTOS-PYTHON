readme_content = """# Desarrollo programa piedra papel o tijera

Este repositorio contiene la implementación en Python del clásico juego de **Piedra, Papel o Tijera**, diseñado para ser ejecutado en la consola interactiva.

## Información del Proyecto
* **Integrantes:** Alejandro Benalcazar
* **Fecha:** 2026-06-28
* **Lenguaje:** Python 3.x

## Objetivo del Sistema
El objetivo principal de este programa es proporcionar una experiencia interactiva y lúdica mediante un juego de consola donde un usuario humano pueda competir contra la inteligencia artificial (CPU) en el juego de "Piedra, Papel o Tijera". 
El sistema busca automatizar la lógica de evaluación de reglas, mantener un registro continuo del puntaje de ambos jugadores en tiempo real y permitir una salida ordenada mostrando los resultados acumulados.

## Descripción de Funcionalidades
El programa cuenta con un flujo continuo basado en consola que ofrece las siguientes características:

1. **Inicialización y Control de Marcadores:** El sistema inicia con los puntajes en cero (`0`) tanto para el jugador humano como para la CPU.
2. **Entrada de Usuario Interactiva:** Solicita continuamente al usuario elegir una de las opciones válidas: `'Piedra'`, `'Papel'`, `'Tijera'` o la palabra clave `'Salir'` para abandonar la partida.
3. **Validación de Entradas:** Si el usuario ingresa una opción que no pertenece a las alternativas válidas o comete un error de escritura, el sistema muestra un mensaje de "Entrada inválida" y le permite reintentar sin alterar el flujo del juego.
4. **Inteligencia Artificial (CPU):** Utiliza la librería nativa de Python para realizar una elección aleatoria y justa entre las tres opciones disponibles en cada ronda.
5. **Evaluación Automática de Reglas:** Aplica la lógica estándar del juego para determinar el resultado de cada ronda:
   * **Empate:** Si ambos eligen la misma opción.
   * **Victoria del Humano:** Piedra vence a Tijera, Papel vence a Piedra, o Tijera vence a Papel.
   * **Victoria de la CPU:** En cualquier otro caso de combinación distinta al empate.
6. **Actualización del Marcador en Tiempo Real:** Al concluir cada ronda, se incrementa el puntaje correspondiente del ganador y se imprime el marcador actual.
7. **Cierre de Juego y Reporte Final:** Al ingresar `'Salir'`, el bucle se detiene inmediatamente y el sistema muestra un resumen detallado con la puntuación final de ambos competidores.

## Código Fuente Incluido
El script principal utiliza un bucle controlado de la siguiente manera:
