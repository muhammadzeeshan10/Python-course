import tensorflow as tf

keras=tf.keras
cifar10=keras.datasets.cifar10
kutils=keras.utils
klayers=keras.layers

from keras.utils import to_categorical

from keras import Sequential
from keras.layers import Conv2D,MaxPooling2D,Flatten,Dense,Dropout
from keras.metrics import Recall,Precision

(x_train,y_train),(x_test,y_test)=cifar10.load_data()
(x_train,x_test)=x_train/255.0,x_test/255.0


class_names = ['airplane', 'automobile', 'bird', 'cat', 'deer',
               'dog', 'frog', 'horse', 'ship', 'truck']


num_classes=10
y_train=to_categorical(y_train,num_classes)
y_test=to_categorical(y_test,num_classes)

# import numpy as np
# print(np.unique(y_train))


import matplotlib.pyplot as plt
import numpy as np
index = 1  # change to see different images
plt.imshow(x_train[index])
plt.title(class_names[np.argmax(y_train[index])])
plt.show()


print(x_train.shape)

model=Sequential([
    Conv2D(32,(3,3), activation="relu", input_shape=(32,32,3)),
    MaxPooling2D(2,2),
    Conv2D(64,(3,3), activation="relu"),
    MaxPooling2D((2,2)),
    Flatten(),
    Dense(128,activation="relu"),
    Dropout(0.3),
    Dense(num_classes,activation="softmax")
])

model.compile(optimizer='adam',
              loss='categorical_crossentropy',
              metrics=['accuracy', Precision(name='precision'), Recall(name='recall')])


# history=model.fit(
#     x_train,y_train,
#     epochs=20,
#     batch_size=32,
#     validation_data=(x_test,y_test),
#     verbose=1
# )




print("\n🧠 Model Summary:\n")
model.summary()


print("\n📊 Evaluating Model on Test Data...\n")
test_loss, test_accuracy, test_precision, test_recall = model.evaluate(x_test, y_test, verbose=1)

print(f"\n✅ Model Evaluation Results:")
print(f"Loss: {test_loss:.4f}")
print(f"Accuracy: {test_accuracy:.4f}")
print(f"Precision: {test_precision:.4f}")
print(f"Recall: {test_recall:.4f}")


from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay
import numpy as np
import matplotlib.pyplot as plt

y_pred = np.argmax(model.predict(x_test), axis=1)
y_true = np.argmax(y_test, axis=1)

cm = confusion_matrix(y_true, y_pred)
disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=class_names)
disp.plot(cmap='viridis', xticks_rotation='horizontal')
plt.show()

print("\n✅ Training & Evaluation Completed Successfully!")
input("Press Enter to exit...")
