# Dataset

## Dataset usado
Se utilizo `Flickr8k`.

## Descarga
El dataset **debe descargarse localmente**. No se incluye en este repositorio.

La idea es que cada usuario:
1. descargue `Flickr8k`,
2. copie las imagenes y el archivo de captions en `data/raw/`,
3. ejecute el pipeline desde los notebooks.

## Estructura local esperada
El proyecto fue implementado con esta estructura dentro de `data/raw/`:

```text
data/raw/
├── Images/
│   ├── 1000268201_693b08cb0e.jpg
│   ├── ...
├── captions.txt
```

`captions.txt` debe tener columnas:
- `image`
- `caption`

## Que se versiona y que no
Para mantener el repositorio liviano:
- **no** se versionan las imagenes crudas
- **no** se versionan features pesadas
- **no** se versionan pesos del modelo
- **si** se versionan notebooks, documentacion y resultados resumidos (`csv`, `png`)

## Archivos procesados generados por el proyecto
En `data/processed/` el pipeline genera:
- `captions_clean_split.csv` (local, pesado, no se versiona)
- `preprocessing_summary.json`
- `train_images.txt`
- `val_images.txt`
- `test_images.txt`
- `tokenizer.json`
- `image_features_mobilenetv2.pkl` (local, pesado, no se versiona)

## Validaciones minimas realizadas
- confirmacion del numero de imagenes en disco
- confirmacion del numero de captions
- ejemplos visuales de imagenes con descripcion
- analisis de longitud de captions
- split por imagen para evitar leakage entre entrenamiento, validacion y test

## Resumen del dataset ya procesado en este proyecto
- `8091` imagenes
- `40455` captions
- `5663` imagenes de entrenamiento
- `1213` imagenes de validacion
- `1215` imagenes de prueba
- vocabulario: `7251`
- longitud maxima: `38`
