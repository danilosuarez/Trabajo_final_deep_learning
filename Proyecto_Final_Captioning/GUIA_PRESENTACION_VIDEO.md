# Guia de presentacion y video final

## Objetivo del proyecto
Construir un modelo de deep learning capaz de generar descripciones automaticas de imagenes a partir del dataset Flickr8k, combinando un encoder visual basado en una CNN preentrenada y un decoder secuencial tipo LSTM.

## Pregunta de interes
Es posible generar descripciones textuales utiles y semanticamente consistentes para imagenes usando una arquitectura Encoder-Decoder entrenada con Flickr8k y calibrada con tecnicas vistas en el curso.

## Opcion del curso
Opcion 3: modelo para comentar automaticamente imagenes.

## Mensaje central del proyecto
El proyecto integra tres componentes del curso:
1. CNN y transfer learning para extraer informacion visual.
2. Modelos recurrentes GRU/LSTM para generar lenguaje natural.
3. Arquitectura Encoder-Decoder con decodificacion greedy y beam search para producir captions.

## Estructura recomendada del video (maximo 12 minutos)
### Slide 1. Portada y opcion elegida
- Titulo del proyecto.
- Nombres del grupo.
- Opcion 3 claramente visible.
- Frase breve del problema.
- Tiempo sugerido: 30 a 40 segundos.

### Slide 2. Problema y utilidad
- Describir por que el captioning automatico es util.
- Ejemplos de aplicaciones: accesibilidad, indexacion, busqueda de imagenes, apoyo a sistemas multimedia.
- Formular la pregunta de interes.
- Tiempo sugerido: 50 segundos.

### Slide 3. Dataset y contexto
- Dataset: Flickr8k.
- 8091 imagenes.
- 40455 captions.
- Cada imagen tiene 5 captions.
- Explicar que es un problema multimodal: imagen como entrada, texto como salida.
- Tiempo sugerido: 50 segundos.

### Slide 4. Exploracion de datos
- Mostrar ejemplos de imagenes con captions.
- Mostrar estadisticas principales del notebook 01:
  - 5663 imagenes train
  - 1213 imagenes val
  - 1215 imagenes test
  - vocabulario de 7251 palabras
  - longitud maxima de caption 38 tokens
- Explicar por que el split se hizo por imagen para evitar leakage.
- Tiempo sugerido: 1 minuto.

### Slide 5. Preparacion de datos
- Limpieza de captions.
- Minusculas, remocion de simbolos irrelevantes, normalizacion de espacios.
- Inclusión de tokens `startseq` y `endseq`.
- Tokenizacion y padding.
- Extraccion de features visuales con MobileNetV2.
- Resaltar que se guardaron artefactos reutilizables.
- Tiempo sugerido: 1 minuto.

### Slide 6. Seleccion del modelo
- Justificar por que no se uso solo una CNN ni solo una RNN.
- Explicar arquitectura propuesta:
  - Encoder: MobileNetV2 preentrenada en ImageNet.
  - Decoder: Embedding + LSTM/GRU.
  - Salida: palabra siguiente con softmax.
- Argumentar con relacion al contenido del curso.
- Tiempo sugerido: 1 minuto.

### Slide 7. Arquitectura
- Mostrar diagrama simple:
  - Imagen -> MobileNetV2 -> vector de features.
  - Caption parcial -> Embedding -> LSTM.
  - Fusion -> Dense -> siguiente palabra.
- Aclarar que el caption se genera palabra por palabra.
- Tiempo sugerido: 50 segundos.

### Slide 8. Baseline
- Modelo baseline: MobileNetV2 + GRU.
- Resultados del baseline:
  - BLEU-1 = 0.486
  - BLEU-2 = 0.3279
- Mostrar ejemplos cualitativos del notebook 02.
- Interpretacion: el modelo aprende semantica global, pero falla en detalles finos.
- Tiempo sugerido: 1 minuto.

### Slide 9. Calibracion inicial
- Comparar candidatos del notebook 03:
  - gru_128
  - gru_256
  - lstm_256
- Resultados:
  - lstm_256: val_loss 3.3898, BLEU-1 0.6130, BLEU-2 0.4244
  - gru_128: val_loss 3.4465, BLEU-2 0.4052
  - gru_256: val_loss 3.4735, BLEU-2 0.4081
- Concluir que `lstm_256` fue el mejor decoder.
- Mostrar grafica `calibration_validation_curves.png`.
- Tiempo sugerido: 1 minuto 20 segundos.

### Slide 10. Calibracion fina
- Explicar que se hizo una calibracion fina alrededor del mejor candidato:
  - lstm_256_base
  - lstm_256_lowlr
  - lstm_256_lowdrop
  - lstm_384_lowlr
- Hallazgo clave:
  - algunas configuraciones mejoraron ligeramente `val_loss`,
  - pero no mejoraron `BLEU` respecto a `lstm_256` del notebook 03.
- Concluir que se mantuvo `lstm_256` como mejor balance.
- Mostrar `fine_calibration_validation_curves.png` solo si ayuda; no dedicarle demasiado tiempo.
- Tiempo sugerido: 1 minuto.

### Slide 11. Beam Search
- Explicar la diferencia entre greedy y beam search.
- Mostrar resultados:
  - greedy: BLEU-2 0.4244, 0.3683 s/imagen
  - beam_3: BLEU-2 0.4354, 1.1349 s/imagen
  - beam_5: BLEU-2 0.4495, 1.8327 s/imagen
- Decidir y justificar:
  - si priorizan balance calidad-tiempo, usar beam_3.
  - si priorizan maximo BLEU, mencionar beam_5 como mejor numericamente.
- Tiempo sugerido: 1 minuto.

### Slide 12. Resultados cualitativos
- Mostrar ejemplos de captions predichos.
- Explicar aciertos:
  - objetos comunes,
  - contexto global,
  - acciones frecuentes.
- Explicar errores:
  - alucinacion de personas u objetos,
  - captions genericos,
  - conteo y detalle fino.
- Tiempo sugerido: 1 minuto.

### Slide 13. Relevancia, limitaciones y cierre
- Relevancia:
  - el modelo funciona y genera captions utiles.
  - demuestra la utilidad de combinar vision y lenguaje.
- Limitaciones:
  - dataset pequeno,
  - captions de referencia variables,
  - errores en escenas ambiguas,
  - encoder fijo sin atencion.
- Trabajo futuro:
  - attention,
  - mejor encoder,
  - beam search optimizado,
  - mayor cantidad de datos.
- Tiempo sugerido: 1 minuto.

## Resultado final recomendado para declarar
### Modelo final entrenado
- `MobileNetV2 + LSTM(256)`
- Mejor resultado de calibracion inicial.

### Estrategia final de inferencia
- Recomendada para equilibrio: `beam_3`
- Mejor numericamente: `beam_5`

## Resultados clave que deben aparecer textualmente
- Dataset: 8091 imagenes, 40455 captions.
- Split por imagen:
  - train 5663
  - val 1213
  - test 1215
- Vocabulario: 7251.
- Max length: 38.
- Baseline GRU:
  - BLEU-1 = 0.486
  - BLEU-2 = 0.3279
- Mejor decoder entrenado:
  - `lstm_256`
  - val_loss = 3.3898
  - val_accuracy = 0.3687
  - BLEU-1 = 0.6130
  - BLEU-2 = 0.4244
  - tiempo entrenamiento = 9.98 min
- Inferencia:
  - greedy: BLEU-2 = 0.4244
  - beam_3: BLEU-2 = 0.4354
  - beam_5: BLEU-2 = 0.4495

## Archivos visuales recomendados para insertar en la presentacion
- [calibration_validation_curves.png](/Users/danilosuarezvargas/Documents/Maestria%20Universidad%20andes/Deep%20learning/Proyecto_Final_Captioning/outputs/predictions/calibration_validation_curves.png)
- [calibration_qualitative_examples.png](/Users/danilosuarezvargas/Documents/Maestria%20Universidad%20andes/Deep%20learning/Proyecto_Final_Captioning/outputs/predictions/calibration_qualitative_examples.png)
- [fine_calibration_validation_curves.png](/Users/danilosuarezvargas/Documents/Maestria%20Universidad%20andes/Deep%20learning/Proyecto_Final_Captioning/outputs/predictions/fine_calibration_validation_curves.png)
- [fine_calibration_qualitative_examples.png](/Users/danilosuarezvargas/Documents/Maestria%20Universidad%20andes/Deep%20learning/Proyecto_Final_Captioning/outputs/predictions/fine_calibration_qualitative_examples.png)
- [beam_search_qualitative_examples.png](/Users/danilosuarezvargas/Documents/Maestria%20Universidad%20andes/Deep%20learning/Proyecto_Final_Captioning/outputs/predictions/beam_search_qualitative_examples.png)

## Reparto sugerido entre dos integrantes
### Integrante 1
- problema
- datos
- preparacion
- seleccion del modelo
- arquitectura

### Integrante 2
- baseline
- calibracion
- beam search
- resultados
- limitaciones y cierre

## Mensajes que no deben faltar
- La opcion elegida es la 3.
- La comparacion de modelos se hizo con validacion y criterio explicito.
- La solucion no es perfecta, pero si util y medible.
- El proyecto muestra una aplicacion real de deep learning multimodal.
