# Fake Brand Logo Detection

This project involves detecting fake brand logos using a Convolutional Neural Network (CNN) built with TensorFlow and Keras. The trained model is saved in a `.pkl` format and deployed as a web application using Streamlit.

## Table of Contents
- [Introduction](#introduction)
- [Installation](#installation)
- [Dataset](#dataset)
- [Deployment](#deployment)
- [Screenshots](#Screenshots)
- [Dockerfile](#Dockerfile)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Introduction
Fake brand logos can be misleading and harmful to consumers. This project aims to classify logos as genuine or fake using a deep learning approach. The trained model is deployed as a web application for easy accessibility.

## Installation
To run this project, you need to have Python 3.x installed. Follow the steps below to set up the environment:

1. Clone the repository:
    ```bash
    git clone https://github.com/chetan-patil7/fake-brand-detection.git
    cd fake-brand-detection
    ```

2. Create a virtual environment and activate it:
    ```bash
    python -m venv venv
    source venv/bin/activate   # On Windows, use `venv\Scripts\activate`
    ```

3. Install the required packages:
    ```bash
    pip install -r requirements.txt
    ```

## Dataset
The dataset should be organized in folders representing the classes (genuine and fake logos). You can add your dataset in the `brands/` directory with subdirectories for each class.


This script preprocesses the images, defines the CNN architecture, and trains the model.

## Model Saving
After training, the model is saved in `.pkl` format for later use:

```python
import pickle

# Save the model
with open('model.pkl', 'wb') as file:
    pickle.dump(model, file)
```

## Deployment
The trained model is deployed using Streamlit. The `app.py` script handles the web interface:

```bash
streamlit run app.py
```
## Screenshots
![stremlit](https://github.com/chetan-patil7/fake_brand_detection/assets/108519641/65141574-4976-42db-8c3b-04d260edfcdb)
![stremlit2](https://github.com/chetan-patil7/fake_brand_detection/assets/108519641/f3e2fea3-e9b5-4229-bcd4-c8b6ce37c0db)
![streamlit3](https://github.com/chetan-patil7/fake_brand_detection/assets/108519641/fc295bb9-6151-48fc-a68c-aee18ba7c3fe)
![streamlit4](https://github.com/chetan-patil7/fake_brand_detection/assets/108519641/85067257-8880-4f0d-9603-675e462ef525)

The Streamlit app allows users to upload an image, which is then processed and classified as either genuine or fake.

## Dockerfile
## Docker Setup

To facilitate easy deployment and ensure a consistent environment, a Dockerfile is provided to containerize the application.

### Dockerfile Summary

The Dockerfile sets up a Docker container for the fake brand logo detection project. It uses the official Python 3.9 slim image as the base and performs the following steps:

1. **Sets the working directory to `/app`**

2. **Copies the current directory contents into the container**

3. **Installs the required Python packages**

4. **Exposes port 8501 for accessing the Streamlit app**
5. **Runs the Streamlit app when the container launches**

### Building and Running the Docker Container

1. **Build the Docker image**:
    ```bash
    docker build -t fake-logo-detection .
    ```

2. **Run the Docker container**:
    ```bash
    docker run -p 8501:8501 fake-logo-detection
    ```

After running the container, the Streamlit app will be accessible at `http://localhost:8501`.

---

## Usage
To use the web application:

1. Run the Streamlit app:
    ```bash
    streamlit run app.py
    ```

2. Open the provided URL in a web browser.
3. Upload an image of a brand logo.
4. The app will display whether the logo is genuine or fake.

## Contributing
Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

## License
This project is licensed under the MIT License. See the `LICENSE` file for more details.

---

This README file and the associated scripts provide a comprehensive guide to setting up and running the fake brand logo detection project. Feel free to modify and expand it based on your specific needs.
