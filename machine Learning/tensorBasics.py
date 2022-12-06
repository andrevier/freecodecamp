import tensorflow as tf

# Example of a tensor
print("-------------")
print("Constant tensor t")
t = tf.constant([[1., 2., 3.],[4., 5., 6.]])
print(t)
# Constant is immutable. 
t1 = tf.constant([[2., 1., 4.],[1., 5., 1.]])
print("-------------")
print("t1\n", t1)

print("-------------")
print("sum of t1 and t:")
print(t1 + t)

# Element-by-element product.
print("-------------")
print("Product t1*t")
print(t1*t)

# About layers and graphs.
print("-------------")
print("Layers and graphs.")
i = tf.ones((1,4))
print(i)
layer = tf.keras.layers.Dense(3)
y = layer(i)
print(len(y))
print(layer.weights)

# Sequential model
print("-------------")
model = tf.keras.Sequential(
    [
        tf.keras.layers.Dense(2, activation="relu"),
        tf.keras.layers.Dense(3, activation="relu"),
        tf.keras.layers.Dense(4),
    ]
) 
y1 = model(i)
print(model.summary())


