import tensorflow as tf

keras=tf.keras
cifar100=tf.keras.datasets.cifar100

(x_train,y_train),(x_test,y_test)=cifar100.load_data()
(x_train,x_test)=x_train/255.0,x_test/255.0

# print(x_train.shape)

model=tf.keras.models.Sequential([
    tf.keras.layers.Flatten(input_shape=(32,32,3)),
    tf.keras.layers.Dense(128,activation="relu"),
    tf.keras.layers.Dropout(.2),
    tf.keras.layers.Dense(100,activation="softmax")
])


print(model.compile(optimizer="adam",
                    loss='sparse_categorical_crossentropy',
                    metrics=['accuracy']))

print(model.fit(x_train,y_train,epochs=3,batch_size=10))
print(model.predict(x_test))
print(model.evaluate(x_test,y_test))
print(model.summary())