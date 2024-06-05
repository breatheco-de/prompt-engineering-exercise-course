# ¿Qué son los "Shots" en la Creación de Prompts? 🎬

En el contexto de la IA y el aprendizaje automático, los "shots" se refieren al número de ejemplos proporcionados al modelo para ayudarlo a entender la tarea. Vamos a desglosar los diferentes tipos:

#### Zero-Shot Prompting

El zero-shot prompting significa darle a la IA una tarea sin ningún ejemplo. La IA tiene que depender únicamente de su conocimiento preexistente y las instrucciones para generar una respuesta.

**Ejemplo:**

```text
Genera un objeto JSON que represente a un usuario
```

#### One-Shot Prompting

El one-shot prompting implica proporcionar a la IA un ejemplo para ayudarla a entender mejor la tarea.

**Ejemplo:**

```text
Genera un objeto JSON que represente a un usuario
Ejemplo:
"""
{
    "nombre": "Juan Pérez",
    "edad": 30,
    "correo": "juan.perez@ejemplo.com"
  }
"""
```

> **Pista:** Recuerda usar delimitadores 👀.

#### Few-Shot Prompting

El few-shot prompting significa darle a la IA unos pocos ejemplos para mejorar su comprensión de la tarea.

> Nota: En general, para los modelos de lenguage grandes no es necesario darle muchos ejemplos para que comprendan un patrón, usualmente con 2 o 3 ejemplos es suficientes dependiendo de la complejidad de la tarea.

**Ejemplo:**

```text
Genera un diálogo de película para una comedia romántica. Hay dos personajes, Alicia y Roberto, que son amigos de la infancia y se enamoran.

Ejemplos:
<Alicia>: Siempre he tenido un crush contigo, Roberto.
<Roberto>: Nunca lo supe, Alicia. Yo siento lo mismo.

La escena termina con ellos tomados de la mano y mirándose a los ojos.
```

#### Many-Shot Prompting

El many-shot prompting implica proporcionar a la IA muchos ejemplos. Esto se usa a menudo cuando la tarea es compleja y requiere más contexto y ejemplos para ser comprendida.


### Por Qué los Ejemplos Ayudan 🧩

Proporcionar ejemplos en los prompts puede mejorar significativamente el rendimiento de la IA. Aquí hay algunas razones por las que:

1. **Comprensión Contextual:** Los ejemplos le dan a la IA una mejor comprensión de la tarea al proporcionar contexto.
2. **Reconocimiento de Patrones:** La IA puede reconocer patrones en los ejemplos y aplicarlos para generar respuestas más precisas.
3. **Reducción de Ambigüedad:** Los ejemplos ayudan a reducir la ambigüedad, facilitando que la IA entienda lo que se espera.

## PISTAS 🤖

1. Experimenta con diferentes tipos de prompts (zero-shot, one-shot, few-shot y many-shot) usando los ejemplos proporcionados.
2. Observa cómo cambian las respuestas de la IA con el número de ejemplos dados.
3. Intenta crear tus propios prompts para diferentes tareas y ve cómo afecta la salida el proporcionar ejemplos.

¡Vamos a poner en práctica lo que has aprendido sobre los "shots" en la creación de prompts! 🚀
