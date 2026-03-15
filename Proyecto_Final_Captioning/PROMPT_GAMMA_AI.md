# Prompt para Gamma AI

Copia y pega este prompt en Gamma. Luego inserta manualmente las imagenes y graficas generadas en la carpeta `outputs/predictions`.

---

Crea una presentacion academica, profesional y clara, en espanol, para un proyecto final universitario de deep learning. La presentacion debe estar pensada para un video-presentacion de maximo 12 minutos, por lo que debe tener entre 12 y 14 diapositivas. El tono debe ser tecnico, riguroso y entendible, sin adornos innecesarios. Quiero una estructura alineada con una rubrica academica que evalua metodologia de analytics, seleccion de modelo, calibracion, visualizacion de resultados y relevancia de la solucion.

Tema del proyecto:
"Generacion automatica de descripciones de imagenes mediante un modelo Encoder-Decoder con MobileNetV2 y LSTM"

Objetivo del proyecto:
Construir un sistema de image captioning que reciba una imagen como entrada y genere una descripcion textual automatica, usando un encoder visual basado en una CNN preentrenada y un decoder secuencial tipo LSTM.

Opcion del proyecto:
Debe quedar explicito desde la primera diapositiva que corresponde a la OPCION 3 del curso: modelo para comentar automaticamente imagenes.

Contexto metodologico:
La presentacion debe cubrir obligatoriamente estos pasos:
1. Descripcion del problema o formulacion de la pregunta de interes.
2. Exploracion de los datos para su entendimiento.
3. Preparacion de los datos para utilizarlos en modelos de deep learning.
4. Analisis sobre la seleccion del modelo apropiado y la estrategia de estimacion y calibracion.
5. Desarrollo y calibracion de modelos.
6. Visualizacion de resultados.
7. Implementacion y demostracion de la utilidad de los resultados.

Datos del proyecto:
- Dataset usado: Flickr8k.
- Numero de imagenes: 8091.
- Numero de captions: 40455.
- Cada imagen tiene 5 captions.
- Split por imagen para evitar leakage:
  - train: 5663 imagenes
  - val: 1213 imagenes
  - test: 1215 imagenes
- Vocabulario final: 7251 palabras.
- Longitud maxima del caption: 38 tokens.

Preparacion de datos realizada:
- limpieza de captions,
- conversion a minusculas,
- eliminacion de caracteres irrelevantes,
- normalizacion de espacios,
- adicion de tokens `startseq` y `endseq`,
- tokenizacion,
- padding,
- extraccion de features visuales con `MobileNetV2` preentrenada.

Arquitectura del modelo:
- Encoder: `MobileNetV2` preentrenada en ImageNet, usada para convertir la imagen en un vector de caracteristicas.
- Decoder: `Embedding + LSTM`.
- Fusion: combinacion de rama visual y rama textual para predecir la siguiente palabra.
- Tipo de arquitectura: `Encoder-Decoder`.
- Generacion del caption: palabra por palabra.

Baseline inicial:
- Modelo baseline: `MobileNetV2 + GRU`.
- Resultados baseline:
  - BLEU-1 = 0.486
  - BLEU-2 = 0.3279
- Interpretacion: el baseline captura semantica general, pero falla en detalles finos y escenas ambiguas.

Calibracion inicial:
Se compararon tres candidatos manteniendo fijo el encoder y el pipeline de datos:
- `gru_128`
- `gru_256`
- `lstm_256`

Resultados de la calibracion inicial:
- `lstm_256`: val_loss = 3.3898, val_accuracy = 0.3687, BLEU-1 = 0.6130, BLEU-2 = 0.4244, training_time = 9.98 min
- `gru_128`: val_loss = 3.4465, BLEU-2 = 0.4052
- `gru_256`: val_loss = 3.4735, BLEU-2 = 0.4081

Conclusion de la calibracion inicial:
El mejor decoder fue `lstm_256`, ya que obtuvo la menor perdida de validacion y los mejores puntajes BLEU.

Calibracion fina:
Luego se hizo una calibracion fina alrededor del mejor LSTM, probando:
- `lstm_256_base`
- `lstm_256_lowlr`
- `lstm_256_lowdrop`
- `lstm_384_lowlr`

Hallazgo de calibracion fina:
Aunque algunas configuraciones redujeron ligeramente `val_loss`, ninguna supero claramente al `lstm_256` del paso anterior en calidad textual medida con BLEU. Por eso se mantuvo `lstm_256` como mejor modelo entrenado.

Estrategias de inferencia comparadas:
- `greedy`
- `beam_3`
- `beam_5`

Resultados de inferencia:
- greedy: BLEU-1 = 0.6130, BLEU-2 = 0.4244, sec_per_image = 0.3683
- beam_3: BLEU-1 = 0.6222, BLEU-2 = 0.4354, sec_per_image = 1.1349
- beam_5: BLEU-1 = 0.6306, BLEU-2 = 0.4495, sec_per_image = 1.8327

Decision final sugerida:
- Mejor modelo entrenado: `MobileNetV2 + LSTM(256)`
- Mejor estrategia de inferencia por equilibrio calidad-tiempo: `beam_3`
- Mejor estrategia numericamente: `beam_5`

Quiero que la presentacion tenga esta estructura de diapositivas:

1. Portada
- Titulo del proyecto
- Nombres del grupo
- Curso
- Opcion 3 claramente visible
- Subtitulo corto que resuma el problema

2. Problema y pregunta de interes
- Explicar que el problema es generar descripciones automaticas de imagenes
- Formular pregunta de interes
- Explicar utilidad practica: accesibilidad, indexacion, busqueda de imagenes, apoyo multimedia

3. Dataset y contexto
- Presentar Flickr8k
- Numero de imagenes y captions
- Naturaleza multimodal del problema
- Mencionar que cada imagen tiene varias descripciones de referencia

4. Exploracion de datos
- Resumir split train/val/test
- Vocabulario y longitud maxima
- Explicar por que el split se hizo por imagen para evitar fuga de informacion
- Dejar espacio para insertar imagenes de ejemplo

5. Preparacion de datos
- Listar pasos de limpieza y tokenizacion
- Explicar `startseq`, `endseq`, padding y tokenizador
- Explicar extraccion de features con MobileNetV2

6. Seleccion del modelo
- Justificar por que un enfoque Encoder-Decoder es adecuado
- Explicar que se combinan CNN y RNN/LSTM
- Relacionar con contenidos del curso

7. Arquitectura propuesta
- Mostrar diagrama simple del pipeline: imagen -> CNN -> vector -> decoder LSTM -> caption
- Explicar que se predice la siguiente palabra con softmax

8. Baseline inicial
- Presentar `MobileNetV2 + GRU`
- Reportar BLEU-1 y BLEU-2 del baseline
- Incluir una frase de interpretacion
- Dejar espacio para insertar ejemplos cualitativos

9. Calibracion inicial de modelos
- Tabla comparativa entre `gru_128`, `gru_256` y `lstm_256`
- Resaltar que `lstm_256` fue el mejor
- Dejar espacio para insertar la grafica de curvas de validacion

10. Calibracion fina
- Explicar que se exploraron hiperparametros alrededor del mejor LSTM
- Mostrar tabla resumida de resultados finos
- Concluir que no hubo una mejora global superior al `lstm_256` inicial

11. Comparacion de estrategias de inferencia
- Explicar diferencia entre greedy y beam search
- Mostrar tabla comparativa con BLEU y tiempo por imagen
- Resaltar el trade-off entre calidad y costo computacional

12. Resultados cualitativos
- Dejar espacio para insertar ejemplos de captions reales vs predichos
- Explicar fortalezas: captura de contexto global, objetos comunes y acciones frecuentes
- Explicar errores: descripciones genericas, alucinacion de elementos no presentes, falla en detalle fino

13. Relevancia de la solucion, limitaciones y trabajo futuro
- Relevancia: el sistema genera captions utiles y medibles
- Limitaciones: dataset pequeno, captions ambiguos, errores en escenas complejas, encoder fijo sin atencion
- Trabajo futuro: attention, mejor encoder, mas datos, optimizacion del beam search

14. Cierre
- Concluir que el proyecto demuestra la utilidad de deep learning multimodal para generar descripciones automaticas de imagenes
- Reafirmar que el mejor modelo fue `MobileNetV2 + LSTM(256)` y que `beam_3` se recomienda como estrategia final por balance entre calidad y tiempo

Estilo visual deseado:
- academico y profesional,
- limpio,
- con tipografia sobria,
- colores neutros con acentos azules o verdes,
- sin estilo corporativo de marketing,
- priorizar claridad de tablas, diagramas y resultados.

Instrucciones adicionales importantes:
- No omitir ninguno de los puntos de la rubrica.
- Enfatizar que hubo metodologia de analytics completa.
- Mostrar comparacion cuantitativa y cualitativa.
- Incluir bullets concretos, no parrafos largos.
- Usar lenguaje tecnico pero claro.
- Dejar espacios visuales donde luego se insertaran manualmente imagenes y figuras generadas en el proyecto.
- La presentacion debe ser apta para que al menos dos integrantes se repartan la exposicion.

Genera la presentacion ya estructurada slide por slide, con titulos, subtitulos y bullets listos.
