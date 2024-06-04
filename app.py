import streamlit as st
import os
os.environ['TF_ENABLE_ONEDNN_OPTS'] = '0'
import tensorflow as tf
from tensorflow.keras.models import load_model
from PIL import Image
import numpy as np

model = load_model('D:/streamlit/cnn_model_final.h5')


st.title('Fake Logo Detection System')

uploaded_image = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])

# if uploaded_image is not None:
#     # Preprocess the image
#     img = Image.open(uploaded_image)
#     img = img.convert('L')  # Convert to grayscale
#     img = img.resize((256, 256))  # Resize to match the model's input shape
#     img_array = np.array(img)
#     img_array = img_array / 255.0  # Normalize pixel values
#     #img_array = np.expand_dims(img_array, axis=-1)  # Add channel dimension
#     img_array = np.expand_dims(img_array, axis=0)  # Add batch dimension

#     # Make predictions
#     prediction = model.predict(img_array)
#     class_names = ['Real', 'Fake']
#     predicted_label = np.argmax(prediction)
#     result = class_names[predicted_label]

#     # Display the result
#     st.image(img, caption=f'Uploaded Image - Predicted as {result}', width=250, use_column_width=False)

if uploaded_image is not None:
    # Display the uploaded image
    image = Image.open(uploaded_image)
    st.image(image, caption='Uploaded Image', use_column_width=True)

    # Preprocess the image
    image = image.resize((256, 256))  # Resize to match model input size
    image = image.convert('L')  # Convert to grayscale
    image_array = tf.keras.preprocessing.image.img_to_array(image)
    image_array = image_array / 255.0  # Normalize pixel values

    # Make prediction
    img_array = tf.expand_dims(image_array, 0)  # Create batch dimension
    prediction = model.predict(img_array)
    predicted_class = "Real" if prediction[0][0] > 0.5 else "Fake"

    st.write(f'Prediction: {predicted_class}')    
    