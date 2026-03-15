# Revision de la presentacion de Gamma y guion sugerido

## Diagnostico general
La presentacion generada por Gamma tiene una **estructura buena y alineada con la rubrica**. Cubre:
- problema,
- datos,
- preparacion,
- seleccion del modelo,
- calibracion,
- resultados,
- relevancia y limitaciones.

Eso ya esta bien.

Lo que **si debe corregirse antes de grabar** es esto:
1. Hay varios textos duplicados o cortados por el export de Gamma.
2. Hay placeholders de imagen que todavia deben reemplazarse por figuras reales.
3. La diapositiva de calibracion fina **no coincide con los resultados reales de los notebooks**.
4. La presentacion debe mencionar con claridad que:
   - el **mejor modelo entrenado** fue `MobileNetV2 + LSTM(256)` del notebook 03,
   - la **mejor inferencia por balance calidad-tiempo** fue `beam_3`,
   - `beam_5` fue mejor numericamente, pero mas costoso.

## Veredicto
- **Si sirve como base final**.
- **No la grabaria todavia sin corregir 3 o 4 slides**.

---

## Revision slide por slide

### Slide 1. Portada
**Estado**: bueno, pero con ruido visual.

**Problemas a corregir**:
- aparece duplicado `Learning`.
- hay repeticion en el texto del resumen del problema.
- falta reemplazar `[Nombres del grupo]`.

**Como deberia quedar**:
- titulo: `Generacion automatica de descripciones de imagenes`
- subtitulo: `Modelo Encoder-Decoder con MobileNetV2 y LSTM sobre Flickr8k`
- opcion 3 visible
- nombres reales del grupo
- resumen corto de una sola frase

**Frase recomendada**:
> En este proyecto abordamos la opcion 3 del curso, que consiste en comentar imagenes automaticamente mediante un modelo de deep learning que combina vision por computador y procesamiento de lenguaje natural.

---

### Slide 2. Problema y pregunta de interes
**Estado**: bien.

**Ajustes menores**:
- no repetir palabras como `Encoder-Decoder` o `usando` en dos lineas.
- dejar una redaccion mas limpia.

**Version oral sugerida**:
> El problema que abordamos es el de generar descripciones automaticas de imagenes. Nuestra pregunta de interes fue si es posible entrenar un modelo Encoder-Decoder que, a partir de una imagen, produzca una descripcion textual coherente y util. Este problema tiene aplicaciones directas en accesibilidad, indexacion y generacion automatica de metadatos.

---

### Slide 3. Dataset Flickr8k
**Estado**: bien.

**Ajustes**:
- esta slide esta correcta en cifras.
- puedes mantenerla casi igual.

**Version oral sugerida**:
> Utilizamos Flickr8k, un dataset estandar en image captioning. Contiene 8091 imagenes y 40455 captions, es decir, cinco descripciones por imagen. Despues de la limpieza textual obtuvimos un vocabulario de 7251 palabras y una longitud maxima de 38 tokens por caption.

---

### Slide 4. Exploracion de datos
**Estado**: conceptualmente bien, pero debe tener la figura real.

**Que insertar**:
- histograma real o al menos una captura del notebook 01.
- una imagen con sus 5 captions si la tienen.

**Punto fuerte**:
- la nota de `split por imagen` esta muy bien y conviene mantenerla.

**Version oral sugerida**:
> En la exploracion verificamos la estructura del dataset y realizamos la particion por imagen, no por caption. Esto es importante porque evita fuga de informacion entre entrenamiento, validacion y prueba. El split final fue 70% entrenamiento, 15% validacion y 15% test, con 5663, 1213 y 1215 imagenes respectivamente.

---

### Slide 5. Preparacion de datos
**Estado**: bien, pero hay detalles de forma.

**Corregir**:
- `K eras` debe quedar `Keras`.
- simplificar un poco la infografia para que no se sature.

**Version oral sugerida**:
> En la preparacion de datos limpiamos los captions, convirtiendo todo a minusculas, eliminando caracteres irrelevantes y normalizando espacios. Luego agregamos los tokens `startseq` y `endseq`, tokenizamos con Keras y aplicamos padding a una longitud maxima de 38. En paralelo, usamos MobileNetV2 preentrenada para extraer un vector fijo de caracteristicas por imagen.

---

### Slide 6. Seleccion del modelo
**Estado**: muy buena.

**Mantener**.

**Version oral sugerida**:
> Seleccionamos una arquitectura Encoder-Decoder porque el problema es multimodal: la entrada es una imagen y la salida es una secuencia de texto. La CNN se encarga de representar la imagen, mientras que la LSTM modela la dependencia secuencial entre palabras para generar descripciones mas coherentes.

---

### Slide 7. Arquitectura propuesta
**Estado**: buena.

**Ajuste**:
- si puedes, agrega una linea final visible: `Imagen -> CNN -> vector de features -> decoder recurrente -> caption`.

**Version oral sugerida**:
> La arquitectura tiene dos ramas. La rama visual toma la imagen y la transforma en un vector de caracteristicas usando MobileNetV2. La rama textual recibe el caption parcial, lo convierte en embeddings y lo procesa con una LSTM de 256 unidades. Ambas ramas se fusionan y el modelo predice la siguiente palabra mediante una capa softmax.

---

### Slide 8. Baseline inicial
**Estado**: bien.

**Ajuste importante**:
- insertar la figura real del baseline.
- si no insertan la figura, la slide queda debil para la rubrica de visualizacion.

**Version oral sugerida**:
> Como punto de partida construimos un baseline con MobileNetV2 y GRU. Este modelo obtuvo BLEU-1 de 0.486 y BLEU-2 de 0.3279. El baseline ya capturaba semantica general de la escena, pero mostraba limitaciones en detalles finos y en escenas ambiguas, por lo que sirvio como umbral minimo de desempeno.

---

### Slide 9. Calibracion inicial
**Estado**: bien estructurada y util.

**Correccion recomendada**:
- si tienes espacio, agrega las `val_accuracy` de `gru_128` y `gru_256` para que no queden guiones.
- segun tus resultados:
  - `gru_128`: `val_accuracy = 0.3580`
  - `gru_256`: `val_accuracy = 0.3508`

**Version oral sugerida**:
> En la calibracion inicial mantuvimos fijo el encoder y comparamos tres decoders: `gru_128`, `gru_256` y `lstm_256`. El mejor resultado lo obtuvo `lstm_256`, con `val_loss = 3.3898`, `val_accuracy = 0.3687`, `BLEU-1 = 0.6130` y `BLEU-2 = 0.4244`. Esto nos indico que LSTM modelaba mejor las dependencias de largo plazo necesarias para generar lenguaje.

---

### Slide 10. Calibracion fina
**Estado**: esta es la slide que **si debes corregir**.

**Problema principal**:
Los valores mostrados en el PDF **no coinciden con los resultados reales del notebook 04**.

**Resultados reales**:
- `lstm_256_lowdrop`: `val_loss = 3.3624`, `val_accuracy = 0.3714`, `BLEU-1 = 0.4809`, `BLEU-2 = 0.3331`
- `lstm_256_lowlr`: `val_loss = 3.3635`, `val_accuracy = 0.3710`, `BLEU-1 = 0.5392`, `BLEU-2 = 0.3715`
- `lstm_384_lowlr`: `val_loss = 3.4355`, `val_accuracy = 0.3595`, `BLEU-1 = 0.5425`, `BLEU-2 = 0.3719`
- `lstm_256_base`: `val_loss = 3.4977`, `val_accuracy = 0.3650`, `BLEU-1 = 0.5357`, `BLEU-2 = 0.3638`

**Mensaje correcto de la slide**:
- algunas configuraciones mejoraron marginalmente `val_loss`,
- pero **ninguna mejoro el BLEU del `lstm_256` del notebook 03**, que tenia `BLEU-2 = 0.4244`,
- por eso se mantuvo el `lstm_256` de la calibracion inicial como mejor modelo entrenado.

**Version oral sugerida**:
> Luego realizamos una calibracion fina alrededor del mejor LSTM, variando learning rate, dropout y numero de unidades. Aunque algunas configuraciones redujeron ligeramente la perdida de validacion, ninguna supero al `lstm_256` inicial en calidad textual medida con BLEU. Por esa razon mantuvimos como modelo final entrenado el `lstm_256` del notebook de calibracion inicial.

---

### Slide 11. Beam Search
**Estado**: muy buena. Esta slide si agrega valor real.

**Mantener**.

**Version oral sugerida**:
> Finalmente, sin cambiar los pesos del modelo, comparamos distintas estrategias de inferencia. La decodificacion greedy escoge la palabra mas probable en cada paso, mientras que beam search conserva varias secuencias candidatas. Vimos que beam search mejora consistentemente los puntajes BLEU. `beam_5` fue el mejor numericamente, pero `beam_3` ofrecio el mejor balance entre calidad y tiempo de inferencia.

---

### Slide 12. Resultados cualitativos
**Estado**: bien, pero depende de insertar la grilla real.

**Que debes insertar**:
- [beam_search_qualitative_examples.png](/Users/danilosuarezvargas/Documents/Maestria Universidad andes/Deep learning/outputs/predictions/beam_search_qualitative_examples.png)

**Version oral sugerida**:
> A nivel cualitativo, el modelo identifica bien el contexto general, objetos prominentes y acciones frecuentes. Sin embargo, en escenas ambiguas puede generar descripciones genericas o incluso mencionar elementos que no estan presentes. Esto ocurre porque combina la informacion visual con patrones estadisticos aprendidos de los captions de entrenamiento.

---

### Slide 13. Relevancia, limitaciones y trabajo futuro
**Estado**: buena.

**Mantener**.

**Version oral sugerida**:
> La solucion es relevante porque demuestra que un modelo multimodal relativamente compacto puede generar captions utiles y medibles. Entre las limitaciones encontramos el tamano reducido del dataset, la ausencia de mecanismos de atencion y la tendencia a producir captions genericos en escenas complejas. Como trabajo futuro planteamos incorporar atencion, usar encoders mas potentes y evaluar sobre datasets mayores como MSCOCO.

---

### Slide 14. Conclusiones
**Estado**: buena, pero conviene limpiar formato.

**Corregir**:
- separar bien los bloques de texto para que no se peguen:
  - `Val Loss: 3.3898`
  - `BLEU-1: 0.6130`
  - `BLEU-2: 0.4244`
- escribir explicitamente:
  - `modelo final entrenado: MobileNetV2 + LSTM(256)`
  - `inferencia final recomendada: beam_3`

**Version oral sugerida**:
> En conclusion, logramos construir una solucion funcional de image captioning utilizando una arquitectura Encoder-Decoder con MobileNetV2 y LSTM. El mejor modelo entrenado fue `MobileNetV2 + LSTM(256)`, y la mejor estrategia practica de inferencia fue `beam_3`, que mejoro la calidad del caption frente a greedy con un costo computacional razonable. El proyecto cubrio todos los pasos de la rubrica y deja abierta una linea clara de mejora futura.

---

## Correcciones concretas antes de grabar

### Obligatorias
1. Reemplazar `[Nombres del grupo]`.
2. Corregir texto duplicado en slide 1.
3. Corregir `K eras` por `Keras`.
4. Corregir la slide de calibracion fina con los resultados reales.
5. Insertar las figuras reales en slides con placeholders.

### Muy recomendables
1. Aclarar en la ultima slide que el mejor modelo entrenado es `lstm_256` del notebook 03.
2. Aclarar que `beam_3` es la recomendacion final por trade-off.
3. Agregar la fuente del dataset y mencionar `ImageNet` como origen del preentrenamiento.

---

## Guion sugerido slide por slide

### Slide 1
"Buenas tardes. Nuestro proyecto final corresponde a la opcion 3 del curso: comentar imagenes automaticamente. Desarrollamos un sistema de image captioning basado en una arquitectura Encoder-Decoder con MobileNetV2 y LSTM, aplicado al dataset Flickr8k."

### Slide 2
"La pregunta de interes fue si es posible entrenar un modelo capaz de recibir una imagen y generar una descripcion textual coherente y util. Este problema tiene aplicaciones en accesibilidad, indexacion de imagenes y generacion automatica de metadatos."

### Slide 3
"Trabajamos con Flickr8k, un dataset estandar de image captioning. Contiene 8091 imagenes y 40455 captions, es decir, cinco descripciones por imagen. Tras la limpieza textual, obtuvimos un vocabulario de 7251 palabras y una longitud maxima de 38 tokens."

### Slide 4
"En la exploracion de datos analizamos la estructura del corpus y realizamos la particion por imagen para evitar fuga de informacion. El conjunto final quedo dividido en 5663 imagenes para entrenamiento, 1213 para validacion y 1215 para prueba."

### Slide 5
"En la preparacion de datos limpiamos los captions, los convertimos a minusculas, eliminamos caracteres irrelevantes y agregamos los tokens `startseq` y `endseq`. Luego tokenizamos, aplicamos padding y, en paralelo, extraimos caracteristicas visuales con MobileNetV2 preentrenada."

### Slide 6
"Seleccionamos una arquitectura Encoder-Decoder porque el problema requiere combinar vision por computador y procesamiento secuencial de lenguaje. La CNN resume la imagen en un vector de caracteristicas y la LSTM genera la descripcion palabra por palabra."

### Slide 7
"La arquitectura final tiene dos ramas. La rama visual usa MobileNetV2 y una proyeccion densa. La rama textual usa embeddings y una LSTM de 256 unidades. Ambas ramas se fusionan y el modelo predice la siguiente palabra mediante una capa softmax sobre el vocabulario."

### Slide 8
"Como baseline usamos MobileNetV2 con un decoder GRU. Este modelo obtuvo un BLEU-1 de 0.486 y un BLEU-2 de 0.3279. El baseline ya lograba capturar semantica general, pero presentaba limitaciones importantes en detalle fino y escenas ambiguas."

### Slide 9
"En la calibracion inicial comparamos tres decoders: `gru_128`, `gru_256` y `lstm_256`. El mejor fue `lstm_256`, que obtuvo la menor perdida de validacion y los mejores puntajes BLEU. Esto nos llevo a seleccionarlo como el mejor candidato entrenado."

### Slide 10
"Posteriormente realizamos una calibracion fina alrededor del mejor LSTM, variando learning rate, dropout y numero de unidades. Aunque algunas configuraciones redujeron marginalmente la perdida de validacion, ninguna supero al `lstm_256` inicial en calidad textual medida con BLEU. Por eso mantuvimos ese modelo como la mejor solucion entrenada."

### Slide 11
"Despues evaluamos estrategias de inferencia. La decodificacion greedy escoge la mejor palabra local, mientras que beam search mantiene varias secuencias candidatas. Beam search mejoro los puntajes BLEU. `beam_5` fue el mejor numericamente, pero `beam_3` ofrecio el mejor equilibrio entre calidad y tiempo de inferencia."

### Slide 12
"A nivel cualitativo, el modelo describe bien el contexto global, objetos prominentes y acciones frecuentes. Sin embargo, tambien observamos captions genericos y alucinaciones en escenas ambiguas. Esto sucede porque el modelo combina la informacion visual con patrones frecuentes aprendidos del lenguaje de entrenamiento."

### Slide 13
"La solucion es relevante porque demuestra que un modelo multimodal relativamente compacto puede generar captions utiles y medibles. Entre las limitaciones encontramos el tamano reducido del dataset, la ausencia de atencion y la dificultad para capturar detalle fino. Como trabajo futuro proponemos incorporar atencion y usar encoders mas potentes."

### Slide 14
"En conclusion, construimos una solucion funcional de image captioning que integra los principales conceptos del curso. El mejor modelo entrenado fue `MobileNetV2 + LSTM(256)` y la mejor estrategia final de inferencia por balance calidad-tiempo fue `beam_3`. Con esto cumplimos la opcion 3 del curso y cubrimos todos los pasos de la rubrica."

---

## Reparto sugerido entre dos personas

### Persona 1
- Slides 1 a 7
- problema
- datos
- preparacion
- seleccion del modelo
- arquitectura

### Persona 2
- Slides 8 a 14
- baseline
- calibracion
- beam search
- resultados
- relevancia, limitaciones y cierre

---

## Tiempo estimado
- Slides 1 a 3: 2 minutos
- Slides 4 a 7: 3 minutos
- Slides 8 a 11: 3.5 minutos
- Slides 12 a 14: 2.5 minutos
- Total estimado: 11 minutos
