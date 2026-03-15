# Prompt mejorado para Gamma AI

Copia y pega este prompt completo en Gamma. Luego inserta manualmente las figuras reales del proyecto en las diapositivas indicadas.

---

Quiero una presentacion academica, profesional, clara y visualmente limpia, en espanol, para un proyecto final universitario de Deep Learning. La presentacion sera usada en un video-presentacion de maximo 12 minutos, por lo que debe tener entre 12 y 14 diapositivas. El tono debe ser tecnico, riguroso y facil de exponer oralmente, evitando texto duplicado, frases repetidas o bloques demasiado largos.

La presentacion debe estar alineada con una rubrica academica que exige cubrir estos pasos metodologicos:
1. Descripcion del problema o formulacion de la pregunta de interes.
2. Exploracion de los datos para su entendimiento.
3. Preparacion de los datos para utilizarlos en modelos de deep learning.
4. Analisis sobre la seleccion del modelo apropiado y la estrategia de estimacion y calibracion.
5. Desarrollo y calibracion de modelos.
6. Visualizacion de resultados.
7. Implementacion y demostracion de la utilidad de los resultados.

## Tema del proyecto
"Generacion automatica de descripciones de imagenes mediante un modelo Encoder-Decoder con MobileNetV2 y LSTM"

## Opcion del curso
Debe quedar explicitamente visible desde la primera diapositiva que este proyecto corresponde a la **OPCION 3: comentar imagenes automaticamente**.

## Problema
El proyecto busca construir un sistema de image captioning que reciba una imagen como entrada y genere una descripcion textual automatica. La motivacion es combinar vision por computador y procesamiento de lenguaje natural en una sola solucion multimodal.

## Pregunta de interes
¿Es posible generar descripciones utiles y semanticamente consistentes para imagenes usando una arquitectura Encoder-Decoder basada en `MobileNetV2` y `LSTM`, calibrada con tecnicas vistas en el curso?

## Utilidad practica
- accesibilidad para personas con discapacidad visual,
- indexacion y busqueda semantica de imagenes,
- generacion automatica de alt-text y metadatos,
- apoyo a aplicaciones multimedia.

## Dataset
Se utilizo Flickr8k.
Datos reales del proyecto:
- 8091 imagenes
- 40455 captions
- 5 captions por imagen
- vocabulario final: 7251 palabras
- longitud maxima de caption: 38 tokens
- split por imagen para evitar leakage:
  - train: 5663 imagenes
  - validacion: 1213 imagenes
  - test: 1215 imagenes

## Preparacion de datos
Explicar que se realizo:
- limpieza de captions,
- conversion a minusculas,
- eliminacion de caracteres irrelevantes,
- normalizacion de espacios,
- adicion de `startseq` y `endseq`,
- tokenizacion con Keras,
- padding a 38 tokens,
- extraccion de features visuales con `MobileNetV2` preentrenada,
- construccion de pares supervisados del tipo: `[features de imagen, secuencia parcial] -> siguiente palabra`.

## Arquitectura del modelo
- Encoder: `MobileNetV2` preentrenada en `ImageNet`, usada como extractor de caracteristicas visuales.
- Decoder: `Embedding + LSTM`.
- Fase de entrenamiento: prediccion de la siguiente palabra.
- Tipo de arquitectura: `Encoder-Decoder`.
- Generacion final del caption: palabra por palabra.

## Baseline inicial
Se construyo un baseline con `MobileNetV2 + GRU`.
Resultados reales del baseline:
- BLEU-1 = 0.4860
- BLEU-2 = 0.3279
Interpretacion correcta:
- el baseline captura semantica global,
- pero falla en detalle fino y en escenas ambiguas,
- sirve como punto de referencia minimo para justificar modelos mas complejos.

## Calibracion inicial de modelos
Aqui es muy importante no mezclar resultados con otras etapas.
Se compararon tres decoders manteniendo fijo el encoder y el pipeline de datos:
- `gru_128`
- `gru_256`
- `lstm_256`

Resultados reales de esta calibracion inicial:
- `lstm_256`: val_loss = 3.3898, val_accuracy = 0.3687, BLEU-1 = 0.6130, BLEU-2 = 0.4244, training_time = 9.98 min
- `gru_128`: val_loss = 3.4465, val_accuracy = 0.3580, BLEU-1 = 0.5936, BLEU-2 = 0.4052, training_time = 9.88 min
- `gru_256`: val_loss = 3.4735, val_accuracy = 0.3508, BLEU-1 = 0.6026, BLEU-2 = 0.4081, training_time = 8.63 min

Conclusion correcta de esta slide:
- el mejor decoder entrenado fue `lstm_256`
- se selecciono por menor `val_loss` y mejores puntajes BLEU.

## Calibracion fina alrededor del mejor LSTM
Aqui debes ser muy riguroso y no mezclar el `lstm_256` del notebook 03 con los resultados del notebook 04.
La calibracion fina consistio en explorar hiperparametros cercanos al mejor modelo anterior:
- `lstm_256_base`
- `lstm_256_lowlr`
- `lstm_256_lowdrop`
- `lstm_384_lowlr`

Resultados reales de la calibracion fina:
- `lstm_256_base`: val_loss = 3.4977, val_accuracy = 0.3650, BLEU-1 = 0.5357, BLEU-2 = 0.3638
- `lstm_256_lowlr`: val_loss = 3.3635, val_accuracy = 0.3710, BLEU-1 = 0.5392, BLEU-2 = 0.3715
- `lstm_256_lowdrop`: val_loss = 3.3624, val_accuracy = 0.3714, BLEU-1 = 0.4809, BLEU-2 = 0.3331
- `lstm_384_lowlr`: val_loss = 3.4355, val_accuracy = 0.3595, BLEU-1 = 0.5425, BLEU-2 = 0.3719

Conclusion correcta de esta slide:
- algunas configuraciones mejoraron marginalmente `val_loss`,
- pero ninguna supero al `lstm_256` de la calibracion inicial en BLEU,
- por ello se mantuvo como **mejor modelo entrenado final** el `lstm_256` de la calibracion inicial.

## Inferencia: Greedy vs Beam Search
Esta parte debe quedar muy clara porque agrega valor metodologico sin reentrenar la red.
Explicar que:
- `greedy` selecciona la mejor palabra local en cada paso,
- `beam search` conserva varias secuencias candidatas y selecciona la mejor frase acumulada.

Resultados reales:
- greedy: BLEU-1 = 0.6130, BLEU-2 = 0.4244, sec_per_image = 0.3683
- beam_3: BLEU-1 = 0.6222, BLEU-2 = 0.4354, sec_per_image = 1.1349
- beam_5: BLEU-1 = 0.6306, BLEU-2 = 0.4495, sec_per_image = 1.8327

Decision que debe explicarse:
- mejor modelo entrenado: `MobileNetV2 + LSTM(256)`
- mejor inferencia numericamente: `beam_5`
- mejor inferencia recomendada por balance calidad-tiempo: `beam_3`

## Hallazgos cualitativos
La presentacion debe explicar que:
- el modelo reconoce bien el contexto general,
- detecta adecuadamente objetos prominentes y acciones frecuentes,
- puede generar descripciones plausibles pero no exactas,
- en escenas ambiguas tiende a producir captions genericos o a alucinar elementos,
- esto ocurre porque combina informacion visual con patrones frecuentes aprendidos de los captions de entrenamiento.

## Limitaciones
- dataset relativamente pequeno,
- captions de referencia variables,
- encoder fijo sin mecanismo de atencion,
- errores en detalle fino y conteo,
- captions genericos en escenas complejas.

## Trabajo futuro
- incorporar mecanismos de atencion,
- usar encoders mas potentes,
- ampliar el dataset,
- optimizar beam search,
- evaluar con metricas adicionales como METEOR o CIDEr.

## Requisitos estrictos de la presentacion
1. No repetir palabras o frases por errores de maquetacion.
2. No mezclar resultados de calibracion inicial con calibracion fina.
3. No mostrar el `lstm_256` de la calibracion inicial como si fuera una de las filas de calibracion fina.
4. Incluir bullets concretos, no parrafos largos.
5. Mantener un estilo academico, sobrio y tecnico.
6. Dejar espacios claros para insertar manualmente graficas e imagenes reales.
7. La presentacion debe ser apta para ser expuesta por al menos dos integrantes.

## Estructura exacta solicitada

### Slide 1. Portada
- Titulo del proyecto
- Subtitulo tecnico
- Opcion 3 visible
- Curso
- Nombres del grupo
- Una frase corta que resuma el problema

### Slide 2. Problema y pregunta de interes
- problema
- pregunta de interes
- utilidad practica

### Slide 3. Dataset
- Flickr8k
- numero de imagenes, captions, vocabulario, tokens maximos
- explicacion breve de por que es adecuado

### Slide 4. Exploracion de datos
- tabla del split train/val/test
- nota de que el split se hizo por imagen
- espacio para insertar histogramas y ejemplos

### Slide 5. Preparacion de datos
- limpieza textual
- tokenizacion y padding
- extraccion de features visuales
- construccion de pares de entrenamiento

### Slide 6. Seleccion del modelo
- justificar Encoder-Decoder
- justificar CNN
- justificar LSTM
- conectar con conceptos del curso

### Slide 7. Arquitectura propuesta
- diagrama simple del pipeline
- encoder visual
- decoder secuencial
- softmax sobre vocabulario

### Slide 8. Baseline inicial
- presentar `MobileNetV2 + GRU`
- mostrar BLEU del baseline
- una interpretacion breve
- espacio para ejemplos cualitativos

### Slide 9. Calibracion inicial
- tabla de `gru_128`, `gru_256`, `lstm_256`
- destacar que `lstm_256` fue el mejor
- espacio para graficas de validacion

### Slide 10. Calibracion fina
- tabla solo con las configuraciones del notebook 04:
  - `lstm_256_base`
  - `lstm_256_lowlr`
  - `lstm_256_lowdrop`
  - `lstm_384_lowlr`
- concluir correctamente que ninguna supero al `lstm_256` del notebook 03 en BLEU

### Slide 11. Comparacion de inferencia
- explicar greedy vs beam search
- mostrar tabla con `greedy`, `beam_3` y `beam_5`
- concluir que `beam_3` es la recomendacion final por trade-off

### Slide 12. Resultados cualitativos
- espacio para grilla de imagen + caption real + caption predicho
- bullets de fortalezas y errores observados

### Slide 13. Relevancia, limitaciones y trabajo futuro
- relevancia de la solucion
- limitaciones
- posibles mejoras futuras

### Slide 14. Conclusiones
- resumir el mejor modelo entrenado
- resumir la mejor estrategia de inferencia
- explicar que el proyecto cumplio todos los pasos de la rubrica

## Estilo visual deseado
- academico
- profesional
- fondo claro
- tipografia sobria
- sin estilo corporativo agresivo
- sin adornos innecesarios
- tablas legibles y faciles de exponer
- layout limpio, con jerarquia visual clara

## Indicacion final para Gamma
Genera la presentacion ya estructurada slide por slide, con titulos, subtitulos y bullets listos para exponer. No inventes resultados adicionales y no alteres las metricas proporcionadas. Mantén consistencia metodologica entre baseline, calibracion inicial, calibracion fina e inferencia final.
