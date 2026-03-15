from __future__ import annotations

import tensorflow as tf


def main() -> None:
    print("TensorFlow:", tf.__version__)
    print("All devices:", tf.config.list_physical_devices())
    print("GPU devices:", tf.config.list_physical_devices("GPU"))

    # Prueba minima de operaciones para confirmar que el entorno carga bien.
    x = tf.random.normal((1024, 1024))
    y = tf.random.normal((1024, 1024))
    z = tf.matmul(x, y)
    print("Matmul shape:", z.shape)


if __name__ == "__main__":
    main()
