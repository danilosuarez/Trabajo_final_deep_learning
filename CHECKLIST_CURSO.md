# Checklist de Cumplimiento del Proyecto Final

## 1. Descripcion del problema o pregunta
- [x] Formular el problema de interes.
- [x] Explicar por que deep learning aporta valor.

## 2. Exploracion de los datos
- [x] Mostrar cantidad de imagenes y captions.
- [x] Mostrar ejemplos de imagenes con captions.
- [x] Analizar longitud de captions y vocabulario.

## 3. Preparacion de los datos
- [x] Limpiar texto.
- [x] Agregar tokens `startseq` y `endseq`.
- [x] Tokenizar captions.
- [x] Aplicar padding.
- [x] Extraer features visuales con la CNN.
- [x] Separar `train`, `validation` y `test` por imagen.

## 4. Seleccion del modelo y estrategia de estimacion
- [x] Justificar el uso de `CNN + LSTM/GRU`.
- [x] Explicar la eleccion del encoder visual.
- [x] Explicar hiperparametros calibrados.

## 5. Desarrollo y calibracion
- [x] Entrenar un baseline.
- [x] Comparar varias configuraciones del decoder.
- [x] Seleccionar el mejor modelo con criterio claro.
- [x] Evaluar una mejora de inferencia con `beam search`.

## 6. Visualizacion de resultados
- [x] Graficar perdida de entrenamiento y validacion.
- [x] Mostrar captions reales vs predichos.
- [x] Reportar metricas `BLEU`.

## 7. Implementacion y demostracion de utilidad
- [x] Probar el modelo con imagenes del conjunto de prueba.
- [x] Mostrar una demo simple en notebook.
- [x] Explicar limitaciones y mejoras futuras.

## Requisitos de entrega
- [x] Material listo para video-presentacion.
- [x] Resultados cuantitativos y cualitativos disponibles.
- [x] Guia de presentacion y prompt para Gamma AI creados.
- [ ] Grabar video final y subir enlace.
