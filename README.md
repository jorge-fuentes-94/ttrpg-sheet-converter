# TTRPG Sheet Converter

Proyecto en curso para leer fichas de personaje de rol escaneadas o fotografiadas y pasar sus datos a texto.

El primer paso ya funciona: **alinear el escaneo con la ficha original**. Una foto de una ficha suele estar girada; el programa la compara con la ficha en blanco del juego, encuentra puntos en común y la endereza para que después cada casilla esté en su sitio.

## Qué hace ahora

- `image_aligner.py`: detecta puntos clave en las dos imágenes con **ORB** (OpenCV), los empareja, calcula la homografía con **RANSAC** y de ahí el ángulo de giro; después rota el escaneo.
- `image_selector.py`: pregunta por consola qué ficha (de momento solo D&D 5e) y qué escaneo usar.
- `image_processor.py`: une las dos piezas y muestra la ficha original, el escaneo y el escaneo enderezado.
- `originals/`: fichas en blanco de D&D 5e. `scans/`: escaneos de prueba.

## Cómo probarlo

```bash
pip install opencv-python numpy
python image_processor.py
```

Las rutas de las imágenes están fijas al principio de `image_processor.py`; cámbialas para probar otro escaneo.

## Lo que falta

- Leer el texto de cada casilla con OCR (`image_reader.py` está empezado con EasyOCR).
- Recortar las zonas de la ficha (atributos, habilidades, conjuros) y volcarlas a JSON.
- Soportar otras fichas además de la de D&D 5e.
