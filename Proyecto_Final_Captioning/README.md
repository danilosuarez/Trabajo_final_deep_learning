# Proyecto Final - Image Captioning con Encoder-Decoder

Proyecto final del curso de Deep Learning, desarrollado bajo la **Opcion 3**: comentario automatico de imagenes.

## Problema
Construir un modelo capaz de recibir una imagen y generar una descripcion corta en lenguaje natural.

Pregunta de interes:
> Es posible generar descripciones utiles y semanticamente consistentes para imagenes usando una arquitectura Encoder-Decoder basada en `MobileNetV2` y `LSTM`, calibrada con tecnicas vistas en el curso.

## Enfoque
La solucion integra tres bloques vistos en clase:
1. `CNN + transfer learning` para extraer informacion visual.
2. `Embedding + LSTM/GRU` para modelar lenguaje secuencial.
3. `Encoder-Decoder` para generar captions palabra por palabra.

Arquitectura final entrenada:
- `Encoder`: `MobileNetV2` preentrenada en `ImageNet`
- `Decoder`: `Embedding + LSTM(256)`
- Estrategia de inferencia recomendada: `beam_3`

## Dataset
Se uso `Flickr8k` con la estructura local descrita en [DATASET.md](./DATASET.md).

Importante:
- el dataset **no** se incluye en este repositorio,
- las imagenes y `captions.txt` deben descargarse y ubicarse localmente en `data/raw/`,
- esto se hizo para mantener el repositorio liviano y evitar versionar archivos pesados.

Resumen del dataset procesado:
- `8091` imagenes
- `40455` captions
- `5663` imagenes de entrenamiento
- `1213` imagenes de validacion
- `1215` imagenes de prueba
- vocabulario final: `7251`
- longitud maxima de caption: `38`

## Resultados principales
### Baseline
Modelo: `MobileNetV2 + GRU`
- `BLEU-1 = 0.4860`
- `BLEU-2 = 0.3279`

### Calibracion inicial
Se compararon:
- `gru_128`
- `gru_256`
- `lstm_256`

Mejor resultado entrenado:
- `lstm_256`
- `best_val_loss = 3.3898`
- `best_val_accuracy = 0.3687`
- `BLEU-1 = 0.6130`
- `BLEU-2 = 0.4244`
- `training_time = 9.98 min`

### Calibracion fina
Se probaron variantes cercanas del mejor `LSTM`, pero no superaron de forma global al `lstm_256` de la calibracion inicial.

### Inferencia: Greedy vs Beam Search
- `greedy`: `BLEU-2 = 0.4244`, `0.3683 s/imagen`
- `beam_3`: `BLEU-2 = 0.4354`, `1.1349 s/imagen`
- `beam_5`: `BLEU-2 = 0.4495`, `1.8327 s/imagen`

Decision recomendada:
- mejor modelo entrenado: `lstm_256`
- mejor estrategia calidad-tiempo: `beam_3`
- mejor estrategia numericamente: `beam_5`

## Estructura del proyecto
```text
Proyecto_Final_Captioning/
├── README.md
├── DATASET.md
├── CHECKLIST_CURSO.md
├── ARQUITECTURA_Y_RUBRICA.md
├── GUIA_PRESENTACION_VIDEO.md
├── PROMPT_GAMMA_AI.md
├── requirements-macos-metal.txt
├── data/
│   ├── raw/
│   └── processed/
├── models/
├── notebooks/
├── outputs/
│   ├── figures/
│   └── predictions/
├── reports/
└── src/
```

## Notebooks
- [01_eda_preprocesamiento.ipynb](./notebooks/01_eda_preprocesamiento.ipynb)
- [02_modelado_baseline.ipynb](./notebooks/02_modelado_baseline.ipynb)
- [03_calibracion_modelos.ipynb](./notebooks/03_calibracion_modelos.ipynb)
- [04_calibracion_fina_lstm.ipynb](./notebooks/04_calibracion_fina_lstm.ipynb)
- [05_inferencia_beam_search.ipynb](./notebooks/05_inferencia_beam_search.ipynb)

## Resultados que conviene mostrar en la entrega
Figuras ya generadas:
- `outputs/predictions/calibration_validation_curves.png`
- `outputs/predictions/calibration_qualitative_examples.png`
- `outputs/predictions/fine_calibration_validation_curves.png`
- `outputs/predictions/fine_calibration_qualitative_examples.png`
- `outputs/predictions/beam_search_qualitative_examples.png`

Tablas ya generadas:
- `outputs/predictions/calibration_results_final.csv`
- `outputs/predictions/fine_calibration_results_final.csv`
- `outputs/predictions/beam_search_results.csv`

## Reproducibilidad
Este repositorio no versiona:
- imagenes crudas del dataset,
- features procesadas pesadas,
- pesos `.keras`,
- entornos locales.

Para replicar el proyecto:
1. descarga localmente `Flickr8k`
2. ubica `captions.txt` e imagenes en `data/raw/` como se describe en [DATASET.md](./DATASET.md)
3. crea un entorno compatible con TensorFlow
4. ejecuta los notebooks en orden

Para Mac Apple Silicon con `tensorflow-metal`, revisa [requirements-macos-metal.txt](./requirements-macos-metal.txt).

## Opciones de ejecucion
### Opcion 1: ejecucion local con GPU en Mac Apple Silicon
El proyecto fue corrido localmente en MacBook Pro con chip `Apple M1 Max`, usando:
- `tensorflow-macos`
- `tensorflow-metal`

Si tienes un entorno similar, puedes seguir la configuracion de [requirements-macos-metal.txt](./requirements-macos-metal.txt).

### Opcion 2: ejecucion en Google Colab
Si no cuentas con aceleracion local o prefieres una configuracion mas simple, el proyecto tambien puede correrse en `Google Colab`.

En ese caso:
- descarga el dataset localmente o montalo desde Drive,
- respeta la misma estructura de `data/raw/`,
- ejecuta los notebooks en el mismo orden.
