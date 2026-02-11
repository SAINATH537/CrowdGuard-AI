import tensorflow as tf
from tensorflow.keras import backend as K
from tensorflow.keras.layers import Layer


class AttentionLayer(Layer):
    def __init__(self, **kwargs):
        super(AttentionLayer, self).__init__(**kwargs)

    def build(self, input_shape):
        feature_dim = input_shape[-1]

        self.W = self.add_weight(
            name="att_weight",
            shape=(feature_dim, feature_dim),
            initializer="glorot_uniform",
            trainable=True
        )

        self.b = self.add_weight(
            name="att_bias",
            shape=(feature_dim,),
            initializer="zeros",
            trainable=True
        )

        self.u = self.add_weight(
            name="context_vector",
            shape=(feature_dim, 1),
            initializer="glorot_uniform",
            trainable=True
        )

        super(AttentionLayer, self).build(input_shape)

    def call(self, inputs):
        u_it = K.tanh(K.dot(inputs, self.W) + self.b)
        att = K.dot(u_it, self.u)
        att = K.squeeze(att, axis=-1)
        att_weights = K.softmax(att)
        att_weights_expanded = K.expand_dims(att_weights, axis=-1)
        weighted_input = inputs * att_weights_expanded
        output = K.sum(weighted_input, axis=1)
        return output

    def compute_output_shape(self, input_shape):
        return (input_shape[0], input_shape[-1])

    # 🔥 VERY IMPORTANT (Fixes model loading issues)
    def get_config(self):
        config = super(AttentionLayer, self).get_config()
        return config

    @classmethod
    def from_config(cls, config):
        return cls(**config)


model = None

try:
    model = tf.keras.models.load_model(
        'model/fight_detection_model.h5',
        custom_objects={'AttentionLayer': AttentionLayer},
        compile=False   # ⭐ prevents many legacy loading crashes
    )
    print("✅ Model loaded successfully!")

except FileNotFoundError:
    print("❌ Model file not found. Check the path.")

except Exception as e:
    print("🔥 FULL MODEL LOAD ERROR:")
    print(e)
