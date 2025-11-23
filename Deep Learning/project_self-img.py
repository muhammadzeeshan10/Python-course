import tensorflow as tf
from tensorflow.keras.preprocessing.image import ImageDataGenerator, load_img, img_to_array
from tensorflow.keras import layers, models
import matplotlib.pyplot as plt
import numpy as np
import os


train_dir = r"D:\AI\Deep Learning\data_sets\train"
test_dir = r"D:\AI\Deep Learning\data_sets\test"


train_datagen = ImageDataGenerator(rescale=1./255)
test_datagen = ImageDataGenerator(rescale=1./255)

train_generator = train_datagen.flow_from_directory(
    train_dir,
    target_size=(128, 128),
    batch_size=2,
    class_mode='categorical'
)

test_generator = test_datagen.flow_from_directory(
    test_dir,
    target_size=(128, 128),
    batch_size=2,
    class_mode='categorical'
)


class_names = list(train_generator.class_indices.keys())
print("\n📂 Classes detected:", class_names)

# Show Few Training Images (Before Training) ---
plt.figure(figsize=(6, 6))
for i in range(len(train_generator.filenames)):
    img_path = os.path.join(train_dir, train_generator.filenames[i])
    img = load_img(img_path, target_size=(128, 128))
    plt.subplot(2, 2, i + 1)
    plt.imshow(img)
    plt.title("Before Training")
    plt.axis("off")
    if i == 3:  
        break
plt.show()

# --- Step 3: Build Model ---
model = models.Sequential([
    layers.Input(shape=(128, 128, 3)),
    layers.Conv2D(32, (3, 3), activation='relu'),
    layers.MaxPooling2D(2, 2),
    layers.Conv2D(64, (3, 3), activation='relu'),
    layers.MaxPooling2D(2, 2),
    layers.Flatten(),
    layers.Dense(128, activation='relu'),
    layers.Dropout(0.3),
    layers.Dense(train_generator.num_classes, activation='softmax')
])


model.compile(optimizer='adam',
              loss='categorical_crossentropy',
              metrics=['accuracy'])

history = model.fit(
    train_generator,
    epochs=10,
    validation_data=test_generator,
    verbose=1
)


plt.plot(history.history['accuracy'], label='Train Accuracy')
plt.plot(history.history['val_accuracy'], label='Test Accuracy')
plt.title("Training vs Testing Accuracy")
plt.legend()
plt.show()


print("\n📸 Showing Predictions (After Training):")

# Pick one image from test folder
for img_file in os.listdir(os.path.join(test_dir, class_names[0])):
    img_path = os.path.join(test_dir, class_names[0], img_file)

    img = load_img(img_path, target_size=(128, 128))
    img_array = img_to_array(img) / 255.0
    img_array = np.expand_dims(img_array, axis=0)  

    prediction = model.predict(img_array)
    predicted_class = class_names[np.argmax(prediction)]

    plt.imshow(img)
    plt.title(f"Predicted: {predicted_class}")
    plt.axis("off")
    plt.show()
    break  


model.save("zeeshan_model.h5")
print("\n✅ Model trained, tested, and saved successfully as 'zeeshan_model.h5'!")
