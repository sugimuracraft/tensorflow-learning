import ssl
import tensorflow as tf

# fix to Exception: URL fetch failure on https://www.cs.toronto.edu/~kriz/cifar-100-python.tar.gz: None
# -- [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: unable to get local issuer certificate
#  (_ssl.c:1129)
ssl._create_default_https_context = ssl._create_unverified_context


if __name__ == "__main__":
    cifar = tf.keras.datasets.cifar100
    (x_train, y_train), (x_test, y_test) = cifar.load_data()
    model = tf.keras.applications.ResNet50(
        include_top=True,
        weights=None,
        input_shape=(32, 32, 3),
        classes=100,
    )

    loss_fn = tf.keras.losses.SparseCategoricalCrossentropy(from_logits=False)
    model.compile(optimizer="adam", loss=loss_fn, metrics=["accuracy"])
    model.fit(x_train, y_train, epochs=5, batch_size=64)
