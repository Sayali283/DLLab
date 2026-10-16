#Load MNIST database and perform operations like displaying the first 10 images, displaying labels and converting image into vector (784 neurons)  Explain me like i am 5 years kidfrom 
#Load Dataset
from tensorflow.keras.datasets import mnist
(x_train,y_train),(x_test,y_test)=mnist.load_data()
print("Dataset loaded Successfully!")
print("Training image shape:",x_train.shape)
print("Training labels shape:",y_train.shape)
print("Testing image shape:",x_test.shape)
print("Testing labels shape:",y_test.shape)

# Display First 10 rows
import matplotlib.pyplot as plt
plt.figure(figsize=(12,5))
for i in range(10):
  plt.subplot(2,5,i+1)
  plt.imshow(x_train[i],cmap='gray')
  plt.title(f"Image{i+1}")
  plt.axis('off')
plt.show()

#Display Labels of the first 10 images
print("Labels of the first 10 images:")
for i in range(10):
  print(y_train[i])

plt.figure(figsize=(12,5))
for i in range(10):
  plt.subplot(2, 5, i+1)
  plt.imshow(x_train[i], cmap="grey")
  plt.title(f"Label:{y_train[i]}")
  plt.axis("off")
plt.tight_layout()
plt.show()

import numpy as np
#Convert each image into a vector of 784 values
x_train_vector=x_train.reshape(x_train.shape[0],784)
x_test_vector =x_test.reshape(x_test.shape[0],784)
print("Original image shape",x_train.shape)
print("Training Vector shape",x_train.shape)
print("Testing vector shape",x_test_vector.shape)

#Displaying the first image as a vector
print("First image as a vector:")
print(x_train_vector[0])
print("Number of values in the first image:", len(x_train_vector[0]))

#Select the first image vector
first_image_vector=x_train_vector[0]
#print the vector length
print("Length vector:",first_image_vector.shape[0])
#Print the first 20 pixel value
print("first 20 pixels values:",first_image_vector[:20])

#Printing in 2D
plt.figure(figsize=(14,2))
plt.imshow(
    x_train_vector[0].reshape(1,784),
    cmap="gray",
    aspect="auto"
)
plt.title("First MNIST Image Flattened into 784 Values")
plt.xlabel("784 Pixel Values")
plt.yticks([])
plt.show()

