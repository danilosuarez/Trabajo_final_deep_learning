# Mapa del Curso Aplicado al Proyecto Final

## Objetivo de esta guia
Consolidar que partes del curso si se aplican al proyecto de `image captioning`, que partes son apoyo metodologico y que partes no conviene meter en la primera version.

El proyecto escogido es:
- `Opcion 3: Modelo automatico para comentar imagenes`

La arquitectura base del proyecto es:
- `Encoder visual`: `CNN` preentrenada
- `Decoder de lenguaje`: `Embedding + GRU/LSTM`
- `Inferencia`: generacion palabra a palabra

---

## Vision general: que aporta cada semana

| Semana | Aporte al proyecto | Nivel de uso |
| --- | --- | --- |
| Semana 2 | Base operativa del entorno y trabajo en repositorio | Bajo |
| Semana 3 | Fundamentos de entrenamiento: activaciones, Adam, BatchNorm | Medio |
| Semana 4 | Calibracion, regularizacion, early stopping y dropout | Alto |
| Semana 5 | Fundamentos de CNN y data augmentation | Alto |
| Semana 6 | Arquitecturas CNN y transfer learning | Muy alto |
| Semana 7 | RNN, LSTM, GRU, embeddings y NLP | Muy alto |
| Semana 8 | Encoder-Decoder, atencion y modelos generativos avanzados | Alto, pero selectivo |

---

## Semana 2

### Que aporta
No parece ser una semana directamente enfocada al modelado del proyecto, pero si deja la base practica para:
- trabajar en ambiente reproducible,
- estructurar repositorio,
- organizar notebooks y entregables.

### Como usarla en el proyecto
- mantener una estructura ordenada del repo,
- separar datos, modelos, notebooks y outputs,
- asegurar que el equipo pueda correr el flujo completo.

### Nivel de importancia
`Bajo` para el modelo, `alto` para la ejecucion ordenada del proyecto.

---

## Semana 3

### Que aporta
Por los modulos disponibles en la carpeta del curso, aqui se cubrieron temas base de entrenamiento:
- funciones de activacion,
- `Adam` y `RMSProp`,
- `Batch Normalization`,
- redes neuronales con Keras.

### Como se usa en este proyecto
- elegir el optimizador del decoder,
- justificar por que `Adam` es una buena primera opcion,
- entender estabilidad de entrenamiento,
- saber cuando una arquitectura necesita normalizacion adicional.

### Que si usaremos
- `Adam` como baseline del decoder,
- Keras/TensorFlow como framework central.

### Que no hace falta forzar
- `BatchNorm` dentro del baseline del decoder si no hay evidencia de que mejora.

---

## Semana 4

### Que aporta
Esta semana es directamente util para la rubrica en dos frentes:
- calibracion de hiperparametros,
- control de overfitting.

Segun los resúmenes en:
- [resumen_calibracion_hiperparametros.md](/Users/danilosuarezvargas/Documents/Maestria%20Universidad%20andes/Deep%20learning/Semana%204/resumen_calibracion_hiperparametros.md)
- [resumen_regularizacion_early_stopping_dropout.md](/Users/danilosuarezvargas/Documents/Maestria%20Universidad%20andes/Deep%20learning/Semana%204/resumen_regularizacion_early_stopping_dropout.md)
- [resumen_redes_neuronales_keras.md](/Users/danilosuarezvargas/Documents/Maestria%20Universidad%20andes/Deep%20learning/Semana%204/resumen_redes_neuronales_keras.md)

### Como se usa en este proyecto
- definir el plan de calibracion del baseline,
- comparar `GRU` vs `LSTM`,
- comparar dimensiones de embedding,
- usar `early stopping`,
- considerar `dropout` en el decoder,
- seleccionar el mejor modelo con validacion y no solo con train.

### Que si usaremos
- `validation set`
- `early stopping`
- comparacion sistematica de hiperparametros
- tablas de resultados

### Mensaje para el video
La semana 4 respalda toda la parte metodologica de:
- seleccion del modelo,
- estrategia de estimacion,
- y calibracion.

---

## Semana 5

### Que aporta
Da el fundamento de por que una `CNN` es la opcion correcta para el encoder visual.

Apoya especialmente con:
- introduccion a convolucion,
- pooling,
- arquitectura tipica de una CNN,
- `data augmentation`.

Referencias:
- [resumen_introduccion_redes_convolucionales.md](/Users/danilosuarezvargas/Documents/Maestria%20Universidad%20andes/Deep%20learning/Semana%205/resumen_introduccion_redes_convolucionales.md)
- [resumen_pooling_fully_connected_arquitecturas_cnn.md](/Users/danilosuarezvargas/Documents/Maestria%20Universidad%20andes/Deep%20learning/Semana%205/resumen_pooling_fully_connected_arquitecturas_cnn.md)
- [resumen_data_augmentation.md](/Users/danilosuarezvargas/Documents/Maestria%20Universidad%20andes/Deep%20learning/Semana%205/resumen_data_augmentation.md)

### Como se usa en este proyecto
- justificar que la imagen tiene estructura espacial,
- justificar que un `MLP` no es la herramienta correcta para la parte visual,
- explicar por que primero se extraen patrones visuales y luego se pasa a una etapa secuencial.

### Que si usaremos
- encoder visual basado en CNN,
- posiblemente `data augmentation` moderado en train si el tiempo lo permite.

### Que no conviene exagerar
- augmentation agresivo sin validar si empeora captions.

---

## Semana 6

### Que aporta
Es probablemente la semana mas importante para el `encoder` del proyecto.

Referencias:
- [resumen_video_2_otras_arquitecturas_famosas_y_transfer_learning.md](/Users/danilosuarezvargas/Documents/Maestria%20Universidad%20andes/Deep%20learning/Semana%206/resumen_video_2_otras_arquitecturas_famosas_y_transfer_learning.md)
- [resumen_lectura_hands_on_ml_cap14_cnn_architectures.md](/Users/danilosuarezvargas/Documents/Maestria%20Universidad%20andes/Deep%20learning/Semana%206/resumen_lectura_hands_on_ml_cap14_cnn_architectures.md)

### Como se usa en este proyecto
- elegir `MobileNetV2`, `ResNet50` o `VGG16` preentrenada,
- congelar la base visual,
- usarla como extractor de caracteristicas,
- evitar entrenar una CNN profunda desde cero con `Flickr8k`.

### Que si usaremos
- `transfer learning`
- encoder congelado en la primera version
- posibilidad de `fine-tuning` solo si el baseline ya funciona bien

### Mensaje para el video
La semana 6 es la justificacion tecnica del `encoder` visual:
- el modelo no “entiende” imagenes desde cero,
- reutiliza una red que ya aprendio patrones generales en `ImageNet`.

---

## Semana 7

### Que aporta
Es la base completa del `decoder` secuencial.

Referencias:
- [resumen_video_1_introduccion_rnn_datos_secuenciales.md](/Users/danilosuarezvargas/Documents/Maestria%20Universidad%20andes/Deep%20learning/Semana7/resumen_video_1_introduccion_rnn_datos_secuenciales.md)
- [resumen_video_3_lstm_gru_memoria_larga_y_gradiente.md](/Users/danilosuarezvargas/Documents/Maestria%20Universidad%20andes/Deep%20learning/Semana7/resumen_video_3_lstm_gru_memoria_larga_y_gradiente.md)
- [resumen_lectura_hands_on_ml_cap15_secciones_1_4.md](/Users/danilosuarezvargas/Documents/Maestria%20Universidad%20andes/Deep%20learning/Semana7/resumen_lectura_hands_on_ml_cap15_secciones_1_4.md)

### Como se usa en este proyecto
- los captions son secuencias, no etiquetas planas,
- el decoder necesita memoria temporal,
- `GRU/LSTM` son mejores que una `RNN` basica,
- el entrenamiento usa `BPTT`,
- la entrada al decoder se maneja como tensor secuencial.

### Que si usaremos
- `Tokenizer`
- `Embedding`
- `GRU` o `LSTM`
- generacion de texto palabra a palabra

### Decision recomendada
- baseline con `GRU`
- comparacion posterior contra `LSTM`

### Mensaje para el video
La semana 7 justifica por que la salida del proyecto no se modela como clasificacion simple, sino como una secuencia generada paso a paso.

---

## Semana 8

### Que aporta
Introduce la arquitectura `Encoder-Decoder`, que es la estructura conceptual exacta del proyecto.

Referencias principales:
- [resumen_video_1_encoder_decoder_seq2seq_asincronico.md](/Users/danilosuarezvargas/Documents/Maestria%20Universidad%20andes/Deep%20learning/Semana%208/resumen_video_1_encoder_decoder_seq2seq_asincronico.md)
- [resumen_lectura_hands_on_ml_cap16_seccion_4_attention_transformers.md](/Users/danilosuarezvargas/Documents/Maestria%20Universidad%20andes/Deep%20learning/Semana%208/resumen_lectura_hands_on_ml_cap16_seccion_4_attention_transformers.md)

### Como se usa en este proyecto
- la entrada es una imagen,
- la salida es una secuencia de palabras,
- no hay correspondencia uno a uno,
- por eso el problema es equivalente a un `Encoder-Decoder` asincronico.

### Que si usaremos
- concepto `Encoder-Decoder`
- `greedy decoding`
- posibilidad de `beam search` como mejora opcional

### Que no conviene meter en la primera version
- `attention` obligatoria
- `transformers`
- arquitectura muy compleja sin baseline funcional

### Por que
El curso los presenta como extensiones potentes, pero para el proyecto la prioridad debe ser:
1. baseline funcional,
2. calibracion defendible,
3. demo clara.

---

## Material de semana 8 que no es central para este proyecto

### Autoencoders, VAE y GANs
Referencia:
- [resumen_lectura_hands_on_ml_cap17_autoencoders_gans.md](/Users/danilosuarezvargas/Documents/Maestria%20Universidad%20andes/Deep%20learning/Semana%208/resumen_lectura_hands_on_ml_cap17_autoencoders_gans.md)

### Reinforcement Learning
Referencia:
- [resumen_lectura_hands_on_ml_cap18_reinforcement_learning.md](/Users/danilosuarezvargas/Documents/Maestria%20Universidad%20andes/Deep%20learning/Semana%208/resumen_lectura_hands_on_ml_cap18_reinforcement_learning.md)

### Decision practica
No se deben meter en este proyecto.

Razon:
- no responden directamente a la pregunta del proyecto,
- aumentan complejidad sin aportar a la rubrica,
- y desordenan la narrativa del video.

Se pueden mencionar solo como posibles lineas futuras si quieren enriquecer la conclusion.

---

## Mapa final: que parte del curso alimenta cada bloque del proyecto

| Bloque del proyecto | Temas del curso que lo respaldan |
| --- | --- |
| Definicion del problema | Semanas 5, 6, 7, 8 |
| EDA y entendimiento del dataset | Semana 4 por metodologia, Semana 8 por naturaleza seq-to-seq |
| Preparacion de datos | Semanas 5, 6 y 7 |
| Seleccion del modelo | Semanas 6, 7 y 8 |
| Calibracion | Semana 4 |
| Visualizacion de resultados | Semana 4 metodologicamente |
| Demo final | Semana 8 por inferencia autoregresiva |

---

## Que arquitectura tiene mas sentido segun el curso

### Baseline recomendado
- `Encoder`: `MobileNetV2` congelada
- `Decoder`: `Embedding + GRU`
- `Entrenamiento`: `Adam`, `early stopping`
- `Inferencia`: `greedy decoding`

### Segunda version razonable
- comparar `GRU` vs `LSTM`
- probar `dropout`
- comparar `MobileNetV2` vs `ResNet50` si el tiempo alcanza

### Mejoras opcionales
- `beam search`
- `fine-tuning` ligero del encoder visual

### Mejoras que no conviene meter salvo que todo ya funcione muy bien
- `attention`
- `transformers`
- `GANs`
- `RL`

---

## Como decirlo en el video

Una forma simple y correcta de presentarlo es:

> El proyecto integra dos lineas del curso. De las semanas 5 y 6 tomamos la parte de vision computacional y transfer learning para construir el encoder visual. De las semanas 7 y 8 tomamos RNN, GRU/LSTM y Encoder-Decoder para generar la descripcion textual palabra a palabra. La calibracion y la regularizacion se apoyan en la metodologia trabajada en semana 4.

---

## Conclusion ejecutiva

Con lo visto en el curso, si es totalmente viable construir este proyecto sin salir del marco tematico de la clase.

La ruta correcta es:
1. `CNN preentrenada` para imagen,
2. `GRU/LSTM` para texto,
3. `Encoder-Decoder` para unir ambas partes,
4. calibracion simple y defendible,
5. demo final con captions generados sobre imagenes nuevas.
