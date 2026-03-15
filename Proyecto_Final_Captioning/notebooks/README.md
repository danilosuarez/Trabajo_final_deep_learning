# Notebooks del proyecto

Orden recomendado de ejecucion:
1. `01_eda_preprocesamiento.ipynb`
2. `02_modelado_baseline.ipynb`
3. `03_calibracion_modelos.ipynb`
4. `04_calibracion_fina_lstm.ipynb`
5. `05_inferencia_beam_search.ipynb`

Descripcion breve:
- `01`: carga, exploracion y preparacion de datos.
- `02`: baseline `MobileNetV2 + GRU`.
- `03`: calibracion inicial `GRU vs LSTM`.
- `04`: calibracion fina alrededor del mejor `LSTM`.
- `05`: comparacion de inferencia `greedy` vs `beam search`.

Si solo quieres reproducir los resultados finales, los notebooks clave son `03` y `05`.
