
import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
from tensorflow.keras import datasets, layers, models


# Analyze the image
def checkImage(image):
    (training_images, training_labels), (testing_images,
                                         testing_labels) = datasets.cifar10.load_data()

    print("hello")
    training_images, testing_images = training_images / 255, testing_images / 255

    class_names = ['Plane', 'Car', 'Bird', 'Cat',
                   'Deer', 'Dog', 'Frog', 'Horse', 'Ship', 'Truck']

    for i in range(16):
        plt.subplot(4, 4, i+1)
        plt.xticks([])
        plt.yticks([])
        plt.imshow(training_images[i], cmap=plt.cm.binary)
        plt.xlabel(class_names[training_labels[i][0]])

    training_images = training_images[:8000]
    training_labels = training_labels[:8000]
    testing_images = testing_images[:4000]
    testing_labels = testing_labels[:4000]

    model = models.load_model('image_classifier.model')

    #img = cv.imread(image_data)
    #img = cv.cvtColor(img, cv.COLOR_BGR2RGB)
    #plt.imshow(img, cmap=plt.cm.binary)

    prediction = model.predict(np.array([image]) / 255)
    index = np.argmax(prediction)

    return class_names[index]


# Compress the image into 32 x 32 pixel
def compress(file):

    image_data = file.read()

    # Convert image data into a NumPy array
    nparr = np.frombuffer(image_data, np.uint8)
    image = cv.imdecode(nparr, cv.IMREAD_COLOR)

    new_width = 32
    new_height = 32

    # Resize the image to the new dimensions
    compressed_image = cv.resize(image, (new_width, new_height))
    return checkImage(compressed_image)


# Train the CNN
'''

    model = models.Sequential()
    model.add(layers.Conv2D(32, (3, 3),
            activation='relu', input_shape=(32, 32, 3)))
    model.add(layers.MaxPooling2D((2, 2)))
    model.add(layers.Conv2D(64, (3, 3), activation='relu'))
    model.add(layers.MaxPooling2D((2, 2)))
    model.add(layers.Conv2D(64, (3, 3), activation='relu'))
    model.add(layers.Flatten())

    model.add(layers.Dense(64, activation='relu'))
    model.add(layers.Dense(10, activation='softmax'))

    model.compile(optimizer='adam',
                loss='sparse_categorical_crossentropy', metrics=['accuracy'])

    model.fit(training_images, training_labels, epochs=10,
            validation_data=(testing_images, testing_labels))

    loss, accuracy = model.evaluate(testing_images, testing_labels)

    print(f'Loss: {loss}')
    print(f'Accuracy: {accuracy}')
    model.save('image_classifier.model')

'''
