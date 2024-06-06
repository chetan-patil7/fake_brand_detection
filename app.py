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
    