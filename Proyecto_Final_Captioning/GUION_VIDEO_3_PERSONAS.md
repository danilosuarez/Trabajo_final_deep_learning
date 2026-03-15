# Guion del video final para 3 personas

Duracion objetivo: entre 10:30 y 11:30 minutos.
Margen de seguridad: no acercarse a 12:00.

## Distribucion general
- Persona 1: Slides 1 a 4
- Persona 2: Slides 5 a 9
- Persona 3: Slides 10 a 14

Tiempo sugerido por persona:
- Persona 1: 3:20
- Persona 2: 3:40
- Persona 3: 3:40

---

## Slide 1. Portada
### Persona 1
**Tiempo sugerido: 0:30**

"Buenas tardes. Nuestro proyecto final corresponde a la opcion 3 del curso: comentar imagenes automaticamente. Desarrollamos un sistema de image captioning capaz de recibir una imagen y generar una descripcion textual, combinando un encoder visual basado en MobileNetV2 con un decoder secuencial tipo LSTM. El trabajo se realizo sobre el dataset Flickr8k y se estructuro siguiendo una metodologia completa de analitica y modelado."

---

## Slide 2. Problema y pregunta de interes
### Persona 1
**Tiempo sugerido: 0:50**

"El problema que abordamos consiste en generar descripciones automaticas de imagenes de forma coherente y util. La pregunta de interes fue si una arquitectura Encoder-Decoder podia aprender una representacion visual suficientemente informativa para producir captions semanticamente consistentes. Este problema tiene aplicaciones directas en accesibilidad para usuarios con discapacidad visual, indexacion semantica de imagenes y generacion automatica de metadatos y alt-text."

---

## Slide 3. Dataset
### Persona 1
**Tiempo sugerido: 0:45**

"Trabajamos con Flickr8k, un benchmark clasico para image captioning. El dataset contiene 8091 imagenes y 40455 captions, es decir, cinco descripciones por imagen. Luego de la limpieza textual obtuvimos un vocabulario de 7251 palabras y una longitud maxima de 38 tokens por caption. Es un dataset adecuado para este proyecto porque permite entrenar y evaluar un modelo multimodal en un entorno academico con costo computacional razonable."

---

## Slide 4. Exploracion de datos
### Persona 1
**Tiempo sugerido: 1:15**

"En la etapa de exploracion verificamos tanto la estructura del conjunto visual como la del corpus textual. Un punto metodologicamente importante es que la particion se hizo por imagen, no por caption, para evitar fuga de informacion entre entrenamiento, validacion y prueba. El split final fue de 5663 imagenes para entrenamiento, 1213 para validacion y 1215 para test. Tambien analizamos la distribucion de longitud de los captions y observamos que la mayoria se concentra en longitudes intermedias, lo que justifico un padding maximo de 38 tokens. Ademas, al revisar ejemplos individuales con sus cinco captions, vimos la variabilidad natural del lenguaje: una misma imagen puede describirse de varias maneras validas. Eso es importante porque luego afecta la evaluacion textual."

---

## Slide 5. Preparacion de datos
### Persona 2
**Tiempo sugerido: 1:00**

"En la preparacion de datos limpiamos los captions convirtiendo todo a minusculas, eliminando caracteres irrelevantes y normalizando espacios. Luego añadimos los tokens startseq y endseq para marcar el inicio y el final de la secuencia. Despues tokenizamos el texto y aplicamos padding para que todas las entradas tuvieran longitud uniforme. En paralelo, para la parte visual, usamos MobileNetV2 preentrenada como extractor de caracteristicas. De esta red obtuvimos un vector fijo por imagen, que luego se combina con la secuencia parcial del caption para formular el problema como prediccion de la siguiente palabra."

---

## Slide 6. Seleccion del modelo
### Persona 2
**Tiempo sugerido: 0:50**

"La seleccion del modelo responde a la naturaleza del problema. Como la entrada es una imagen y la salida es una secuencia de texto, necesitamos una arquitectura que combine representacion visual y generacion secuencial. Por eso usamos un enfoque Encoder-Decoder. El encoder visual resume la imagen en un espacio latente compacto, mientras que el decoder recurrente aprovecha el contexto acumulado para producir una descripcion palabra por palabra. Esta seleccion es coherente con enfoques estandar de modelado secuencial y transferencia de aprendizaje."

---

## Slide 7. Arquitectura propuesta
### Persona 2
**Tiempo sugerido: 0:55**

"La arquitectura final tiene dos ramas. La rama visual toma la imagen, la pasa por MobileNetV2 y obtiene un vector de 1280 dimensiones. Ese vector se proyecta a un espacio comun mediante una capa densa. La rama textual recibe el caption parcial, lo transforma en embeddings y lo procesa con una LSTM de 256 unidades. Luego ambas ramas se fusionan y el modelo predice la siguiente palabra con una capa softmax sobre las 7251 palabras del vocabulario. En otras palabras, el caption no se genera de una sola vez, sino de forma autoregresiva, condicionando cada prediccion a la informacion visual y a las palabras ya generadas."

---

## Slide 8. Baseline inicial
### Persona 2
**Tiempo sugerido: 0:40**

"Antes de adoptar el decoder final, construimos un baseline con la misma estructura general pero usando GRU en lugar de LSTM. Este baseline obtuvo un BLEU-1 de 0.486 y un BLEU-2 de 0.3279. Ya era capaz de capturar contexto global y algunos objetos prominentes, pero sus descripciones tendian a ser mas genericas y menos precisas en escenas ambiguas. Esto nos sirvio como punto de referencia para justificar la calibracion posterior."

---

## Slide 9. Calibracion inicial
### Persona 2
**Tiempo sugerido: 1:15**

"En la calibracion inicial mantuvimos fijo el encoder y todo el pipeline de datos, y comparamos tres configuraciones del decoder: gru_128, gru_256 y lstm_256. El mejor resultado lo obtuvo lstm_256, con una val_loss de 3.3898, val_accuracy de 0.3687, BLEU-1 de 0.6130 y BLEU-2 de 0.4244. Frente a las variantes GRU, la LSTM mostro una mejor capacidad para sostener coherencia secuencial y mejorar el solapamiento textual con las referencias. Por eso seleccionamos esta configuracion como el mejor modelo entrenado y como base para la siguiente etapa."

---

## Slide 10. Calibracion fina
### Persona 3
**Tiempo sugerido: 1:00**

"Una vez identificado el mejor decoder, realizamos una calibracion fina variando tres hiperparametros cercanos: la tasa de aprendizaje, el dropout y el numero de unidades LSTM. El objetivo era verificar si podiamos mejorar la generalizacion sin alterar la estructura global del modelo. Observamos que algunas variantes redujeron ligeramente la perdida de validacion, pero no mejoraron la calidad textual medida con BLEU respecto al lstm_256 elegido en la calibracion inicial. Por esa razon decidimos mantener el lstm_256 original como mejor modelo entrenado, priorizando consistencia entre desempeno y calidad del caption final."

---

## Slide 11. Comparacion de estrategias de inferencia
### Persona 3
**Tiempo sugerido: 1:05**

"Despues evaluamos distintas estrategias de decodificacion sin cambiar los pesos del modelo. La inferencia greedy selecciona la palabra mas probable en cada paso, mientras que beam search conserva varias secuencias candidatas y elige la mejor frase acumulada. Los resultados mostraron que beam search mejora consistentemente los puntajes BLEU. Greedy obtuvo BLEU-2 de 0.4244, beam-3 subio a 0.4354 y beam-5 a 0.4495. Sin embargo, esa mejora tiene un costo en tiempo de inferencia. Por eso, aunque beam-5 fue el mejor numericamente, consideramos que beam-3 ofrece el mejor balance entre calidad y eficiencia."

---

## Slide 12. Resultados cualitativos
### Persona 3
**Tiempo sugerido: 1:00**

"En los resultados cualitativos observamos que el modelo final captura bastante bien el contexto general de las escenas, reconoce objetos frecuentes y produce captions gramaticalmente plausibles. Sin embargo, tambien encontramos limitaciones claras. En algunas imagenes complejas el modelo menciona personas u objetos que no son realmente el foco principal de la escena, o genera descripciones demasiado genericas. Esto ocurre porque el caption final depende tanto de la representacion visual como de patrones estadisticos aprendidos del corpus textual, de modo que a veces privilegia una descripcion probable sobre una descripcion exacta."

---

## Slide 13. Relevancia, limitaciones y trabajo futuro
### Persona 3
**Tiempo sugerido: 0:50**

"A pesar de esas limitaciones, la solucion es relevante porque demuestra que es posible construir un sistema funcional de image captioning con una arquitectura accesible y con una metodologia completamente reproducible. Entre las limitaciones destacamos el tamaño relativamente pequeño del dataset, la ausencia de mecanismos de atencion visual y la dificultad para modelar detalle fino. Como trabajo futuro proponemos incorporar atencion, usar encoders mas potentes y ampliar la evaluacion con datasets y metricas adicionales."

---

## Slide 14. Conclusiones
### Persona 3
**Tiempo sugerido: 0:35**

"En conclusion, el mejor modelo entrenado fue MobileNetV2 con LSTM de 256 unidades, y la mejor estrategia de inferencia recomendada fue beam search con k igual a 3 por su equilibrio entre calidad y costo computacional. El proyecto cumplio la opcion 3 del curso y cubrio todos los pasos de la rubrica: formulacion del problema, exploracion y preparacion de datos, seleccion y calibracion del modelo, visualizacion de resultados y analisis critico de la solucion. Muchas gracias."

---

## Version resumida por persona

### Persona 1
- Slide 1: presentacion general del proyecto.
- Slide 2: problema, pregunta de interes y utilidad.
- Slide 3: dataset.
- Slide 4: exploracion y split por imagen.

### Persona 2
- Slide 5: preparacion de datos.
- Slide 6: seleccion del modelo.
- Slide 7: arquitectura.
- Slide 8: baseline.
- Slide 9: calibracion inicial.

### Persona 3
- Slide 10: calibracion fina.
- Slide 11: beam search.
- Slide 12: resultados cualitativos.
- Slide 13: relevancia y limitaciones.
- Slide 14: conclusiones.

---

## Recomendaciones para no pasar de 12 minutos
1. No leer textualmente cada bullet de la diapositiva.
2. En slides con tablas, mencionar solo el hallazgo central.
3. En slides con imagenes, explicar una sola idea fuerte.
4. Evitar repetir cifras que ya estan visibles en pantalla si no agregan interpretacion.
5. Ensayar una vez completa con cronometro; el objetivo real debe ser 11 minutos.
