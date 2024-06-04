### Sobre Contexto y Alucinaciones 🧠

La importancia del contexto en la creación de prompts es innegable. En esta lección, exploraremos qué es el contexto, cómo proporcionar suficiente contexto para obtener salidas precisas y relevantes de la IA, y cómo evitar **alucinaciones**.

### Entendiendo el Contexto en la Creación de Prompts 📚

El contexto es crucial cuando interactúas con modelos de IA. Ayuda a la IA a entender el trasfondo y los detalles específicos de tu solicitud, lo que lleva a respuestas más precisas y relevantes. 

Si no proporcionas suficiente contexto, la IA podría generar información irrelevante o incorrecta, lo que también puede llevar a alucinaciones donde la IA genera información que no es precisa o relevante.


### ¿Qué son las Alucinaciones? 😵‍💫

U️na alucinación ocurre cuando la IA genera información que no es cierta debido a que no tiene suficiente contexto o que en los datos de entrenamiento no se incluye la información específica que estás solicitando.


#### Mal Prompt:
```text
¿Cuál fue la magnitud del terremoto que ocurrió el 3 de abril de 2024 en Taiwán? ¿Cuántas personas resultaron heridas?
```
Este prompt carece de contexto y podría llevar a respuestas inexactas o irrelevantes porque los datos de entrenamiento podrían no incluir este evento específico.

#### Buen Prompt:
```text
¿Cuál fue la magnitud del terremoto que ocurrió el 3 de abril de 2024 en Taiwán? ¿Cuántas personas resultaron heridas?

Contexto de Wikipedia: El 3 de abril de 2024, a las 07:58:11 NST (23:58:11 UTC el 2 de abril), un terremoto de magnitud 7.4 golpeó a 15 km (9.3 mi) al sur de la ciudad de Hualien, en el condado de Hualien, Taiwán. Al menos 18 personas murieron y más de 1,100 resultaron heridas en el terremoto. Es el terremoto más fuerte en Taiwán desde el terremoto de Jiji en 1999, con tres réplicas por encima de magnitud 6.0.
```
En este prompt, proporcionamos suficiente contexto sobre el terremoto en Taiwán, lo que hará que la respuesta generada no sea un alucinación.

#### Ejemplo de alucinación para el primer prompt:
```text
La magnitud del terremoto fue de 7.5 en la escala de Richter y resultaron heridas alrededor de 500 personas. 
```

### Consejos para  evitar alucinaciones 📝🚫

Para asegurar que la IA entienda tu solicitud, deberías:
1. **Ser Específico**: Indica claramente lo que necesitas.
2. **Proporcionar Información de Fondo**: Incluye cualquier detalle relevante que pueda ayudar a la IA a entender el contexto, recuerda usar delimitadores apropiadamente.
3. **Usar Ejemplos**: Si es posible, proporciona ejemplos para ilustrar tu punto.
4. **Verificar la Información**: Siempre verifica las respuestas de la IA con fuentes confiables.
5. **Pídele a la IA** que te indique si **no** tiene suficiente información para responder tu pregunta.