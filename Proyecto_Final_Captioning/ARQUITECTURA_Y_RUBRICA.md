# Arquitectura del Proyecto y Alineacion con la Rubrica

## Opcion escogida
`Opcion 3: Modelo automatico para comentar imagenes`

## Pregunta de interes
¿Es posible construir un modelo de deep learning que, a partir de una imagen, genere una descripcion corta y coherente en lenguaje natural que resuma su contenido principal?

## Objetivo del proyecto
Desarrollar un sistema de `image captioning` que reciba una imagen y produzca automaticamente una frase descriptiva.

## Arquitectura propuesta
La solucion combina dos bloques:

### 1. Encoder visual
Su funcion es convertir la imagen en una representacion numerica compacta.

Modelo sugerido:
- `MobileNetV2` o `ResNet50` preentrenada en `ImageNet`

Salida:
- vector de caracteristicas visuales

Justificacion:
- semana 6 cubrio `CNN` y `transfer learning`
- permite aprovechar conocimiento visual ya aprendido
- reduce costo de entrenamiento frente a entrenar una CNN desde cero

### 2. Decoder de lenguaje
Su funcion es tomar las caracteristicas visuales y generar la descripcion palabra a palabra.

Modelo sugerido:
- `Embedding`
- `GRU` o `LSTM`
- `Dense + Softmax`

Salida:
- distribucion de probabilidad sobre el vocabulario en cada paso

Justificacion:
- semana 7 cubrio `Embedding`, `LSTM`, `GRU`
- semana 8 cubrio `Encoder-Decoder`
- el problema es secuencial: la palabra siguiente depende de la imagen y de las palabras previas

## Flujo de datos del modelo
```text
Imagen
  -> CNN preentrenada
  -> vector de features
  -> Decoder (Embedding + GRU/LSTM)
  -> palabra 1
  -> palabra 2
  -> ...
  -> caption final
```

## Version baseline recomendada
Para mantener el proyecto defendible y ejecutable en el tiempo del curso:

- `Encoder`: `MobileNetV2` congelada
- `Decoder`: `Embedding + GRU`
- `Decodificacion`: `greedy decoding`

Esta version es suficiente para demostrar:
- uso de `deep learning`
- integracion de vision + NLP
- entrenamiento y calibracion
- generacion real de captions en imagenes nuevas

## Alineacion con la rubrica

### 1. Descripcion del problema o pregunta de interes
Problema:
- En plataformas digitales, catalogos o redes sociales es util generar descripciones automaticas de imagenes.

Valor:
- mejora indexacion
- mejora accesibilidad
- ayuda a organizar grandes colecciones de imagenes

Que deben mostrar:
- por que este problema si justifica `deep learning`
- por que generar texto desde imagen es mas que una clasificacion tradicional

### 2. Exploracion de los datos
Que deben analizar:
- numero de imagenes
- numero de captions
- captions por imagen
- longitud de captions
- ejemplos de imagenes con sus descripciones

Mensaje que deben dejar claro:
- entienden tanto la parte visual como la parte textual del dataset

### 3. Preparacion de los datos
Debe incluir:
- limpieza de captions
- tokens `startseq` y `endseq`
- tokenizacion
- padding
- separacion `train`, `val`, `test` por imagen
- extraccion de features con CNN

Mensaje que deben dejar claro:
- no hubo fuga de informacion
- el pipeline deja los datos listos para el modelo

### 4. Seleccion del modelo
Modelos candidatos razonables:
- `CNN + GRU`
- `CNN + LSTM`

Argumento recomendado:
- un `MLP` no sirve bien porque no modela secuencia
- una `CNN` sola no genera lenguaje
- el problema necesita un `Encoder-Decoder`

### 5. Desarrollo y calibracion
Comparaciones sugeridas:
- `GRU` vs `LSTM`
- `MobileNetV2` vs `ResNet50` como encoder congelado
- dimension del `Embedding`
- numero de unidades recurrentes

Criterio de seleccion:
- perdida en validacion
- calidad cualitativa de captions
- si es posible, `BLEU`

### 6. Visualizacion de resultados
Deben mostrar:
- curvas de entrenamiento y validacion
- ejemplos de imagen + caption real + caption predicho
- comparacion de modelos

Si alcanzan:
- `BLEU-1` y `BLEU-2`

### 7. Implementacion y utilidad
Demo minima:
- tomar 3 a 5 imagenes nuevas
- correr inferencia
- mostrar caption generado

Mensaje final:
- en que escenarios seria util
- limitaciones del modelo
- mejoras futuras

## Estructura sugerida del video de 12 minutos

### 1. Introduccion y opcion escogida
- decir explicitamente: `Opcion 3`
- plantear pregunta de interes

### 2. Datos
- dataset
- ejemplos visuales
- hallazgos de EDA

### 3. Preparacion
- limpieza de captions
- tokenizacion
- split
- extraccion de features

### 4. Arquitectura
- encoder visual
- decoder secuencial
- por que se eligio esa arquitectura

### 5. Calibracion
- modelos comparados
- criterio de seleccion

### 6. Resultados
- graficas
- captions reales vs generados
- metricas

### 7. Cierre
- utilidad
- limitaciones
- trabajo futuro

## Frase corta para explicar el proyecto
`Nuestro modelo recibe una imagen, extrae sus patrones visuales con una CNN preentrenada y luego genera una descripcion en texto usando un decoder recurrente palabra por palabra.`
